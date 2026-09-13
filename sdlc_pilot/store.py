"""Immutable artifact publication without a separate, crash-sensitive index."""

from dataclasses import dataclass, asdict
from pathlib import Path
import hashlib
import json
import math
import os
import re
import tempfile


class StoreError(ValueError):
    pass


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise StoreError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(raw: bytes):
    def invalid_constant(value):
        raise StoreError(f"Non-finite JSON number: {value}")

    def finite_float(value):
        number = float(value)
        if not math.isfinite(number):
            raise StoreError("JSON number exceeds finite floating-point range")
        return number

    try:
        result = json.loads(raw.decode("utf-8"), object_pairs_hook=_unique_object,
                            parse_constant=invalid_constant, parse_float=finite_float)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise StoreError(f"Invalid UTF-8 JSON: {exc}") from exc
    if not isinstance(result, dict):
        raise StoreError("Artifact must be a JSON object")
    return result


def encode(document):
    try:
        return (json.dumps(document, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
    except (ValueError, TypeError) as exc:
        raise StoreError(str(exc)) from exc


def normalized_windows_path(path):
    # Windows realpath can retain the extended-length prefix during races with
    # newly created paths. Normalize both sides before the containment check.
    value = str(path)
    if os.name == "nt":
        if value.startswith('\\\\?\\UNC\\'):
            value = '\\\\' + value[8:]
        elif value.startswith('\\\\?\\'):
            value = value[4:]
    return Path(value)


@dataclass(frozen=True)
class Identity:
    project_id: str
    run_id: str
    iteration_id: str
    artifact_id: str
    artifact_version: str

    def __post_init__(self):
        for field in ("project_id", "run_id", "artifact_id"):
            value = getattr(self, field)
            if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}", value):
                raise StoreError(f"Unsafe {field}")
        if not isinstance(self.iteration_id,str) or not re.fullmatch(r"ITER-\d{3,}", self.iteration_id):
            raise StoreError("Invalid iteration_id")
        if not isinstance(self.artifact_version,str) or not re.fullmatch(r"\d+\.\d+", self.artifact_version):
            raise StoreError("Invalid artifact_version")

    @classmethod
    def from_reference(cls, reference):
        try:
            return cls(**{k: reference[k] for k in cls.__dataclass_fields__})
        except (KeyError, TypeError) as exc:
            raise StoreError("Incomplete artifact identity") from exc


SLUGS = {
    "PILOT-INPUT": "pilot-input", "A16": "test-case-creation-outputs",
    "A17": "test-coverage-review-outputs", "A05": "requirements-review-outputs",
    "A04": "acceptance-criteria-outputs", "A15": "test-planning-outputs",
    "A06": "feasibility-assessment-outputs", "A09": "system-component-design-outputs",
    "E09": "human-decisions", "E06": "test-and-defect-baselines", "E01": "business-context",
}


class ArtifactStore:
    """Use an owner-controlled directory on a local filesystem supporting hard links.

    Atomic no-replace publication handles concurrent publishers and a crash after
    publication. No mutable index or latest pointer is needed. Filesystem users
    with write access remain trusted; this is not a hostile-process sandbox.
    """

    def __init__(self, root):
        self.root = normalized_windows_path(Path(root).resolve())
        self.root.mkdir(parents=True, exist_ok=True)

    def path_for(self, identity):
        key = hashlib.sha256(encode(asdict(identity))).hexdigest()
        slug = SLUGS.get(identity.artifact_id, identity.artifact_id.lower())
        filename = f"{identity.artifact_id}_{slug}_{identity.iteration_id}_v{identity.artifact_version}.json"
        path = self.root / "objects" / key / filename
        resolved = normalized_windows_path(path.resolve())
        if not resolved.is_relative_to(self.root):
            raise StoreError(f"Artifact path escapes the configured store: {resolved} (root {self.root})")
        return path

    def publish(self, identity, document):
        return self.publish_bytes(identity, encode(document))

    def publish_bytes(self, identity, raw):
        document = parse_json(raw)
        for field, value in asdict(identity).items():
            if field in document and document[field] != value:
                raise StoreError(f"Document identity differs: {field}")
        schema_version = document.get("schema_version")
        if not isinstance(schema_version, str) or not re.fullmatch(r"\d+\.\d+", schema_version):
            raise StoreError("Missing or invalid schema_version")
        path = self.path_for(identity)
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path_for(identity)  # Check newly created parents for redirected paths.
        fd, temporary = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            self._publish_no_replace(Path(temporary), path, raw)
        finally:
            Path(temporary).unlink(missing_ok=True)
        return {**asdict(identity), "schema_version": schema_version,
                "sha256": hashlib.sha256(raw).hexdigest()}

    @staticmethod
    def _publish_no_replace(temporary, path, raw):
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.read_bytes() != raw:
                raise StoreError("Artifact version already exists with different content")
        except OSError as exc:
            raise StoreError(f"Atomic publication failed; no overwrite fallback: {exc}") from exc
        # On POSIX, persist the directory entry as well as the file data.
        if os.name != "nt":
            directory = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)

    def read(self, reference):
        identity = Identity.from_reference(reference)
        expected = reference.get("sha256", "")
        if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected) or expected == "0" * 64:
            raise StoreError("Invalid or unresolved artifact digest")
        path = self.path_for(identity)
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise StoreError(f"Missing or unreadable artifact: {identity.artifact_id}") from exc
        if hashlib.sha256(raw).hexdigest() != expected:
            raise StoreError("Artifact digest mismatch")
        result = parse_json(raw)
        if result.get("schema_version") != reference.get("schema_version"):
            raise StoreError("Artifact schema version mismatch")
        for field, value in asdict(identity).items():
            if field in result and result[field] != value:
                raise StoreError(f"Stored identity differs: {field}")
        return result

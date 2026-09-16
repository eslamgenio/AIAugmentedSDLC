class Monitor:
    def __init__(self):
        self.states = {}
        self.notifications = []
        self.notified = set()

    def register(self, device):
        self.states[device] = {"status": "ONLINE", "misses": 0}

    def process(self, device, event):
        state = self.states[device]
        if event == "HEARTBEAT_RECEIVED":
            state["misses"] = 0
            state["status"] = "ONLINE"
            self.notified.discard(device)
        elif event == "HEARTBEAT_MISSED":
            state["misses"] += 1
            if state["misses"] >= 3:
                state["status"] = "OFFLINE"
                if device not in self.notified:
                    self.notifications.append(device)
                    self.notified.add(device)
        else:
            raise ValueError("Unsupported event")
        return state["status"]

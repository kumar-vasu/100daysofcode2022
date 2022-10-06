class TimeMap:

    def __init__(self):
        self.store = {}
        self.key_stack = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
            self.key_stack[key] = []
        self.store[key][timestamp] = value
        self.key_stack[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        timestamp_index = len(self.key_stack[key]) - 1
        timestamp_prev = None
        while timestamp_index >= 0:
            if self.key_stack[key][timestamp_index] <= timestamp:
                timestamp_prev = self.key_stack[key][timestamp_index]
                break
            timestamp_index -= 1
        if timestamp_prev:
            return self.store[key][timestamp_prev]
        else:
            return ""
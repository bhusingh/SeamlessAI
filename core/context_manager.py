import os
import json
from threading import Lock

CONTEXT_FILE = "user_context.json"
_LOCK = Lock()

class ContextManager:
    def __init__(self, path=CONTEXT_FILE):
        self.path = path
        # create file if missing
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f, indent=2)

    def load_all(self):
        with _LOCK:
            with open(self.path, "r") as f:
                return json.load(f)

    def load_context(self, user_id):
        with _LOCK:
            with open(self.path, "r") as f:
                data = json.load(f)
            return data.get(user_id, [])

    def save_context(self, user_id, messages):
        # messages: list of strings (alternating user and assistant)
        with _LOCK:
            with open(self.path, "r") as f:
                data = json.load(f)
            data[user_id] = messages
            with open(self.path, "w") as f:
                json.dump(data, f, indent=2)

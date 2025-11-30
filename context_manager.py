import json
import os

CONTEXT_FILE = "user_context.json"

def load_context(user_id):
    if os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}
    return data.get(user_id, [])

def save_context(user_id, messages):
    if os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}
    data[user_id] = messages
    with open(CONTEXT_FILE, "w") as f:
        json.dump(data, f)

import json
from threading import Lock

lock = Lock()

def read_db():
    with lock:
        with open("database.json", "r") as f:
            return json.load(f)

def write_db(data):
    with lock:
        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)
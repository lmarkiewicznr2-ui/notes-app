import json
import os

FILE = "notes.json"

def read_notes():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=2)
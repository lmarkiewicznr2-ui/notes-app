import json
import os

BASE_DIR = "notes"

def get_file(name):
    os.makedirs(BASE_DIR, exist_ok=True)
    return os.path.join(BASE_DIR, f"{name}.json")

def read_notes(name):
    file = get_file(name)

    if not os.path.exists(file):
        return []

    try:
        with open(file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def write_notes(name, notes):
    file = get_file(name)

    with open(file, "w") as f:
        json.dump(notes, f, indent=2)
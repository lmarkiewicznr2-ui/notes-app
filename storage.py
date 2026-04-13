import json
import os

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

DATA_DIR = "data"
BASE_DIR = os.path.join(DATA_DIR, "notes")
CURRENT_FILE = os.path.join(DATA_DIR, ".current")

def set_current_list(name):
    os.makedirs(BASE_DIR, exist_ok=True)
    with open(CURRENT_FILE, "w") as f:
        f.write(name)

def get_current_list():
    if not os.path.exists(CURRENT_FILE):
        return None

    with open(CURRENT_FILE, "r") as f:
        return f.read().strip()
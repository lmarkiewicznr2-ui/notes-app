from storage import read_notes, write_notes
import sys
import os

def add(args):
    if len(args) < 2:
        print("Usage: note add <list> <text>")
        return

    name = args[0]
    text = " ".join(args[1:])

    notes = read_notes(name)
    notes.append(text)
    write_notes(name, notes)

    print(f"[{name}] Added: {text}")

def list_notes(args):
    if not args:
        print("Usage: note list <list>")
        return

    name = args[0]
    notes = read_notes(name)

    if not notes:
        print(f"[{name}] No notes yet!")
        return

    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n}")

def delete(args):
    if not args:
        print("Usage: note del <num... or text...>")
        return

    notes = read_notes()

    # CASE 1: all numbers → delete by index
    if all(a.isdigit() for a in args):
        indices = sorted(set(int(a) for a in args), reverse=True)

        removed = 0

        for i in indices:
            if 1 <= i <= len(notes):
                notes.pop(i - 1)
                removed += 1

        write_notes(notes)
        print(f"[{name}] Deleted {removed} note(s) by index")
        return

    # CASE 2: word / text delete
    query = " ".join(args).lower()

    new_notes = []
    removed = 0

    for n in notes:
        if query in n.lower():
            removed += 1
            continue
        new_notes.append(n)

    write_notes(new_notes)

    print(f"Deleted {removed} note(s) containing '{query}'")




def list_lists():
    base_dir = "notes"

    if not os.path.exists(base_dir):
        print("No lists yet!")
        return

    files = os.listdir(base_dir)

    if not files:
        print("No lists yet!")
        return

    print("Lists:")

    for f in files:
        if f.endswith(".json"):
            name = f[:-5]  # remove .json
            print(f"- {name}")


def remove_list(args):
    if not args:
        print("Usage: note remove-list <list>")
        return

    name = args[0]
    file = os.path.join("notes", f"{name}.json")

    if not os.path.exists(file):
        print(f"[{name}] List does not exist")
        return

    confirm = input(f"Delete list '{name}'? (y/n): ").lower()

    if confirm != "y":
        print("Cancelled")
        return

    os.remove(file)
    print(f"[{name}] List deleted")
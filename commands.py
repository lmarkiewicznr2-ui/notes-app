from storage import read_notes, write_notes
import sys

def add(args):
    if not args:
        print("Usage: note add <text>")
        return

    notes = read_notes()
    notes.append(" ".join(args))
    write_notes(notes)
    print(f"Added: {notes[-1]}")

def list_notes():
    notes = read_notes()

    if not notes:
        print("No notes yet!")
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
        print(f"Deleted {removed} note(s) by index")
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
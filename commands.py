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
        print("Usage: note del <number>")
        return

    try:
        index = int(args[0])
    except ValueError:
        print("Invalid number")
        return

    notes = read_notes()

    if index < 1 or index > len(notes):
        print("Invalid number")
        return

    notes.pop(index - 1)
    write_notes(notes)
    print("Deleted note")
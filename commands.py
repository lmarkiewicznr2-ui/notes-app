from storage import read_notes, write_notes
from storage import read_notes, write_notes, get_current_list, set_current_list
import sys
import os

def add(args):
    if len(args) < 2:
        print("Usage: note add <list> <text>")
        return

    name = args[0]
    text = " ".join(args[1:])
    set_current_list(name)
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
        print("Usage: note del <list> <num... or text...>")
        return

    # detect list
    if args[0].isdigit():
        name = get_current_list()
        rest = args

        if not name:
            print("No list specified and no default list set")
            return
    else:
        name = args[0]
        rest = args[1:]
        set_current_list(name)

    if not rest:
        print("Nothing to delete")
        return

    notes = read_notes(name)

    if not notes:
        print(f"[{name}] No notes found")
        return

    # numeric delete
    if all(a.isdigit() for a in rest):
        indices = sorted(set(int(a) for a in rest), reverse=True)

        removed = 0

        for i in indices:
            if 1 <= i <= len(notes):
                notes.pop(i - 1)
                removed += 1

        write_notes(name, notes)
        print(f"[{name}] Deleted {removed} note(s) by index")
        return

    # text delete
    query = " ".join(rest).lower()

    new_notes = [n for n in notes if query not in n.lower()]
    removed = len(notes) - len(new_notes)

    write_notes(name, new_notes)

    print(f"[{name}] Deleted {removed} note(s) containing '{query}'")



def search(args):
    if not args:
        print("Usage: note find <list?> <text>")
        return

    # detect if list is provided
    if len(args) >= 2 and not args[0].isdigit():
        name = args[0]
        query = " ".join(args[1:])
        set_current_list(name)
    else:
        name = get_current_list()
        query = " ".join(args)

        if not name:
            print("No list specified and no default list set")
            return

    notes = read_notes(name)

    if not notes:
        print(f"[{name}] No notes found")
        return

    query_lower = query.lower()

    found = False

    for i, n in enumerate(notes, start=1):
        if query_lower in n.lower():
            print(f"{i}. {n}")
            found = True

    if not found:
        print(f"[{name}] No matches for '{query}'")
import sys



usage = """
Usage:
  python notes.py add <note>
  python notes.py list
  python notes.py delete <number>
"""







if len(sys.argv) < 2:
    print(usage)
    sys.exit()

command = sys.argv[1]




def add_note():
    if len(sys.argv) < 3:
        print(usage)
        sys.exit()

    note = " ".join(sys.argv[2:])

    try:
        with open("notes.txt", "r") as file:
            lines = [line.split(". ", 1)[1] for line in file.read().splitlines()]
    except FileNotFoundError:
        lines = []

    lines.append(note)

    with open("notes.txt", "w") as file:
        for i, n in enumerate(lines, start=1):
            file.write(f"{i}. {n}\n")




def list_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read().strip()
            if not content:
                print("No notes yet!")
            else:
                print(content)
    except FileNotFoundError:
        print("No notes yet!")





def delete_note():
    if len(sys.argv) < 3:
        print("Usage: python notes.py delete <number>")
        sys.exit()

    try:
        with open("notes.txt", "r") as file:
            lines = file.read().splitlines()

        index = int(sys.argv[2])

        if index < 1 or index > len(lines):
            print("Invalid note number")
            sys.exit()

        lines.pop(index - 1)

        with open("notes.txt", "w") as file:
            for i, n in enumerate(lines, start=1):
                file.write(f"{i}. {n}\n")

    except FileNotFoundError:
        print("No notes yet!")
        sys.exit()





if command == "add":
    add_note()
elif command == "list":
    list_notes()
elif command == "delete":
    delete_note()
else:
    print("Unknown command. Use: add, list, delete")
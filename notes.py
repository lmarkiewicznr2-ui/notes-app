import sys
usage = "Usage:\n  python notes.py add <note>\n  python notes.py list"
if len(sys.argv) < 2:
    print(usage)
    sys.exit()

command = sys.argv[1]


if command == "add":
    if len(sys.argv) < 3:
        print(usage)
        sys.exit()
    note = sys.argv[2]
    try:
        with open("notes.txt", "r") as file:
            lines = file.read().splitlines()
    except FileNotFoundError:
        lines = []
    lines.append(note)
    with open ("notes.txt", "w") as file:
        for i, n in enumerate(lines, start=1):
            file.write(f"{i}. {n}\n")
elif command == "list":
    
    try:
        with open("notes.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No notes yet!")
elif command == "delete":
    if len(sys.argv) < 3:
        print("Usage: python notes.py delete <number>")
        sys.exit()

    try:
        with open("notes.txt", "r") as file:
            index = int(sys.argv[2])
            lines = file.read().splitlines()
            if index < 1 or index > len(lines): 
                print("Invalid note number")
                sys.exit()
            lines.pop(index - 1)
            with open("notes.txt","w") as file:
                for i, n in enumerate(lines, start=1):
                    file.write(f"{i}. {n}\n")
    except FileNotFoundError:
        print("No notes yet!")
        sys.exit()


else:
    print("Unknown command. Use: add or list")
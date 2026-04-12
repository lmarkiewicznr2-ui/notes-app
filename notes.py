import sys


command = sys.argv[1]


if command == "add":
    print("adding note")
    note = sys.argv[2]
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
elif command == "list":
    print("listing notes")
    with open("notes.txt", "r") as file:
        notes = file.read()
        print(notes)
else:
    print("unknown command")

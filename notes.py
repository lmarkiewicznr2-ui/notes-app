import sys


command = sys.argv[1]


if command == "add":
    print("adding note")
elif command == "list":
    print("listing notes")
else:
    print("unknown command")
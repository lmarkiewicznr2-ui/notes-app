import sys
from commands import add, list_notes, delete

ALIASES = {
    "add": "add",
    "ad": "add",
    "a": "add",
    "addd": "add",

    "list": "list",
    "ls": "list",
    "l": "list",

    "delete": "delete",
    "del": "delete",
    "d": "delete",
}

def help_menu():
    print("""
note <command>

Commands:
  add / a / ad / addd   <text>
  list / l / ls
  delete / del / d      <number>
""")

def main():
    if len(sys.argv) < 2:
        help_menu()
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    cmd = ALIASES.get(cmd, cmd)

    if cmd == "add":
        add(args)
    elif cmd == "list":
        list_notes()
    elif cmd == "delete":
        delete(args)
    elif cmd == "help":
        help_menu()
    elif cmd in ["lists", "lslists", "lsl", "ll"]:
        list_lists()
    elif cmd in ["remove-list", "rmlist", "rml", "rl"]:
        remove_list(args)
    elif cmd in ["find", "search", "f"]:
        search(args)
    else:
        print("Unknown command. Use: note help")

if __name__ == "__main__":
    main()
import sys


def main():
    while True:
        sys.stdout.write("$ ")
        # User Input
        command = input()
        execute_command(command)


def execute_command(command):
    if command == "exit":
        sys.exit(0)
    elif command.startswith("echo "):
        print(f"{command[5:]}")
    elif command.startswith("type "):
        if command[5:] in ["echo", "exit", "type"]:
            print(f"{command[5:]} is a shell builtin")
        else:
            print(f"{command[5:]}: not found")
    else:
        sys.stdout.write(f"{command}: command not found")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()

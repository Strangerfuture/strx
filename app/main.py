import sys


def main():
    while True:
        sys.stdout.write("$ ")
        # User Input
        command = input()
        execute_command(command)


def execute_command(command):
    if command == "exit":
        exit()
    elif command.startwith("echo "):
        print(f"{command[5:]}")
    else:
        sys.stdout.write(f"{command}: command not found")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()

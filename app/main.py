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
    if command.split(" ")[0] == "echo":
        print(f"{" ".join(command.split(" ")[1:])}")
    else:
        sys.stdout.write(f"{command}: command not found")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()

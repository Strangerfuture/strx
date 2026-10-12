from os import path
import sys
import shutil



def main():
    while True:
        sys.stdout.write("$ ")
        # User Input
        command = input()
        execute_command(command)


def is_builtin(command):
    return command in {"echo", "exit", "type"}




def execute_command(command):

    parts = command.split()
    cmd = parts[0]
    args = parts[1:] if len(parts) > 1 else ""

    if  is_builtin(cmd):
        if cmd == "exit":
            sys.exit(0)
        elif cmd == "echo":
            print(f"{" ".join(args)}")
        elif cmd == "type":
            if is_builtin(args[0]):
                print(f"{args[0]} is a shell builtin")
            elif path := shutil.which(args[0]):
                print(f"{cmd} is {path}")
            else:
                print(f"{cmd}: not found")
    else:
        sys.stdout.write(f"{cmd}: command not found")
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()

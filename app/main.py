import sys
import os
import subprocess


#from typing import Optional


def locate_exec(command):
    PATH = os.environ.get("PATH")
    directories = PATH.split(":")

    cmd_path = None    
    for directory in directories:
        if os.path.isfile(f'{directory}/{command}'):
            cmd_path = f'{directory}/{command}'
    
    return cmd_path


def echo_handle(args):
    print(" ".join(args))


def exit_handle(args):
    sys.exit(int(args[0]) if args else 0)


def type_handle(args):
    if args[0] in built_ins:
        print(f"{args[0]} is a shell builtin")
    elif executable := locate_exec(args[0]):
        print(f"{args[0]} is {executable}") 
    else:
        print(f"{args[0]} not found")


built_ins = {"exit": exit_handle,
             "echo": echo_handle,
             "type": type_handle,}


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command, *args = input().split()

        if command in built_ins:
            built_ins[command](args)
            continue
        elif executable := locate_exec(command):
            subprocess.run([executable, *args])
        else:
            print(f"{command}: command not found")
        
        sys.stdout.flush()

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""This is a program named console.py that contains the entry point
of the command interpreter:."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""
    prompt = "(hbnb) "

    def emptyline(self):
        """When there is an empty line + ENTER shouldn’t execute anything."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

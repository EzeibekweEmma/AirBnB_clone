#!/usr/bin/python3
"""Module for boilerplate a console"""
import cmd
from actions import Actions


class HBNBCommand(cmd.Cmd):
    """Creates a console HBNB"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

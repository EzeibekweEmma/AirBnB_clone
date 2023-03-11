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

    def emptyline(self):
        """Handle empty line when is passed as an argument"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, and prints the id"""
        arg = HBNBCommand.parse_argument(arg)
        Actions.create(arg)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        arg = HBNBCommand.parse_argument(arg)
        Actions.show(arg)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg = HBNBCommand.parse_argument(arg)
        Actions.destroy(arg)

    def do_all(self, arg):
        """Prints string representation of all instances based"""
        arg = HBNBCommand.parse_argument(arg)
        Actions.all(arg)

    def do_update(self, arg):
        """Update an instance"""
        arg = HBNBCommand.parse_argument(arg)
        Actions.update(arg)

    def default(ignore, line):
        """Handle default point cmd"""
        arg = HBNBCommand.parse_argument(line)
        Actions.default(arg)

    @staticmethod
    def parse_argument(arg):
        """Convert any argument string into argument tuple"""
        return tuple(map(str, arg.split()))


if __name__ == '__main__':
    HBNBCommand().cmdloop()

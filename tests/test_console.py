#!/usr/bin/python3
"""Module for TestHBNBCommand class."""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):

    """Tests HBNBCommand console."""

    attribute_values = {
        str: "foobar108",
        int: 1008,
        float: 1.08
    }

    reset_values = {
        str: "",
        int: 0,
        float: 0.0
    }

    test_random_attributes = {
        "strfoo": "barfoo",
        "intfoo": 248,
        "floatfoo": 9.8
    }

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update
    """
            self.assertEqual(s, f.getvalue())

    def test_help_EOF(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        s = 'Handles End Of File character.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Exits the program.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates an instance.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        s = 'Prints the string representation of an instance.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = 'Deletes an instance based on the class name and id.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = 'Prints all string representation of all instances.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_count(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        s = 'Counts the instances of a class.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s = 'Updates an instance by adding or updating attribute.\n        \n'
        self.assertEqual(s, f.getvalue())

    def test_do_quit(self):
        """Tests quit commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_EOF(self):
        """Tests EOF commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 1)
        self.assertEqual("\n", msg)

    def test_emptyline(self):
        """Tests emptyline functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        s = ""
        self.assertEqual(s, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        s = ""
        self.assertEqual(s, f.getvalue())

    def test_do_create(self):
        """Tests create for all classes."""
        for classname in self.classes():
            self.help_test_do_create(classname)

    def help_test_do_create(self, classname):
        """Helper method to test the create commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(classname, uid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        self.assertTrue(uid in f.getvalue())

    def test_do_create_error(self):
        """Tests create command with errors."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create garbage")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def test_do_show(self):
        """Tests show for all classes."""
        for classname in self.classes():
            self.help_test_do_show(classname)
            self.help_test_show_advanced(classname)

    def help_test_do_show(self, classname):
        """Helps test the show command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(uid in s)

        def test_do_show_error(self):
            """Tests show command with errors."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** class name missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show garbage")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** class doesn't exist **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show BaseModel")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** instance id missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                 HBNBCommand().onecmd("show BaseModel 6524359")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** no instance found **")

        def help_test_show_advanced(self, classname):
            """Helps test .show() command."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
            s = f.getvalue()
            self.assertTrue(uid in s)

        def test_do_show_error_advanced(self):
            """Tests show() command with errors."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(".show()")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** class name missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("garbage.show()")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** class doesn't exist **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("BaseModel.show()")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** instance id missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd('BaseModel.show("6524359")')
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** no instance found **")

        def test_do_destroy(self):
            """Tests destroy for all classes."""
            for classname in self.classes():
                self.help_test_do_destroy(classname)
                self.help_test_destroy_advanced(classname)

        def help_test_do_destroy(self, classname):
            """Helps test the destroy command."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {} {}".format(classname, uid))
            s = f.getvalue()[:-1]
            self.assertTrue(len(s) == 0)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(".all()")
            self.assertFalse(uid in f.getvalue())

        def test_do_destroy_error(self):
            """Tests destroy command with errors."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** class name missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy garbage")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** class doesn't exist **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy BaseModel")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** instance id missing **")

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy BaseModel 6524359")
            msg = f.getvalue()[:-1]
            self.assertEqual(msg, "** no instance found **")

        def help_test_destroy_advanced(self, classname):
            """Helps test the destroy command."""
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(classname))
            uid = f.getvalue()[:-1]
            self.assertTrue(len(uid) > 0)

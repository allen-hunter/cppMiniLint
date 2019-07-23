import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.code_tests.multiple_classes import MultipleClasses
from minilint.parser_message import *


class TestMultipleClasses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.multiple_classes = MultipleClasses()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):  # from test, just making sure that the supers are in place
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.multiple_classes.receive_message(new_file)
        self.assertEqual(self.multiple_classes._line_number, 0)
        self.assertEqual(self.multiple_classes._filename, "foo.h")
        self.multiple_classes.receive_message(new_line)
        self.assertEqual(self.multiple_classes._line_number, 1)
        second_file = NewFile("bar.h")
        self.multiple_classes.receive_message(second_file)
        self.assertEqual(self.multiple_classes._filename, "bar.h")

    def test_process_line(self):
        new_file = NewFile("foo.h")
        new_class = Class("foo", [], [])
        self.multiple_classes.receive_message(new_file)
        self.multiple_classes.receive_message(new_class)
        self.multiple_classes.receive_message(new_class)
        result = self.multiple_classes._process_end_of_file()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
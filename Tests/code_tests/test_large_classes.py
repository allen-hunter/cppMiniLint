import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.code_tests.large_classes import LargeClasses
from minilint.parser_message import *


class TestLargeClasses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.large_classes = LargeClasses()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):  # from test, just making sure that the supers are in place
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.large_classes.receive_message(new_file)
        self.assertEqual(self.large_classes._line_number, 0)
        self.assertEqual(self.large_classes._filename, "foo.h")
        self.large_classes.receive_message(new_line)
        self.assertEqual(self.large_classes._line_number, 1)
        second_file = NewFile("bar.h")
        self.large_classes.receive_message(second_file)
        self.assertEqual(self.large_classes._filename, "bar.h")

    def test_process_line(self):
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "Class foo{}")
        self.large_classes.receive_message(new_file)
        self.large_classes.receive_message(new_line)



if __name__ == '__main__':
    unittest.main()
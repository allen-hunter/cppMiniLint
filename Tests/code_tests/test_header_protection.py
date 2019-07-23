import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.code_tests.header_protection import HeaderProtection
from minilint.parser_message import *


class TestHeaderProtection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.header_protection = HeaderProtection()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):  # from test, just making sure that the supers are in place
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.header_protection.receive_message(new_file)
        self.assertEqual(self.header_protection._line_number, 0)
        self.assertEqual(self.header_protection._filename, "foo.h")
        self.header_protection.receive_message(new_line)
        self.assertEqual(self.header_protection._line_number, 1)
        second_file = NewFile("bar.h")
        self.header_protection.receive_message(second_file)
        self.assertEqual(self.header_protection._filename, "bar.h")

    def test_process_line(self):
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "#pragma once")
        end_of_file = EndOfFile("foo.h")
        self.header_protection.receive_message(new_file)
        self.header_protection.receive_message(new_line)
        self.assertEqual(self.header_protection._header_protected, True)
        self.header_protection.receive_message(end_of_file)
        new_line = LineFromFile(True, "#ifndef file_H\n#define file_H")
        self.header_protection.receive_message(new_file)
        self.header_protection.receive_message(new_line)
        self.assertEqual(self.header_protection._header_protected, True)

if __name__ == '__main__':
    unittest.main()
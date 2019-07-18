import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.code_tests.no_copyright import NoCopyright
from minilint.parser_message import *


class TestNoCopyright(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.no_copyright = NoCopyright()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):  # from test, just making sure that the supers are in place
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.no_copyright.receive_message(new_file)
        self.assertEqual(self.no_copyright._line_number, 0)
        self.assertEqual(self.no_copyright._filename, "foo.h")
        self.no_copyright.receive_message(new_line)
        self.assertEqual(self.no_copyright._line_number, 1)
        second_file = NewFile("bar.h")
        self.no_copyright.receive_message(second_file)
        self.assertEqual(self.no_copyright._filename, "bar.h")

    def test_process_eof(self):
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        end_of_file = EndOfFile("foo.h")
        self.no_copyright.receive_message(new_file)
        self.no_copyright.receive_message(new_line)
        self.no_copyright.receive_message(end_of_file)
        message = self.no_copyright.report.get_message("foo.h", 1)
        self.assertEqual(message, ['no copyright message in file'])


if __name__ == '__main__':
    unittest.main()
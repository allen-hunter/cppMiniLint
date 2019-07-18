import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.code_tests.too_long import TooLong
from minilint.parser_message import *


class TestFileTooLong(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.too_long = TooLong()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):  # from test, just making sure that the supers are in place
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.too_long.receive_message(new_file)
        self.assertEqual(self.too_long._line_number, 0)
        self.assertEqual(self.too_long._filename, "foo.h")
        self.too_long.receive_message(new_line)
        self.assertEqual(self.too_long._line_number, 1)
        second_file = NewFile("bar.h")
        self.too_long.receive_message(second_file)
        self.assertEqual(self.too_long._filename, "bar.h")

    def test_process_line(self):
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        end_of_file = EndOfFile("foo.h")
        self.too_long.receive_message(new_file)
        for i in range(310):
            self.too_long.receive_message(new_line)
        self.too_long.receive_message(end_of_file)
        message = self.too_long.report.get_message("foo.h", 310)
        self.assertEqual(message, ['file has 10 too many lines'])

        new_file = NewFile("foo.cpp")
        end_of_file = EndOfFile("foo.cpp")
        self.too_long.receive_message(new_file)
        new_line = LineFromFile(False, "this is a line from a cpp file")
        for i in range(1010):
            self.too_long.receive_message(new_line)
        self.too_long.receive_message(end_of_file)
        message = self.too_long.report.get_message("foo.cpp", 1010)
        self.assertEqual(message, ['file has 10 too many lines'])

    def test_set_max_file_sizes(self):
        self.too_long.set_max_file_sizes(5, 5)
        self.assertEqual(self.too_long._max_header_size, 5)
        self.assertEqual(self.too_long._max_cpp_size, 5)

if __name__ == '__main__':
    unittest.main()
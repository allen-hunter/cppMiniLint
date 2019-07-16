import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.test import Test
from minilint.parser_message import *


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.test = Test()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.test.receive_message(new_file)
        self.assertEqual(self.test._line_number, 0)
        self.assertEqual(self.test._filename, "foo.h")
        self.test.receive_message(new_line)
        self.assertEqual(self.test._line_number, 1)
        second_file = NewFile("bar.h")
        self.test.receive_message(second_file)
        self.assertEqual(self.test._filename, "bar.h")


if __name__ == '__main__':
    unittest.main()
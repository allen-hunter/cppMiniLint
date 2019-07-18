import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0], 'cppMiniLint', 'sub', 'dir'))
from minilint.code_tests.if_zero import IfZero
from minilint.parser_message import *


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.ifzero = IfZero()

    def tearDown(self):  # runs after each test
        pass

    def test_receive_message(self):  # from test, just making sure that the supers are in place
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.ifzero.receive_message(new_file)
        self.assertEqual(self.ifzero._line_number, 0)
        self.assertEqual(self.ifzero._filename, "foo.h")
        self.ifzero.receive_message(new_line)
        self.assertEqual(self.ifzero._line_number, 1)
        second_file = NewFile("bar.h")
        self.ifzero.receive_message(second_file)
        self.assertEqual(self.ifzero._filename, "bar.h")

    def test_receive_message_if_zero(self):  # ifzero specific
        new_file = NewFile("foo.h")
        new_line = LineFromFile(True, "this is a line from a header file")
        self.ifzero.receive_message(new_file)
        self.ifzero.receive_message(new_line)
        self.assertEqual(len(self.ifzero.report.issues), 0)
        new_line = LineFromFile(True, "#if 0")
        self.ifzero.receive_message(new_line)
        self.assertEqual(len(self.ifzero.report.issues['foo.h']), 1)
        new_line = LineFromFile(True, "#if(0)")
        self.ifzero.receive_message(new_line)
        self.assertEqual(len(self.ifzero.report.issues['foo.h']), 2)


if __name__ == '__main__':
    unittest.main()
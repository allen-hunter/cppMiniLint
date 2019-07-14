import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0],'cppMiniLint', 'sub', 'dir'))
from minilint.parser import Parser
from minilint.code_tests.ifzero import IfZero


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.parser = Parser()
        # self.parser.test_suite.tests_to_run.append(IfZero())

    def tearDown(self):  # runs after each test
        pass

    def test_parse_all_files(self):
        self.parser.headers = ['testcpp\Date.h']
        self.parser.cpp_files = ['testcpp\Date.cpp']
        with patch('minilint.parser.Parser.announce_new_filename') as mocked_announce_new_filename:
            self.parser.parse_all_files()
            mocked_announce_new_filename.assert_any_call('testcpp\Date.h')
            mocked_announce_new_filename.assert_any_call('testcpp\Date.cpp')

    def test_read_lines(self):
        self.parser.cpp_files = ['testcpp\Date.cpp']
        with patch('minilint.parser.Parser.announce_new_cpp_line') as mocked_announce_new_cpp_line:
            self.parser.parse_all_files()
            self.assertEqual(mocked_announce_new_cpp_line.call_count, 35)
        self.parser.cpp_files = []
        self.parser.headers = ['testcpp\Date.h']
        with patch('minilint.parser.Parser.announce_new_header_line') as mocked_announce_new_header_line:
            self.parser.parse_all_files()
            self.assertEqual(mocked_announce_new_header_line.call_count, 21)


if __name__ == '__main__':
    unittest.main()
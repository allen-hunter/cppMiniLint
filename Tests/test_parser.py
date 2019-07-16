import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0],'cppMiniLint', 'sub', 'dir'))
from minilint.parser import Parser
from minilint.filelist import FileList
from minilint.parser_message import *


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.file_list = FileList()
        self.parser = Parser(self.file_list)

    def tearDown(self):  # runs after each test
        pass

    def test_parse_all_files(self):
        self.file_list.add_file('testcpp\Date.h')
        self.file_list.add_file('testcpp\Date.cpp')
        with patch('minilint.parser.Parser._parse_file') as mocked_parse_file:
            self.parser.parse_all_files()
            mocked_parse_file.assert_any_call('testcpp\Date.h', True)
            mocked_parse_file.assert_any_call('testcpp\Date.cpp', False)


if __name__ == '__main__':
    unittest.main()
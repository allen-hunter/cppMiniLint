import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0],'cppMiniLint', 'sub', 'dir'))
from minilint.file_list import File_List


class TestFileList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.file_list = File_List()

    def tearDown(self):  # runs after each test
        pass

    def test_load_directory(self):
        self.file_list.load_directory('testcpp')
        self.assertTrue('testcpp\\Date.h' in self.file_list.headers)
        self.assertTrue('testcpp\\Date.cpp' in self.file_list.cpp_files)


if __name__ == '__main__':
    unittest.main()
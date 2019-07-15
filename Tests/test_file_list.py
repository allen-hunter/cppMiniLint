import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0],'cppMiniLint', 'sub', 'dir'))
from minilint.filelist import FileList


class TestFileList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.file_list = FileList()

    def tearDown(self):  # runs after each test
        pass

    def test_load_directory(self):
        self.file_list.load_directory('testcpp')
        # finding files
        self.assertEqual(self.file_list.headers.count('testcpp\\Date.h'), 1)
        self.assertEqual(self.file_list.headers.count('testcpp\\A2DD.hpp'), 1)
        self.assertEqual(self.file_list.cpp_files.count('testcpp\\Date.cpp'), 1)
        self.assertEqual(self.file_list.cpp_files.count('testcpp\\A2DD.CPP'), 1)
        self.assertEqual(self.file_list.cpp_files.count('testcpp\\cube.c'), 1)
        # appending
        original_size = len(self.file_list.headers)
        self.file_list.load_directory('testcpp')
        self.assertEqual(original_size*2, len(self.file_list.headers))
        self.assertEqual(self.file_list.headers.count('testcpp\\Date.h'), 2)

    def test_add_file(self):
        # ignoring all but valid extensions
        self.file_list.add_file('python_is_ignored.py')
        self.assertEqual(self.file_list.headers.count('python_is_ignored.py'), 0)
        self.assertEqual(self.file_list.cpp_files.count('python_is_ignored.py'), 0)
        # extensions going to the right places
        self.file_list.add_file('testcpp\\Date.h')
        self.file_list.add_file('testcpp\\A2DD.hpp')
        self.file_list.add_file('testcpp\\Date.cpp')
        self.file_list.add_file('testcpp\\A2DD.CPP')
        self.file_list.add_file('testcpp\\cube.c')
        self.assertEqual(self.file_list.headers.count('testcpp\\Date.h'), 1)
        self.assertEqual(self.file_list.headers.count('testcpp\\A2DD.hpp'), 1)
        self.assertEqual(self.file_list.cpp_files.count('testcpp\\Date.cpp'), 1)
        self.assertEqual(self.file_list.cpp_files.count('testcpp\\A2DD.CPP'), 1)
        self.assertEqual(self.file_list.cpp_files.count('testcpp\\cube.c'), 1)
        # appending
        self.file_list.add_file('testcpp\\Date.h')
        self.assertEqual(self.file_list.headers.count('testcpp\\Date.h'), 2)

    def test_clear(self):
        self.file_list.load_directory('testcpp')
        self.assertTrue(len(self.file_list.headers) > 0)
        self.file_list.clear()
        self.assertEqual(len(self.file_list.headers), 0)


if __name__ == '__main__':
    unittest.main()
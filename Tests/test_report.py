import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0],'cppMiniLint', 'sub', 'dir'))
from minilint.report import Report


class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # runs at the beginning
        pass

    @classmethod
    def tearDownClass(cls):  # runs at the end
        pass

    def setUp(self):  # runs before each test
        self.report = Report()
        pass

    def tearDown(self):  # runs after each test
        pass

    def test_add_message(self):
        self.report.add_message('file_name', 'line_number', 'message_text')
        self.assertTrue('file_name' in self.report.issues)
        self.assertTrue('line_number' in self.report.issues['file_name'])
        self.assertEqual(self.report.issues['file_name']['line_number'], ['message_text'])
        #duplicates
        self.report.add_message('file_name', 'line_number', 'new message text')
        self.assertTrue('message_text' in self.report.issues['file_name']['line_number'])
        self.assertTrue('new message text' in self.report.issues['file_name']['line_number'])

if __name__ == '__main__':
    unittest.main()
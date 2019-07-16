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

    def test_get_messages(self):
        line_and_messages = self.report.get_messages('file_name')
        self.assertEqual(len(line_and_messages), 0)
        self.report.add_message('file_name', 'line_number', 'message 1')
        self.report.add_message('file_name', 'line_number', 'message 2')
        self.assertEqual(len(line_and_messages), 1)
        self.assertEqual(len(line_and_messages['line_number']), 2)

    def test_get_message(self):
        messages = self.report.get_message('file_name', 'line_number')
        self.assertEqual(len(messages), 0)
        self.report.add_message('file_name', 'line_number', 'message 1')
        self.report.add_message('file_name', 'line_number', 'message 2')
        self.assertEqual(len(messages), 2)  # interesting that we can count this even though
                                            # we asked for it when the dict was empty

if __name__ == '__main__':
    unittest.main()
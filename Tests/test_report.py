import sys
import os
import unittest
from unittest.mock import patch
sys.path.append(os.path.join(sys.path[0],'cppMiniLint', 'sub', 'dir'))
from minilint.report import Report


class TestReport(unittest.TestCase):

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

    def test_iadd(self):
        other_report = Report()
        self.report.add_message('file_name.h', '2', 'message_text_1')
        self.report.finish_file('file_name.h', 'test 1')
        other_report.add_message('file_name.h', '2', 'message_text_2')
        other_report.finish_file('file_name.h', 'test 2')
        self.report += other_report
        self.assertEqual(self.report.issues['file_name.h']['2'], ['message_text_1', 'message_text_2'])
        self.assertEqual(self.report.scores['test 2']['file_name.h'], 1)

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
    def test_clear(self):
        messages = self.report.get_message('file_name', 'line_number')
        self.assertEqual(len(messages), 0)
        self.report.add_message('file_name', 'line_number', 'message 1')
        self.report.add_message('file_name', 'line_number', 'message 2')
        self.assertEqual(len(messages), 2)
        self.report.clear('file_name')
        messages = self.report.get_message('file_name', 'line_number')
        self.assertEqual(len(messages), 0)

    def test_produce_report(self):
        self.report.add_message('file_name', 'line_number', 'message_text')
        report_text = self.report.produce_report()
        self.assertEqual(report_text, 'file_name\n\tline: line_number\n\t\tmessage_text\n')

    def test_remove_path(self):
        file_sans_path = self.report._remove_path('foo.h')
        self.assertEqual(file_sans_path, 'foo.h')
        file_sans_path = self.report._remove_path('baz\\bar\\foo.h')
        self.assertEqual(file_sans_path, 'foo.h')

    def test_finish_file(self):
        self.report.add_message('\\foo\\bar\\file_name.h', 'line_number', 'message 1')
        self.report.add_message('\\foo\\bar\\file_name.h', 'line_number', 'message 2')
        self.report.finish_file('\\foo\\bar\\file_name.h', 'test')
        self.assertEqual(self.report.scores['test']['file_name.h'], 2)

    def test_sort_by_reference_and_weight(self):
        self.report.add_message('\\foo\\bar\\file_name.h', 'line_number', 'message 1')
        self.report.add_message('\\foo\\bar\\file_name.h', 'line_number', 'message 2')
        self.report.finish_file('\\foo\\bar\\file_name.h', 'test')
        self.report.add_message('\\foo\\bar\\file_name.cpp', 'line_number', 'message 1')
        self.report.add_message('\\foo\\bar\\file_name.cpp', 'line_number', 'message 2')
        self.report.add_message('\\foo\\bar\\file_name.cpp', 'line_number', 'message 3')
        self.report.finish_file('\\foo\\bar\\file_name.cpp', 'test')
        self.assertEqual(self.report.sort_by_reference_and_weight('file_name.cpp'), 3)
        self.report.add_reference('file_name.cpp')
        self.assertEqual(self.report.sort_by_reference_and_weight('file_name.cpp'), 6)
        file_list = ['\\foo\\bar\\file_name.h', '\\foo\\bar\\file_name.cpp']
        sorted_list = sorted(file_list, key=lambda file: self.report.sort_by_reference_and_weight(file), reverse=True)
        self.assertEqual(sorted_list, ['\\foo\\bar\\file_name.cpp', '\\foo\\bar\\file_name.h'])


if __name__ == '__main__':
    unittest.main()
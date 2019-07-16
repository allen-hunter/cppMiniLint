from minilint.testsuite import TestSuite
from minilint.parser_message import *
# The Parser Class is the subject in an observer pattern.
# It is responsible for parsing through header and implementation files
# and notifying tests of c++ entities for evaluation


class Parser(object):

    def __init__(self, file_list_to_parse):
        # public
        self._file_list = file_list_to_parse
        self.test_suite = TestSuite()

    def parse_all_files(self):
        for header in self._file_list.headers:
            self._parse_file(header, True)
        for cpp in self._file_list.cpp_files:
            self._parse_file(cpp, False)

    def _parse_file(self, file, file_is_header):
        self.test_suite.receive_message(NewFile(file))
        file = open(file, "r")
        self._read_lines(file, file_is_header)
        file.close()

    def _read_lines(self, file, file_is_header):
        for line in file:
            self.test_suite.receive_message(LineFromFile(file_is_header,line))

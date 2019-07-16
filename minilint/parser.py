from minilint.testsuite import TestSuite
from minilint.parser_message import *
# The Parser Class is the subject in an observer pattern.
# It is responsible for parsing through header and implementation files
# and notifying tests of c++ entities for evaluation

# todo: think of using an observer pattern to loosen the coupling to testsuite


class Parser(object):

    def __init__(self, file_list_to_parse):
        # public
        self._file_list = file_list_to_parse
        self.test_suite = TestSuite()

    def parse_all_files(self):
        for header in self._file_list.headers:
            self.__parse_file(header, True)
        for cpp in self._file_list.cpp_files:
            self.__parse_file(cpp, False)

    def __parse_file(self, file, file_is_header):
        self.announce_new_filename(file)
        self.test_suite.receive_message(NewFile(file))
        file = open(file, "r")
        self.__read_lines(file, file_is_header)
        file.close()

    def __read_lines(self, file, file_is_header):
        for line in file:
            if file_is_header:
                self.announce_new_header_line(line)
            else:
                self.announce_new_cpp_line(line)

    # notifying functions for observers
    # todo: consider using polymorphism to allow a single function to handle all messages
    def announce_new_filename(self, filename):
        self.test_suite.receive_new_filename(filename)

    def announce_new_header_line(self, line):
        self.test_suite.receive_new_header_line(line)

    def announce_new_cpp_line(self, line):
        self.test_suite.receive_new_cpp_line(line)

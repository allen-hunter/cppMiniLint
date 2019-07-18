import re
from ..test import *
from ..parser_message import *
# a test which looks for files that are too long


class TooLong(Test):
    def __init__(self):
        super(TooLong, self).__init__()
        self.__regex = re.compile('.*\.hp*', re.IGNORECASE)
        self._max_header_size = 300  # todo: pull from config
        self._max_cpp_size = 1000  # todo: pull from config
        self._max_size = 0

    def set_max_file_sizes(self, header_length, cpp_length):
        self._max_header_size = header_length
        self._max_cpp_size = cpp_length

    # for the observer pattern
    def receive_message(self, parser_message):
        super(TooLong, self).receive_message(parser_message)
        if isinstance(parser_message, NewFile):
            self.__process_new_file(parser_message.file_name)
        elif isinstance(parser_message, LineFromFile):
            self.__process_line()

    # method for the test
    def __process_line(self):
        if self._line_number > self._max_size:
            error_message = "file has " + str(self._line_number - self._max_size) + " too many lines"
            self.report.clear(self._filename)  # get rid of previous complaints by this test
            self.report.add_message(self._filename, self._line_number, error_message)

    def __process_new_file(self, file_name):
        if self.__regex.search(file_name):
            self._max_size = self._max_header_size
        else:
            self._max_size = self._max_cpp_size
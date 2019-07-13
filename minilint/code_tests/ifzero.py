from ..test import *
import re
# a test which detects #if 0 header directives (used to comment out code blocks)

class IfZero(Test):
    def __init__(self):
        self.__regex = re.compile('#if\\s*\(*0', re.IGNORECASE)
        super(IfZero, self).__init__()

    # for the observer pattern
    def receive_new_header_line(self, line):
        super(IfZero, self).receive_new_header_line(line)
        self.__process_line(line)

    def receive_new_cpp_line(self, line):
        super(IfZero, self).receive_new_cpp_line(line)
        self.__process_line(line)

    def receive_new_filename(self, name):
        super(IfZero, self).receive_new_filename(name)

    # methods for the test
    def __process_line(self, line):
        if self.string_contains_if_zero(line):
            self.report.add_message(self._filename, self._line_number, "if zero preprocessor instruction found")

    def string_contains_if_zero(self, line):
        if self.__regex.search(line):
            return True
        return False

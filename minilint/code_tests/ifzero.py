from ..test import *
import re
# a test which detects #if 0 header directives (used to comment out code blocks)

class IfZero(Test):
    def __init__(self):
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
    def produce_report(self):
        # todo: implement report
        pass

    def __process_line(self, line):
        if IfZero.string_contains_if_zero(line):
            report_message = self._filename + " line " + str(self._line_number) + ": if zero"
            super(IfZero, self).add_line_to_report(report_message)

    def string_contains_if_zero(line):
        regex = re.compile('#if\\s*\(*0', re.IGNORECASE)
        if regex.search(line):
            return True
        return False

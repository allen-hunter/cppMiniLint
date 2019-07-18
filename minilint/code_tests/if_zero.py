from ..test import *
import re
# a test which detects #if 0 header directives (used to comment out code blocks)

class IfZero(Test):
    def __init__(self):
        self.__regex = re.compile('#if\\s*\(*0', re.IGNORECASE)
        super(IfZero, self).__init__()

    # for the observer pattern
    def receive_message(self, parser_message):
        super(IfZero, self).receive_message(parser_message)
        if isinstance(parser_message, LineFromFile):
            self.__process_line(parser_message.line_text)

    # methods for the test
    def __process_line(self, line):
        if self.string_contains_if_zero(line):
            self.report.add_message(self._filename, self._line_number, "if zero preprocessor instruction found")

    def string_contains_if_zero(self, line):
        if self.__regex.search(line):
            return True
        return False

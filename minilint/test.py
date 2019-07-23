from minilint.report import Report
from minilint.parser_message import *

# abstract base class (interface) for tests.  Follows the observer pattern with the intention
# of using parser as the subject.  Every code test should inherit from this class


class Test:
    def __init__(self):
        self._line_number = 0
        self._filename = ""
        self.report = Report()

    def produce_report(self):
        pass

# for the observer pattern
    #general message
    def receive_message(self, parser_message):
        if isinstance(parser_message, NewFile):
            self._filename = parser_message.file_name
            self._line_number = 0
        elif isinstance(parser_message, LineFromFile):
            self._line_number += 1
        elif isinstance(parser_message, EndOfFile):
            self.report.finish_file(parser_message.file_name, self.__class__.__name__)

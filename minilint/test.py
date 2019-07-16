from minilint.report import Report
from minilint.parser_message import *

# abstract base class (interface) for tests.  Follows the observer pattern with the intention
# of using parser as the subject.  Every code test should inherit from this class


class Test:
    def __init__(self):
        self._line_number = 0
        self._filename = ""
        self.report = Report()  # todo: we should be handed the report so that it can be polymorphic

    def produce_report(self):
        pass

# for the observer pattern
    #general message
    def receive_message(self, parser_message):
        print(isinstance(parser_message, NewFile))
        print(parser_message.file_name)

    def receive_new_header_line(self, line):
        self._line_number += 1

    def receive_new_cpp_line(self, line):
        self._line_number += 1

    def receive_new_filename(self, name):
        self._filename = name
        self._line_number = 0

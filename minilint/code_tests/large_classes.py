from ..test import *
from ..parser_message import *
import re
# A test which verifies that header files are protected either with preprocessor directives or pragma once


class LargeClasses(Test):
    def __init__(self):
        super(LargeClasses, self).__init__()
        self._allowable_lines_for_class = 300  # todo:take from config
        self._initialize()

    # for the observer pattern
    def receive_message(self, parser_message):
        super(LargeClasses, self).receive_message(parser_message)
        if isinstance(parser_message, LineFromFile):
            self._process_line_from_file(parser_message)
        elif isinstance(parser_message, EndOfFile):
            self._process_end_of_file()

    def _process_line_from_file(self, parser_message):
        if not parser_message.is_header:
            return
        for i in range(len(parser_message.line_text)):
            candidate_string = parser_message.line_text[i:len("class")+i]
            if candidate_string.lower() == "class":
                self._record_new_class()
            elif parser_message.line_text[i] == "{":
                self._number_nested += 1
            elif parser_message.line_text[i] == "}":
                self._denest()

    def _record_new_class(self):
        self._classes_by_nest_depth[self._number_nested] = self._line_number

    def _denest(self):
        self._number_nested -= 1
        if self._number_nested in self._classes_by_nest_depth:
            total_lines = self._line_number - self._classes_by_nest_depth[self._number_nested]
            self._classes_by_nest_depth.pop(self._number_nested)
            if total_lines > self._allowable_lines_for_class:
                self.report.add_message(self._filename, self._line_number, "long class detected")

    def _process_end_of_file(self):
        self._initialize()

    def _initialize(self):
        self._number_nested = 0
        self._classes_by_nest_depth = {} # dictionary: nest_depth(int) : starting line (int)

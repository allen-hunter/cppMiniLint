from ..test import *
from ..parser_message import *
import re
# A test which verifies that header files are protected either with preprocessor directives or pragma once


class MultipleClasses(Test):
    def __init__(self):
        super(MultipleClasses, self).__init__()
        self._class_count = 0

    # for the observer pattern
    def receive_message(self, parser_message):
        super(MultipleClasses, self).receive_message(parser_message)
        if isinstance(parser_message, Class):
            self._class_count += 1
        elif isinstance(parser_message, EndOfFile):
            self._process_end_of_file()

    def _process_end_of_file(self):
        too_many = False
        if self._class_count > 1:
            errorstring = "Too many classes in file: " + str(self._class_count) + " classes in header"
            self.report.add_message(self._filename, 1, errorstring)
            too_many = True
        self._class_count = 0
        return too_many

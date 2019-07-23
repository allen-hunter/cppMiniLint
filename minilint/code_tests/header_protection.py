from ..test import *
from ..parser_message import *
import re
# A test which verifies that header files are protected either with preprocessor directives or pragma once


class HeaderProtection(Test):
    def __init__(self):
        super(HeaderProtection, self).__init__()
        self._header_protected = False
        self._pragma_regex = re.compile("#\s*?pragma\s*?once", re.IGNORECASE)
        self._preprocessor_regex = re.compile("#\s*ifndef\s*\w*?_*?\w*?\s*\n#\s*define", re.IGNORECASE)
        self._is_header = False

    # for the observer pattern
    def receive_message(self, parser_message):
        super(HeaderProtection, self).receive_message(parser_message)
        if isinstance(parser_message, NewFile):
            self._header_protected = False
        elif isinstance(parser_message, EndOfFile):
            self._process_end_of_file()
        elif isinstance(parser_message, LineFromFile):
            self._process_line(parser_message)

    def _process_end_of_file(self):
        if not self._header_protected and self._is_header:
            self.report.add_message(self._filename, 1, "no header protection")
        else:
            self._header_protected = False

    def _process_line(self, parser_message):
        if not parser_message.is_header:
            self._is_header = False
            return False
        self._is_header = True
        if self._pragma_regex.search(parser_message.line_text)\
                or self._preprocessor_regex.search(parser_message.line_text):
            self._header_protected = True
        return self._header_protected


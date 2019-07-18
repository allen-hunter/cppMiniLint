import re
from ..test import *
from ..parser_message import *
# a test which looks for files missing a copyright block.  note that the regular expression
# is tailored to my employer's c++ coding style


class NoCopyright(Test):
    def __init__(self):
        super(NoCopyright, self).__init__()
        self.__regex = re.compile('\* Copyright ', re.IGNORECASE)
        self._found_copyright_message = False

    # for the observer pattern
    def receive_message(self, parser_message):
        super(NoCopyright, self).receive_message(parser_message)
        if isinstance(parser_message, EndOfFile):
            self.__process_end_of_file(parser_message.file_name)
        elif isinstance(parser_message, LineFromFile):
            self.__process_line(parser_message.line_text)

    # method for the test
    def __process_line(self, line):
        if self.__regex.search(line):
            self._found_copyright_message = True

    def __process_end_of_file(self, file_name):
        if self._found_copyright_message:
            self._found_copyright_message = False
            return
        else:
            self.report.add_message(file_name, 1, "no copyright message in file")

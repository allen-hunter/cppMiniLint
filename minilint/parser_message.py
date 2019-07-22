#This file contains all the message classes that the parser can issue to tests


# base class.
class ParserMessage:
    def __init__(self):
        pass


# issued when either a header or cpp line is read
class LineFromFile(ParserMessage):
    def __init__(self, is_header, line_text):
        self.is_header = is_header
        self.line_text = line_text


# issued when a new file is opened for processing
class NewFile(ParserMessage):
    def __init__(self, file_name):
        self.file_name = file_name


# issued when end of file reached
class EndOfFile(ParserMessage):
    def __init__(self, file_name):
        self.file_name = file_name


class Variable(ParserMessage):
    def __init__(self, name, var_type, value):
        self.name = name
        self.type = var_type
        self.value = value


class Class(ParserMessage):
    def __init__(self, name, bases, deriveds):
        self.name = name
        self.bases = bases
        self.deriveds = deriveds

# The Parser Class is the subject in an observer pattern.
# It is responsible for parsing through header and implementation files
# and notifying tests of c++ entities for evaluation


class Parser:
    def _init__(self):
        # public
        self.headers = []
        self.cpp_files = []
        # private
        self.__testchain = []

    def parse(self):
        for header in self.headers:
            file = open(header, "r")
            self.__readline(file)
        for cpp in self.cpp_files:
            self.__readline(file)

    def __readline(self, file):
        for line in file:
            print("todo: readline")

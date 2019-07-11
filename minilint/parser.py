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

    def parse_all_files(self):
        for header in self.headers:
            self.announce_new_filename(header)
            file = open(header, "r")
            self.__read_lines(file, True)
        for cpp in self.cpp_files:
            self.announce_new_filename(cpp)
            self.__read_lines(file, False)

    def __read_lines(self, file, file_is_header):
        for line in file:
            if file_is_header:
                self.announce_new_header_line(line)
            else:
                self.announce_new_cpp_line(line)

    # notifying functions for observers

    def announce_new_filename(self, filename):
        pass

    def announce_new_header_line(self, line):
        pass

    def announce_new_cpp_line(self, line):
        pass

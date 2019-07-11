# The Parser Class is the subject in an observer pattern.
# It is responsible for parsing through header and implementation files
# and notifying tests of c++ entities for evaluation


class Parser:
    def _init__(self):
        # public
        self.headers = []
        self.cpp_files = []

    def parse_all_files(self):
        for header in self.headers:
            self.__parse_file(header, True)
        for cpp in self.cpp_files:
            self.__parse_file(cpp, False)

    def __parse_file(self, file, file_is_header):
        self.announce_new_filename(file)
        file = open(file, "r")
        self.__read_lines(file, file_is_header)

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

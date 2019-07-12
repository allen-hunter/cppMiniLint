# abstract base class (interface) for tests.  Follows the observer pattern with the intention
# of using parser as the subject.  Every code test should inherit from this class


class Test:
    def __init__(self):
        self._line_number = 0
        self._filename = ""
        self.report = ""

    # this introduces a bit of incoherence.  Consider decomposing.
    #todo: decompose report
    def produce_report(self):
        pass

    def add_line_to_report(self, line):
        print(line)

# for the observer pattern
    def receive_new_header_line(self, line):
        self._line_number += 1

    def receive_new_cpp_line(self, line):
        self._line_number += 1

    def receive_new_filename(self, name):
        self._filename = name
        self._line_number = 0

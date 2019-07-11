# abstract base class (interface) for tests.  Follows the observer pattern with the intention
# of using parser as the subject.  Every code test should inherit from this class


class Test:
    def __init__(self):
        self.report = ""

    # this introduces a bit of incoherence.  Consider decomposing.
    def produce_report(self):
        pass

# for the observer pattern
    def receive_new_header_line(self, line):
        pass

    def receive_new_cpp_line(self, line):
        pass

    def receive_new_filename(self, name):
        pass

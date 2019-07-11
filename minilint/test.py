# abstract base class (interface) for tests.  Follows the observer pattern with the intention
# of using parser as the subject.  Every code test should inherit from this class


class Test:
    def receive_new_header_line(self):
        pass

    def receive_new_cpp_line(self):
        pass

    def receive_new_filename(self):
        pass
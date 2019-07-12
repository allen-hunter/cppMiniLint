from minilint.test import *


class TestSuite(Test):
    def __init__(self):
        # public
        self.tests_to_run = []
        super(TestSuite, self).__init__()

    def produce_report(self):
        for test in self.tests_to_run:
            test.produce_report()
        print("\nreport!\n")
            #todo: implement report

    # for the observer pattern
    def receive_new_header_line(self, line):
        for test in self.tests_to_run:
            test.receive_new_header_line(line)

    def receive_new_cpp_line(self, line):
        for test in self.tests_to_run:
            test.receive_new_cpp_line(line)

    def receive_new_filename(self, name):
        for test in self.tests_to_run:
            test.receive_new_filename(name)

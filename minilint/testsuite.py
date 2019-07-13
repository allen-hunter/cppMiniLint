from minilint.test import *


class TestSuite(Test):
    def __init__(self):
        # public
        self.tests_to_run = []
        self.__file_names = []
        super(TestSuite, self).__init__()

    #todo: this detracts from class coherence.  solve that.
    def produce_report(self):
        return_string = ""
        for file_name in self.__file_names:
            report_for_file = self.get_file_report_from_all_tests(file_name)
            if len(report_for_file) > 0:
                return_string += return_string + file_name + ":\n"+report_for_file
        return return_string

    def get_file_report_from_all_tests(self, file_name):
        return_string = ""
        for test in self.tests_to_run:
            messages = test.report.get_messages(file_name)
            if len(messages) > 0:
                return_string += str(test.__class__) + ":\n"
            for message in messages:
                return_string += "\tline " + str(message) + ": " \
                        + str(messages[message]) + "\n"
        return return_string

    # for the observer pattern
    def receive_new_header_line(self, line):
        for test in self.tests_to_run:
            test.receive_new_header_line(line)

    def receive_new_cpp_line(self, line):
        for test in self.tests_to_run:
            test.receive_new_cpp_line(line)

    def receive_new_filename(self, name):
        self.__file_names.append(name)
        for test in self.tests_to_run:
            test.receive_new_filename(name)

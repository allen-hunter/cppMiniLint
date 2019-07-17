from minilint.test import *


class TestSuite(Test):
    def __init__(self):
        # public
        self.tests_to_run = []
        self.__file_names = []
        super(TestSuite, self).__init__()

    def produce_report(self):
        for test in self.tests_to_run:
            self.report += test.report
        return self.report.produce_report()

    # for the observer pattern.  Inherited from test
    def receive_message(self, parser_message):
        super(TestSuite, self).receive_message(parser_message)
        if isinstance(parser_message, NewFile):
            self.__file_names.append(parser_message.file_name)
        for test in self.tests_to_run:
            test.receive_message(parser_message)

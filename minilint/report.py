import collections


# storage class for test output
class Report:
    def __init__(self):
        self.issues = collections.defaultdict(dict)  # 2 dimensional dictionary, file[line:message]

    def add_message(self, file_name, line_number, message):
        self.issues[file_name][line_number] = message

    def get_messages(self, file_name):
        return self.issues[file_name]

    def get_message(self, file_name, line_number):
        return self.issues[file_name][line_number]

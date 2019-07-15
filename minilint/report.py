import collections


# storage class for test output
class Report:
    def __init__(self):
        self.issues = collections.defaultdict(lambda: collections.defaultdict(list))  # 2 dimensional dictionary, file[line:[messages]]

    def add_message(self, file_name, line_number, message):
        self.issues[file_name][line_number].append(message)  # you can have multiple messages per line

    def get_messages(self, file_name):
        return self.issues[file_name]  # returns line:[messsages]

    def get_message(self, file_name, line_number):
        return self.issues[file_name][line_number] # returns [messages]
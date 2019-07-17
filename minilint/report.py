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
        return self.issues[file_name][line_number]  # returns [messages]

    def __iadd__(self, other):  # += operator overrride
        for file_name in other.issues:
            self._add_lines(other, file_name)
        return self

    def _add_lines(self, other, file_name):
        for line_number in other.issues[file_name]:
            self._add_messages(other, file_name, line_number)

    def _add_messages(self, other, file_name, line_number):
        for message in other.issues[file_name][line_number]:
            self.issues[file_name][line_number].append(message)

    def produce_report(self):
        return self._produce_report_of_files()

    def _produce_report_of_files(self):
        return_string = ""
        for file in self.issues:
            report_from_file = self._produce_report_of_lines(file)
            return_string += self.format_if_has_content(str(file)+"\n", report_from_file, "")
        return return_string

    def format_if_has_content(self, prefix, new_text, postfix):
        if len(new_text) > 0:
            return prefix + new_text + postfix

    def _produce_report_of_lines(self, file):
        return_string = ""
        for line_number in self.issues[file]:
            report_from_line = self._produce_report_of_messages(file, line_number)
            return_string += self.format_if_has_content("\tline: " + str(line_number) +"\n", report_from_line, "")
        return return_string

    def _produce_report_of_messages(self, file, line_number):
        return_string = ""
        for message in self.issues[file][line_number]:
            return_string = self.format_if_has_content("\t\t", message, "\n")
        return return_string

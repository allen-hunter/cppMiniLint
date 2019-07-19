import collections
import os
# storage class and report generation

class Report:
    def __init__(self):
        self.issues = collections.defaultdict(
            lambda: collections.defaultdict(list))  # 2 dimensional dictionary, file[line:[messages]]
        self.scores = collections.defaultdict(
            lambda: collections.defaultdict(int))  # 2 dimensional dictionary, file[test:score]
        self.references = {}  # dictionary of name(str):refcount(int
        self.weight = 1.0  # test multiplies number of errors against this to get its badness score

# storage methods
    def add_message(self, file_name, line_number, message):
        self.issues[file_name][line_number].append(message)  # you can have multiple messages per line

    def get_messages(self, file_name):
        return self.issues[file_name]  # returns line:[messsages]

    def get_message(self, file_name, line_number):
        return self.issues[file_name][line_number]  # returns [messages]

    def clear(self, file_name):
        self.issues[file_name].clear()

    def __iadd__(self, other):  # += operator overrride
        self.scores.update(other.scores)
        for file_name in other.issues:
            self._add_lines(other, file_name)
        return self

    def _add_lines(self, other, file_name):
        for line_number in other.issues[file_name]:
            self._add_messages(other, file_name, line_number)

    def _add_messages(self, other, file_name, line_number):
        for message in other.issues[file_name][line_number]:
            self.issues[file_name][line_number].append(message)

    def _remove_path(self, file_name_with_path):
        dir_name, file_name = os.path.split(file_name_with_path)
        return file_name

    def add_reference(self, file_name_with_path):
        file_name_sans_path = self._remove_path(file_name_with_path)
        self.references[file_name_sans_path] = self.references.get(file_name_sans_path, 0) + 1

    def finish_file(self, file_name_with_path, test):
        file_name_sans_path = self._remove_path(file_name_with_path)
        for line in self.issues[file_name_with_path]:
            self.scores[test][file_name_sans_path] += (len(self.issues[file_name_with_path][line]) * self.weight)

# report generation methods
    def produce_report(self):
        return self._produce_report_of_files()

    def sort_by_reference_and_weight(self, file_name_with_path):
        file_name_sans_path = self._remove_path(file_name_with_path)
        references = 1 + self.references.get(file_name_sans_path, 0)
        combined_weight = 0
        for test in self.scores:
            combined_weight += self.scores[test][file_name_sans_path]
        return combined_weight * references

    def _produce_report_of_files(self):
        return_string = ""
        # dirtiest files first
        for file in sorted(self.issues, key=lambda file: self.sort_by_reference_and_weight(file), reverse=True):
            report_from_file = self._produce_report_of_lines(file)
            return_string += self.format_if_has_content(str(file)+"\n", report_from_file, "")
        return return_string

    def format_if_has_content(self, prefix, new_text, postfix):
        if len(new_text) > 0:
            return prefix + new_text + postfix

    def _produce_report_of_lines(self, file):
        return_string = ""
        for line_number in sorted (self.issues[file]):
            report_from_line = self._produce_report_of_messages(file, line_number)
            return_string += self.format_if_has_content("\tline: " + str(line_number) +"\n", report_from_line, "")
        return return_string

    def _produce_report_of_messages(self, file, line_number):
        return_string = ""
        for message in self.issues[file][line_number]:
            return_string = self.format_if_has_content("\t\t", message, "\n")
        return return_string

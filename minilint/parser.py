from minilint.testsuite import TestSuite
from minilint.parser_message import *
from pygccxml import utils
from pygccxml import declarations
from pygccxml import parser
import re
import ntpath
import os
# The Parser Class is the subject in an observer pattern.
# It is responsible for parsing through header and implementation files
# and notifying tests of c++ entities for evaluation


class Parser(object):

    def __init__(self, file_list_to_parse):
        # public
        self._file_list = file_list_to_parse
        self.test_suite = TestSuite()
        self._include_regex = re.compile("#include\s*[\"|\<].*?[\"|\>]", re.IGNORECASE)  # ignoring __has_include
        # todo: pull from config
        self._xml_generator_config = parser.xml_generator_configuration_t(
            xml_generator_path="C:\\castxml\\bin\\castxml.exe",
            xml_generator="castxml",
            compiler_path="C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Professional\\VC\\Tools\\MSVC\\14.16.27023\\bin\\Hostx64\\x64\\cl.exe")

    def parse_all_files(self):
        for header in self._file_list.headers:
            self._parse_file(header, True)
        for cpp in self._file_list.cpp_files:
            self._parse_file(cpp, False)

    def _parse_file(self, file_name, file_is_header):
        self.test_suite.receive_message(NewFile(file_name))
        file = open(file_name, "r")
        self._read_lines(file, file_is_header)
        file.close()
        self.test_suite.receive_message(EndOfFile(file_name))

    def _read_lines(self, file, file_is_header):
        for line in file:
            self._look_for_reference(line)
            self.test_suite.receive_message(LineFromFile(file_is_header,line))
        if file_is_header:
            self._extract_symbols(file.name)

    def _look_for_reference(self, line):
        matches = self._include_regex.findall(line)
        for match in matches:
            match = re.sub("#include\s*[\"|\<]", "", match, flags=re.IGNORECASE)
            match = re.sub("[\"|\>]", "", match, flags=re.IGNORECASE)
            match = ntpath.basename(match)  # remove the path
            self.test_suite.report.add_reference(match)
        return len(matches)

    def _extract_symbols(self, filename):
        decls = parser.parse([filename], self._xml_generator_config )
        global_namespace = declarations.get_global_namespace(decls)
        self._extract_variables(global_namespace)
        self._extract_classes(global_namespace)

    def _extract_variables(self, global_namespace):
        # long argument because if you do not hand the last option a True, then it spouts warnings
        for var in global_namespace.variables(None, None, None, None, None, None, True):
            self.test_suite.receive_message(Variable(var.name, var.decl_type, var.value))

    def _extract_classes(self, global_namespace):
        for class_ in global_namespace.classes(None, None, None, None, None, True):
            bases = [base.related_class.name for base in class_.bases]
            deriveds = [derive.related_class.name for derive in class_.derived]
            self.test_suite.receive_message(Class(class_.name, bases, deriveds))

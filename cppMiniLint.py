import sys
import os
# import architecture
from minilint.parser import Parser
from minilint.filelist import FileList
# import tests
from minilint.code_tests.if_zero import IfZero
from minilint.code_tests.too_long import TooLong


def print_report(parser, file_name):
    report = parser.test_suite.produce_report()
    # print(report)
    output_file = open(file_name, "w")
    output_file.write(report)
    output_file.close()


def add_tests(parser):
    parser.test_suite.tests_to_run.append(IfZero())
    parser.test_suite.tests_to_run.append(TooLong())

# This is the "main"
# it should:
#   take a directory argument
#   take an output file argument
#   create a list of files for evaluation
#   invoke evaluations
if len(sys.argv) != 3:
    print("usage: cppMiniLint.py directory outputfilename")
else:
    print("Starting...")
    files = FileList()
    files.load_directory(sys.argv[1])
    parser = Parser(files)
    add_tests(parser)
    parser.parse_all_files()
    print_report(parser,sys.argv[2])
    print("Done.  Output is in ", sys.argv[2])

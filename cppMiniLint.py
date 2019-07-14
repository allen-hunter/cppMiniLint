import sys
import os
from minilint.parser import *
from minilint.code_tests.ifzero import *
# todo: config file


# creates a list of filenames in all the directoris below path
# that are of filetype suffix
#
# arguments:
# path is a string describing the path
# suffix is a string describing the file type (ie '.h')


def collect_file_names(path, suffix):
    file_names_with_path = []
    for root, directories, file_names in os.walk(path):
        for file in file_names:
            if suffix in file:
                file_names_with_path.append(os.path.join(root, file))
    return file_names_with_path


def print_report(parser, file_name):
    report = parser.test_suite.produce_report()
    # print(report)
    output_file = open(file_name, "w")
    output_file.write(report)
    output_file.close()

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
    parser = Parser()
    parser.headers = collect_file_names(sys.argv[1], '.h')
    parser.cpp_files = collect_file_names(sys.argv[1], '.cpp')
    parser.test_suite.tests_to_run.append(IfZero())
    parser.parse_all_files()
    print_report(parser,sys.argv[2])
    print("Done.  Output is in ", sys.argv[2])

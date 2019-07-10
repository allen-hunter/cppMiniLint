import sys
import os
#from minilint.parser import skycake
from minilint.parser import *

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


# This is the "main"
# it should:
#   take a directory argument
#   take an output file argument
#   create a list of files for evaluation
#   invoke evaluations
if len(sys.argv) != 3:
    print("usage: cppMiniLint.py directory outputfilename")
else:
    print("Starting..")
    # TODO: processing here
    parser = Parser()
    parser.headers = collect_file_names(sys.argv[1], '.h')
    parser.cpp_files = collect_file_names(sys.argv[1], '.cpp')
    for f in parser.headers:
        print(f)
    for f in parser.cpp_files:
        print(f)
    print("Done.  Output is in ", sys.argv[2])

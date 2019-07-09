import sys
import os


# creates a list of filenames in all the directoris below path
# that are of filetype suffix
#
# arguments:
# path is a string describing the path
# suffix is a string describing the file type (ie '.h')
def collect_filenames(path, suffix):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if suffix in file:
                files.append(os.path.join(r, file))
    return files


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
    files = collect_filenames(sys.argv[1], '.py')
    for f in files:
        print(f)
    print("Done.  Output is in ", sys.argv[2])

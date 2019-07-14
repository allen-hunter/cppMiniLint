import os

# a collection object for files for consideration

class File_List(object):

    def __init__(self):
        self.headers = []
        self.cpp_files = []

    def clear(self):
        self.headers = []
        self.cpp_files = []

    def load_directory(self, path):
        self.headers += self.__collect_file_names_from_path(path, ['.h', '.hpp'])
        self.cpp_files += self.__collect_file_names_from_path(path, ['c', '.cpp'])

    def __collect_file_names_from_path(self, path, suffixes):
        file_names_with_path = []
        for root, directories, file_names in os.walk(path):
            for file in file_names:
                if self.__suffix_matches(file, suffixes):
                    file_names_with_path.append(os.path.join(root, file))
        return file_names_with_path

    def __suffix_matches(self, file, suffixes):
        for suffix in suffixes:
            if str(file).lower().endswith(suffix):
                return True
        return False
    
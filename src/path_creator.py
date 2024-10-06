import os
import re


class PathCreator:
    def get_full_path(self, suffix, regex_pattern):
        root_dir = os.path.abspath(suffix)
        files = []

        try:
            for root, dirs, _ in os.walk(root_dir):
                matching_dirs = [d for d in dirs if re.match(regex_pattern, d)]
                files.extend(matching_dirs)
        except Exception as e:
            return self.file_not_founded_result()

        if self.check_single_count_file(files):
            print("Multiple files were found: " + ", ".join(files))
        elif not files:
            return self.file_not_founded_result()

        return os.path.join(suffix, files[0])

    @staticmethod
    def file_not_founded_result():
        print("File not found")
        return None

    @staticmethod
    def check_single_count_file(files):
        return len(files) > 1

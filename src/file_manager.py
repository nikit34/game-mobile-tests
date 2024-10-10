import os


class FileManager:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def remove(self, folder_path):
        path = str(os.path.join(self.current_dir, folder_path))
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if filename != '.gitkeep':
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)

    @classmethod
    def get_full_path(cls, suffix, regex_pattern):
        root_dir = os.path.abspath(suffix)
        files = []

        try:
            for root, dirs, _ in os.walk(root_dir):
                matching_dirs = [d for d in dirs if re.match(regex_pattern, d)]
                files.extend(matching_dirs)
        except Exception as e:
            return cls._file_not_founded_result()

        if cls._check_single_count_file(files):
            print("Multiple files were found: " + ", ".join(files))
        elif not files:
            return cls._file_not_founded_result()

        return os.path.join(suffix, files[0])

    @staticmethod
    def _file_not_founded_result():
        print("File not found")
        return None

    @staticmethod
    def _check_single_count_file(files):
        return len(files) > 1

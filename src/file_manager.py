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

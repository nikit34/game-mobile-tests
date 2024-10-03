import json
import os


class Config:
    _config_data = None

    @classmethod
    def load_config(cls, file_name):
        if cls._config_data is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, file_name)
            with open(file_path, 'r') as file:
                cls._config_data = json.load(file)
        return cls._config_data

    @classmethod
    def get_package_name(cls):
        return cls.load_config('desired_caps.json')['appium:appPackage']

    @classmethod
    def get_desired_caps(cls):
        return cls.load_config('desired_caps.json')

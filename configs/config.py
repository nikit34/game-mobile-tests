import json
import os


class Config:
    _config_cache = {}

    @classmethod
    def load_config(cls, file_name):
        if file_name not in cls._config_cache:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, file_name)
            with open(file_path, 'r') as file:
                cls._config_cache[file_name] = json.load(file)
        return cls._config_cache[file_name]

    @classmethod
    def get_package_name(cls):
        return cls.load_config('desired_caps.json').get('appium:appPackage')

    @classmethod
    def get_desired_caps(cls):
        return cls.load_config('desired_caps.json')

    @classmethod
    def get_implicitly_timeout(cls):
        return cls.load_config('waiting.json').get('implicitly_timeout')

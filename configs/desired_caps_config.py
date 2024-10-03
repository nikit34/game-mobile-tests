from configs.config import Config


class DesiredCapsConfig(Config):
    @classmethod
    def get_package_name(cls):
        return cls.load_config('json/desired_caps.json').get('appium:appPackage')

    @classmethod
    def get_desired_caps(cls):
        return cls.load_config('json/desired_caps.json')
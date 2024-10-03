from configs.config import Config


class AppiumConfig(Config):
    @classmethod
    def get_host(cls):
        return cls.load_config('json/appium.json').get('host')

    @classmethod
    def get_port(cls):
        return cls.load_config('json/appium.json').get('port')

    @classmethod
    def get_timeout(cls):
        return cls.load_config('json/appium.json').get('timeout')

from configs._config import Config


class AppiumConfig(Config):
    CONFIG = 'json/appium.json'

    @classmethod
    def get_host(cls):
        return cls.load_config(cls.CONFIG).get('host')

    @classmethod
    def get_port(cls):
        return cls.load_config(cls.CONFIG).get('port')

    @classmethod
    def get_timeout(cls):
        return cls.load_config(cls.CONFIG).get('timeout')

from configs._config import Config


class EnvironmentConfig(Config):
    CONFIG = 'json/environment.json'

    @classmethod
    def get_platform(cls):
        platform = cls.load_config(cls.CONFIG).get('platform').lower()
        if platform not in ['ios', 'android']:
            raise ValueError('The platform can only be ios or android')
        return platform

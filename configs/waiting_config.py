from configs._config import Config


class WaitingConfig(Config):
    CONFIG = 'json/waiting.json'

    @classmethod
    def get_implicitly_timeout(cls):
        return cls.load_config(cls.CONFIG).get('implicitly_timeout')
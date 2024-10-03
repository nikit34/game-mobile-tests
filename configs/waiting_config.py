from configs._config import Config


class WaitingConfig(Config):
    @classmethod
    def get_implicitly_timeout(cls):
        return cls.load_config('json/waiting.json').get('implicitly_timeout')
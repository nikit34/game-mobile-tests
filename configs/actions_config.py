from configs._config import Config


class ActionsConfig(Config):
    CONFIG = 'json/actions.json'

    @classmethod
    def get_duration(cls):
        return cls.load_config(cls.CONFIG).get('duration')

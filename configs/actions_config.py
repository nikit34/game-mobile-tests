from configs._config import Config


class ActionsConfig(Config):
    @classmethod
    def get_duration(cls):
        return cls.load_config('json/actions.json').get('duration')

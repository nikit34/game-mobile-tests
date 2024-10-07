from configs._config import Config


class ImagesCheckerConfig(Config):
    CONFIG = 'json/images_checker.json'

    @classmethod
    def get_tolerance(cls):
        return cls.load_config(cls.CONFIG).get('tolerance')

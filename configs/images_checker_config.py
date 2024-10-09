from configs._config import Config


class ImagesCheckerConfig(Config):
    CONFIG = 'json/images_checker.json'

    @classmethod
    def get_tolerance(cls):
        return cls.load_config(cls.CONFIG).get('tolerance')

    @classmethod
    def get_train_tolerance(cls):
        return cls.load_config(cls.CONFIG).get('train_tolerance')

    @classmethod
    def get_train_factor_count_error(cls):
        return cls.load_config(cls.CONFIG).get('train_factor_count_error')

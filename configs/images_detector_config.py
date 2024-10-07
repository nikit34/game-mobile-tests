from configs._config import Config


class ImagesDetectorConfig(Config):
    CONFIG = 'json/images_detector.json'

    @classmethod
    def get_eps(cls):
        return cls.load_config(cls.CONFIG).get('eps')

    @classmethod
    def get_clahe_clip_limit(cls):
        return cls.load_config(cls.CONFIG).get('clahe_clip_limit')

    @classmethod
    def get_clahe_grid_size(cls):
        return cls.load_config(cls.CONFIG).get('clahe_grid_size')

    @classmethod
    def get_min_color_similarity(cls):
        return cls.load_config(cls.CONFIG).get('min_color_similarity')

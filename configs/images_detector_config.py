from configs._config import Config


class ImagesDetectorConfig(Config):
    CONFIG = 'json/images_detector.json'

    @classmethod
    def get_n_octave_layers(cls):
        return cls.load_config(cls.CONFIG).get('n_octave_layers')

    @classmethod
    def get_contrast_threshold(cls):
        return cls.load_config(cls.CONFIG).get('contrast_threshold')

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
    def get_min_cluster_area(cls):
        return cls.load_config(cls.CONFIG).get('min_cluster_area')

    @classmethod
    def get_min_samples(cls):
        return cls.load_config(cls.CONFIG).get('min_samples')

    @classmethod
    def get_ransac(cls):
        return cls.load_config(cls.CONFIG).get('ransac')

    @classmethod
    def get_ransac_threshold(cls):
        return cls.load_config(cls.CONFIG).get('ransac_threshold')

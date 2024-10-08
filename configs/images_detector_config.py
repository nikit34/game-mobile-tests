from configs._config import Config


class ImagesDetectorConfig(Config):
    FOLDER_CONFIG = 'json/images_detectors/'

    def __init__(self, name_target):
        self.config = self.get_images_detector(name_target)

    def get_images_detector(self, name_target):
        return self.load_config(self.FOLDER_CONFIG + name_target + ".json")

    def get_n_octave_layers(self):
        return self.config.get('n_octave_layers')

    def get_contrast_threshold(self):
        return self.config.get('contrast_threshold')

    def get_eps(self):
        return self.config.get('eps')

    def get_clahe_clip_limit(self):
        return self.config.get('clahe_clip_limit')

    def get_clahe_grid_size(self):
        return self.config.get('clahe_grid_size')

    def get_min_cluster_area(self):
        return self.config.get('min_cluster_area')

    def get_min_samples(self):
        return self.config.get('min_samples')

    def get_ransac(self):
        return self.config.get('ransac')

    def get_ransac_threshold(self):
        return self.config.get('ransac_threshold')

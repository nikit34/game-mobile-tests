import cv2
import numpy as np
from sklearn.cluster import DBSCAN

from configs.images_detector_config import ImagesDetectorConfig


class ImageDetector:
    def __init__(
            self,
            eps=ImagesDetectorConfig.get_eps(),
            clahe_clip_limit=ImagesDetectorConfig.get_clahe_clip_limit(),
            clahe_grid_size=ImagesDetectorConfig.get_clahe_grid_size(),
            min_color_similarity=ImagesDetectorConfig.get_min_color_similarity(),
            min_cluster_area=ImagesDetectorConfig.get_min_cluster_area()
    ):
        self.eps = eps
        self.clahe_clip_limit = clahe_clip_limit
        self.clahe_grid_size = clahe_grid_size
        self.min_color_similarity = min_color_similarity
        self.min_cluster_area = min_cluster_area

    @staticmethod
    def apply_clahe(image, clip_limit, grid_size):
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
        return clahe.apply(image)

    @staticmethod
    def get_color_histogram(image, bins=(8, 8, 8)):
        hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist, hist)
        return hist.flatten()

    @staticmethod
    def compute_sift_keypoints_and_descriptors(gray_image):
        sift = cv2.SIFT_create()
        return sift.detectAndCompute(gray_image, None)

    @staticmethod
    def match_descriptors(des1, des2):
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches = bf.match(des1, des2)
        return sorted(matches, key=lambda x: x.distance)

    @staticmethod
    def extract_coordinates_from_matches(matches, keypoints):
        coordinates = []
        for match in matches:
            x, y = keypoints[match.trainIdx].pt
            coordinates.append((int(x), int(y)))
        return coordinates

    @staticmethod
    def perform_clustering(coordinates, eps):
        if len(coordinates) > 0:
            coordinates = np.array(coordinates)
            clustering = DBSCAN(eps=eps).fit(coordinates)
            cluster_labels = clustering.labels_
            clustered_coords = coordinates[cluster_labels != -1]
            return clustered_coords, cluster_labels
        else:
            return np.array([]), []

    @staticmethod
    def get_cluster_bounds(coordinates, cluster_labels, min_area):
        cluster_bounds = []
        unique_labels = set(cluster_labels) - {-1}

        coordinates = np.array(coordinates)

        for label in unique_labels:
            cluster_points = coordinates[cluster_labels == label]
            x_min, y_min = np.min(cluster_points, axis=0)
            x_max, y_max = np.max(cluster_points, axis=0)
            width = x_max - x_min
            height = y_max - y_min
            area = width * height

            if area >= min_area:
                cluster_bounds.append(((int(x_min), int(y_min)), (int(x_max), int(y_max))))

        return cluster_bounds

    @staticmethod
    def draw_clusters_and_points(image, cluster_bounds, clustered_coords):
        for (x_min, y_min), (x_max, y_max) in cluster_bounds:
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        for x, y in clustered_coords:
            cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

    @staticmethod
    def convert_to_color_if_needed(image):
        if image.ndim == 2:
            return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        return image

    def get_coordinates_objects(self, original_img, template_img):
        original_img.cv_image = self.convert_to_color_if_needed(original_img.cv_image)
        template_img.cv_image = self.convert_to_color_if_needed(template_img.cv_image)

        gray_original = cv2.cvtColor(original_img.cv_image, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template_img.cv_image, cv2.COLOR_BGR2GRAY)

        gray_original = self.apply_clahe(gray_original, self.clahe_clip_limit, self.clahe_grid_size)
        gray_template = self.apply_clahe(gray_template, self.clahe_clip_limit, self.clahe_grid_size)

        kp1, des1 = self.compute_sift_keypoints_and_descriptors(gray_template)
        kp2, des2 = self.compute_sift_keypoints_and_descriptors(gray_original)

        matches = self.match_descriptors(des1, des2)
        coordinates = self.extract_coordinates_from_matches(matches, kp2)

        clustered_coords, cluster_labels = self.perform_clustering(coordinates, self.eps)
        cluster_bounds = self.get_cluster_bounds(coordinates, cluster_labels, self.min_cluster_area)

        self.draw_clusters_and_points(original_img.cv_image, cluster_bounds, clustered_coords)

        color_hist_template = self.get_color_histogram(template_img.cv_image)
        color_hist_original = self.get_color_histogram(original_img.cv_image)
        color_similarity = cv2.compareHist(color_hist_template, color_hist_original, cv2.HISTCMP_CORREL)

        if color_similarity > self.min_color_similarity:
            original_img.save("detected")
            template_img.save("template")
            return cluster_bounds
        else:
            return []

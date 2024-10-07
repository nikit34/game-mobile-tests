import cv2


class ImageDetector:
    @staticmethod
    def apply_clahe(image):
        clahe = cv2.createCLAHE(clipLimit=7.0, tileGridSize=(8, 8))
        return clahe.apply(image)

    @staticmethod
    def get_color_histogram(image, bins=(8, 8, 8)):
        hist = cv2.calcHist([image], [0, 1, 2], None, bins, [0, 256, 0, 256, 0, 256])
        cv2.normalize(hist, hist)
        return hist.flatten()

    @staticmethod
    def get_coordinates_objects(original_img, template_img):
        if original_img.cv_image.ndim == 2:
            original_img.cv_image = cv2.cvtColor(original_img.cv_image, cv2.COLOR_GRAY2BGR)
        if template_img.cv_image.ndim == 2:
            template_img.cv_image = cv2.cvtColor(template_img.cv_image, cv2.COLOR_GRAY2BGR)

        gray_original = cv2.cvtColor(original_img.cv_image, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template_img.cv_image, cv2.COLOR_BGR2GRAY)

        gray_original = ImageDetector.apply_clahe(gray_original)
        gray_template = ImageDetector.apply_clahe(gray_template)

        sift = cv2.SIFT_create()

        kp1, des1 = sift.detectAndCompute(gray_template, None)
        kp2, des2 = sift.detectAndCompute(gray_original, None)

        color_hist_template = ImageDetector.get_color_histogram(template_img.cv_image)
        color_hist_original = ImageDetector.get_color_histogram(original_img.cv_image)

        color_similarity = cv2.compareHist(color_hist_template, color_hist_original, cv2.HISTCMP_CORREL)

        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches = bf.match(des1, des2)

        matches = sorted(matches, key=lambda x: x.distance)

        coordinates = []
        for match in matches:
            x, y = kp2[match.trainIdx].pt
            coordinates.append((int(x), int(y)))

            cv2.circle(original_img.cv_image, (int(x), int(y)), 5, (0, 255, 0), 2)

        if color_similarity > 0.2:
            original_img.save("detected")
            template_img.save("template")
            return coordinates
        else:
            return []

import cv2
import numpy as np

class Flag:
    def __init__(self, file_location: str = None, image: np.ndarray = None):
        self.file_location = file_location
        self.features = {}
        self.image = image
        self._edges = None

    def get_edges(self):
        if self._edges is not None:
            return self._edges
        edges = cv2.Canny(self.image, 0, 200, apertureSize=3)
        self._edges = edges
        return self._edges

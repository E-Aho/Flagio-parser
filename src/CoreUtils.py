import cv2
import numpy as np

def get_boundaries(image: np.ndarray) -> np.ndarray:
    """Takes in an image object, returns an array of edges in [x0, y0, x1, y1] format"""

    img_scale = min(len(image[0]), len(image))
    min_line_len = int(img_scale * 0.2)
    max_line_gap = int(img_scale * 0.2)
    edges = cv2.Canny(image, 0, 200, apertureSize=3)
    lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, minLineLength=min_line_len, maxLineGap=max_line_gap,
                            threshold=10)

    return lines


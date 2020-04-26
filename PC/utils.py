import numpy as np
import cv2
from func import *
SIZE = (400, 300)

RECT = np.float32([[0, 299],
                   [399, 299],
                   [399, 0],
                   [0, 0]])

TRAP = np.float32([[0, 299],
                   [399, 299],
                   [320, 200],
                   [80, 200]])
class taskOneMain:
    def __init__(self):
        pass
    def transform(self, frame):
        img = cv2.resize(frame, (400, 300))
        binary = binarize(img)
        perspective = trans_perspective(binary, TRAP, RECT, SIZE)
        return perspective
    def detect_stop_line(self, frame):
        perspective = self.transform(frame)
        if np.mean(perspective[90:110, 150:200]) > 200:
            return True
        else:
            return False

import cv2
import numpy as np

def detect_coconut(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Brown color range
    lower = np.array([5, 40, 40])
    upper = np.array([25, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    area = cv2.countNonZero(mask)

    return area > 6000  # threshold

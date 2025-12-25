import cv2
import numpy as np

def detect_coconut(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_brown = np.array([5, 50, 50])
    upper_brown = np.array([20, 255, 255])
    mask = cv2.inRange(hsv, lower_brown, upper_brown)
    area = cv2.countNonZero(mask)

    return area > 5000

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

def is_coconut():
    ret, frame = camera.read()
    if not ret:
        return False

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([10, 40, 40])
    upper = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 15000:
            return True
    return False

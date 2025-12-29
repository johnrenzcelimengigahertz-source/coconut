import cv2
from vision import detect_coconut
from sound_analyzer import analyze_sound
from serial_comm import read_sensor, send_command

print("=== Coconut Sorting System Started ===")

coconut_count = 0

while True:
    sensor = read_sensor()

    if sensor == "DETECTED":
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            print("Camera error")
            continue

        if not detect_coconut(frame):
            print("Non-coconut detected → ignored")
            continue

        coconut_count += 1
        print(f"\n🥥 Coconut #{coconut_count} detected")

        send_command("TAP")  # Tap coconut
        coconut_type = analyze_sound()

        print(f"➡ Type: {coconut_type}")
        print("----------------------------------")

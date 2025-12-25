import cv2
from vision import detect_coconut
from sound_analyzer import analyze_sound
from serial_comm import send_command, read_sensor

coconut_count = 0

print("System Ready...")

while True:
    sensor = read_sensor()

    if sensor == "DETECTED":
        frame = cv2.VideoCapture(0).read()[1]
        is_coconut = detect_coconut(frame)

        if not is_coconut:
            print("Non-coconut detected. Ignored.")
            continue

        coconut_count += 1
        print(f"Coconut #{coconut_count} detected")

        send_command("TAP")  # Trigger solenoid
        coconut_type = analyze_sound()

        print(f"Coconut Type: {coconut_type}")
        print(f"Total Coconuts: {coconut_count}")

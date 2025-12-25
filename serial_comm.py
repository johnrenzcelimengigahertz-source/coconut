import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

def read_arduino():
    if arduino.in_waiting:
        return arduino.readline().decode().strip()
    return None

def send_arduino(msg):
    arduino.write(f"{msg}\n".encode())

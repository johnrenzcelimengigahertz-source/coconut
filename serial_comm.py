import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

def read_sensor():
    if arduino.in_waiting:
        return arduino.readline().decode().strip()
    return None

def send_command(cmd):
    arduino.write((cmd + "\n").encode())

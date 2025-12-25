import threading
import time
from serial_comm import read_arduino, send_arduino
from vision import is_coconut

# ================= GLOBAL STATE =================
total_coconut = 0
total_non_coconut = 0
coconut_queue = []

current_status = "IDLE"
next_smash = "-"

# ================= ACCESS FOR GUI =================
def get_status():
    return total_coconut, total_non_coconut, next_smash, current_status

# ================= MAIN LOOP =================
def sorter_loop():
    global total_coconut, total_non_coconut, next_smash, current_status

    while True:
        msg = read_arduino()
        if not msg:
            continue

        # ===== PHASE 1 =====
        if msg == "OBJECT_DETECTED":
            current_status = "DETECTING"

            if is_coconut():
                total_coconut += 1
                coconut_queue.append(total_coconut)
                send_arduino("COCONUT")
            else:
                total_non_coconut += 1
                send_arduino("NONCOCONUT")

            current_status = "IDLE"

        # ===== PHASE 2 =====
        elif msg == "COCONUT_AT_SENSOR2":
            if coconut_queue:
                coconut_id = coconut_queue.pop(0)
                next_smash = f"Coconut #{coconut_id}"
                current_status = "SMASHING"
                send_arduino(f"SMASH_{coconut_id}")
                time.sleep(1)
                next_smash = "-"
                current_status = "IDLE"

# ================= THREAD START =================
def start_sorter():
    threading.Thread(target=sorter_loop, daemon=True).start()

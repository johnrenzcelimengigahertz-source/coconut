import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# ---------- Coconut Detection Logic ----------
def detect_coconut(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # GREEN FRESH COCONUT (young coconut)
    green_lower = np.array([35, 40, 40])
    green_upper = np.array([85, 255, 255])

    # BROWN / DRY (non-coconut or old coconut)
    brown_lower = np.array([5, 40, 40])
    brown_upper = np.array([25, 255, 255])

    green_mask = cv2.inRange(hsv, green_lower, green_upper)
    brown_mask = cv2.inRange(hsv, brown_lower, brown_upper)

    green_area = cv2.countNonZero(green_mask)
    brown_area = cv2.countNonZero(brown_mask)

    # Thresholds (adjust if needed)
    if green_area > 6000:
        return "FRESH COCONUT", "green"
    elif brown_area > 6000:
        return "NON-COCONUT", "brown"
    else:
        return "UNKNOWN", "gray"


# ---------- GUI ----------
class CoconutDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coconut Detector")
        self.root.geometry("900x700")

        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.result_label = tk.Label(
            root,
            text="Detecting...",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="black",
            pady=10
        )
        self.result_label.pack(fill="x")

        self.cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            label, color = detect_coconut(frame)

            self.result_label.config(text=label, bg=color)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_frame)

    def on_close(self):
        self.cap.release()
        self.root.destroy()


# ---------- RUN ----------
root = tk.Tk()
app = CoconutDetectorApp(root)
root.protocol("WM_DELETE_WINDOW", app.on_close)
root.mainloop()

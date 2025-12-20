import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk

# ==============================
# CAMERA SETUP
# ==============================
cap = cv2.VideoCapture(0)  # 0 = default webcam

# ==============================
# MAIN WINDOW
# ==============================
root = tk.Tk()
root.title("Coconut Sorting System")
root.geometry("1100x600")
root.configure(bg="#e6d3a3")  # coconut husk color

# ==============================
# TITLE
# ==============================
title = tk.Label(
    root,
    text="🥥 Coconut Sorting System",
    font=("Arial", 26, "bold"),
    bg="#e6d3a3",
    fg="#4b2e1e"
)
title.pack(pady=10)

# ==============================
# MAIN FRAME
# ==============================
main_frame = tk.Frame(root, bg="#e6d3a3")
main_frame.pack(fill="both", expand=True)

# ==============================
# LEFT PANEL (CAMERA + COCONUTS)
# ==============================
left_frame = tk.Frame(main_frame, bg="#e6d3a3")
left_frame.pack(side="left", padx=20, pady=20)

# Camera label
camera_label = tk.Label(
    left_frame,
    text="Camera View",
    font=("Arial", 16, "bold"),
    bg="#e6d3a3",
    fg="#4b2e1e"
)
camera_label.pack()

# Camera display
camera_canvas = tk.Label(left_frame, bg="black")
camera_canvas.pack(pady=10)

# ==============================
# COCONUT DISPLAY
# ==============================
canvas = tk.Canvas(
    left_frame,
    width=500,
    height=200,
    bg="#f5e6c8",
    highlightthickness=0
)
canvas.pack(pady=10)

def draw_coconut(x, y, label):
    canvas.create_oval(
        x, y, x+120, y+100,
        fill="#7a4a2e",
        outline="#4b2e1e",
        width=3
    )
    # coconut eyes
    canvas.create_oval(x+35, y+35, x+45, y+45, fill="black")
    canvas.create_oval(x+55, y+35, x+65, y+45, fill="black")
    canvas.create_oval(x+75, y+35, x+85, y+45, fill="black")

    canvas.create_text(
        x+60, y+125,
        text=label,
        font=("Arial", 12, "bold"),
        fill="#4b2e1e"
    )

draw_coconut(20, 40, "Malauhog")
draw_coconut(190, 40, "Malakatad")
draw_coconut(360, 40, "Malakanin")

# ==============================
# RIGHT PANEL (STATUS)
# ==============================
status_frame = tk.Frame(
    main_frame,
    bg="#f5e6c8",
    width=300
)
status_frame.pack(side="right", fill="y", padx=20, pady=20)

status_title = tk.Label(
    status_frame,
    text="System Status",
    font=("Arial", 18, "bold"),
    bg="#f5e6c8",
    fg="#4b2e1e"
)
status_title.pack(pady=10)

detected_label = tk.Label(
    status_frame,
    text="Detected Coconut:",
    font=("Arial", 14),
    bg="#f5e6c8",
    fg="#4b2e1e"
)
detected_label.pack(pady=10)

detected_value = tk.Label(
    status_frame,
    text="---",
    font=("Arial", 22, "bold"),
    bg="#f5e6c8",
    fg="#2e7d32"
)
detected_value.pack(pady=10)

# ==============================
# DEMO BUTTONS (FOR TESTING)
# ==============================
def set_detected(name):
    detected_value.config(text=name)

ttk.Button(
    status_frame,
    text="Simulate Malauhog",
    command=lambda: set_detected("Malauhog")
).pack(fill="x", pady=5)

ttk.Button(
    status_frame,
    text="Simulate Malakatad",
    command=lambda: set_detected("Malakatad")
).pack(fill="x", pady=5)

ttk.Button(
    status_frame,
    text="Simulate Malakanin",
    command=lambda: set_detected("Malakanin")
).pack(fill="x", pady=5)

# ==============================
# CAMERA UPDATE LOOP
# ==============================
def update_camera():
    ret, frame = cap.read()
    if ret:
        # Flip for mirror view
        frame = cv2.flip(frame, 1)

        # Convert BGR → RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize for UI
        frame = cv2.resize(frame, (480, 270))

        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)

        camera_canvas.imgtk = imgtk
        camera_canvas.configure(image=imgtk)

    root.after(10, update_camera)

update_camera()

# ==============================
# CLEAN EXIT
# ==============================
def on_close():
    cap.release()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# ==============================
# START UI
# ==============================
root.mainloop()

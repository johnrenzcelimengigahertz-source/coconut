import tkinter as tk
from sorter_logic import get_status

def start_gui():
    root = tk.Tk()
    root.title("🥥 Coconut Sorter Dashboard")
    root.geometry("600x400")
    root.configure(bg="#1e1e1e")

    font_big = ("Arial", 18, "bold")
    font_med = ("Arial", 14)

    lbl_coconut = tk.Label(root, fg="lime", bg="#1e1e1e", font=font_big)
    lbl_non = tk.Label(root, fg="red", bg="#1e1e1e", font=font_big)
    lbl_next = tk.Label(root, fg="orange", bg="#1e1e1e", font=font_med)
    lbl_status = tk.Label(root, fg="cyan", bg="#1e1e1e", font=font_med)

    lbl_coconut.pack(pady=10)
    lbl_non.pack(pady=10)
    lbl_next.pack(pady=10)
    lbl_status.pack(pady=20)

    def update():
        coconut, non_coconut, next_smash, status = get_status()
        lbl_coconut.config(text=f"Coconuts: {coconut}")
        lbl_non.config(text=f"Non-Coconuts: {non_coconut}")
        lbl_next.config(text=f"Next Smash: {next_smash}")
        lbl_status.config(text=f"Status: {status}")
        root.after(200, update)

    update()
    root.mainloop()

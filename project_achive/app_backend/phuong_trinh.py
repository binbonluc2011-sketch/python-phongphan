import tkinter as tk

def pt(root):
    h = root.winfo_screenheight() - 100
    w = root.winfo_screenwidth() // 2

    pt_and_kq = tk.Frame(root, height=h, bg="red")
    pt_and_kq.pack_propagate(False)

    pt_frame = tk.Frame(pt_and_kq, width=w, bg="green")
    pt_frame.pack(side="left", fill="y")
    pt_frame.pack_propagate(False)

    kq_frame = tk.Frame(pt_and_kq, width=w, color="blue")
    kq_frame.pack(fill="y", side="right")
    kq_frame.pack_propagate(False)

    root.after(3000, lambda: pt_and_kq.pack(side="bottom", fill="x"))
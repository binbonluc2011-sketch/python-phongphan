import tkinter as tk

def phuong_trinh(parent):
    # Tạo giao diện giải phương trình
    label = tk.Label(parent, text="Giao diện giải phương trình", font=("Arial", 12), bg="lightblue")
    label.pack(pady=20)

    # Ví dụ: Thêm các thành phần khác như Entry, Button
    entry = tk.Entry(parent, width=30)
    entry.pack(pady=10)

    solve_button = tk.Button(parent, text="Giải phương trình", command=lambda: print("Đang giải phương trình..."))
    solve_button.pack(pady=10)
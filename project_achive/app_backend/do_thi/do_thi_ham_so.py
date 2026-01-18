import tkinter as tk

def do_thi(parent):
    # Tạo giao diện giải đồ thị
    label = tk.Label(parent, text="Giao diện giải đồ thị", font=("Arial", 12), bg="lightblue")
    label.pack(pady=20)

    # Ví dụ: Thêm các thành phần khác như Entry, Button
    entry = tk.Entry(parent, width=30)
    entry.pack(pady=10)

    plot_button = tk.Button(parent, text="Vẽ đồ thị", command=lambda: print("Đang vẽ đồ thị..."))
    plot_button.pack(pady=10)
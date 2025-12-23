import tkinter as tk
from app_frontend import intro
from app_backend import menu

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.state("zoomed")
root.title("Project Achive - developed by Phong Phan - Early access")

# Hiển thị phần giới thiệu
intro.intro(root)

# Hiển thị menu và xử lý lựa chọn
menu.menu(root)

# Chạy vòng lặp chính của ứng dụng
tk.mainloop()
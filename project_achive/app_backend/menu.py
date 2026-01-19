import tkinter as tk
from app_backend.phuong_trinh.he_phuong_trinh import he_PT

def menu(root):
    # Tạo frame chính
    main = tk.Frame(root, height=100, bg="white")
    main.pack_propagate(False)

    # Tiêu đề chính
    main_title = tk.Label(main, text="PROJECT ACHIVE - DEVELOPED BY PHONG PHAN", font=("Arial", 15), bg="white")
    main_title.pack(side="top")

    # Tùy chọn menu
    select_option = tk.StringVar()
    select_option.set("giải phương trình")

    option = ["phương trình bậc nhất một ẩn", "phương trình bậc hai một ẩn", "hệ phương trình bậc nhất hai ẩn", "đồ thị hàm số y = ax + b (a khác 0)", "đồ thị parabol y = x² (a khác 0)"]
    option_menu = tk.OptionMenu(main, select_option, *option)
    option_menu.place(relx=0.03, rely=0.6)

    # Tạo frame để hiển thị nội dung
    content_frame = tk.Frame(root, bg="lightblue", width=400, height=300)
    content_frame.pack_propagate(False)

    # Hàm xử lý khi chọn menu
    def on_option_change(*args):
        # Xóa nội dung cũ trong content_frame
        for widget in content_frame.winfo_children():
            widget.destroy()

        selected = select_option.get()
        if selected == "hệ phương trình bậc nhất hai ẩn":
            he_PT(content_frame)  # Gọi hàm từ file phuong_trinh_v1.py
        elif selected == "giải đồ thị":
            pass # Gọi hàm từ file do_thi_v1.py

        content_frame.pack(side="top", fill="both", expand=True)

    # Liên kết sự kiện thay đổi tùy chọn
    select_option.trace("w", on_option_change)

    # Hiển thị frame chính sau 3 giây
    main.pack_forget()
    root.after(3000, lambda: main.pack(side="top", fill="x"))

    return select_option
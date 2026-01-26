import tkinter as tk
from sympy import symbols, Eq, solve, sympify

from app_backend.phuong_trinh import phuong_trinh_bac_hai

x = symbols("x")

def PT_bac_nhat(parent):
    #tạo frame phương trình bậc nhất
    pt_bac_nhat = tk.Frame(parent, width=parent.winfo_screenwidth()/2, bg="white")
    pt_bac_nhat.pack(side="left", fill="y")
    pt_bac_nhat.pack_propagate(False)
    #tạo tạo title phương trình bậc nhất
    pt_title = tk.Label(pt_bac_nhat, text="PHƯƠNG TRÌNH BẬC NHẤT", font=("Arial", 16), bg="white")
    pt_title.pack(side="top")
    #tạo label phương trình bậc nhất
    pt_label = tk.Label(pt_bac_nhat, text="Phương trình bậc nhất một ẩn, có dạng : ax + b = 0", font=("Arial", 13), bg="white")
    pt_label.place(relx=0.1, rely=0.1)
    #tạo label input cho phương trình
    input_pt = tk.Label(pt_bac_nhat, text="Nhập phương trình: ", font=("Arial", 11), bg="white")
    input_pt.place(relx=0.1, rely=0.15)
    #tạo entry cho phương trình
    entry_pt = tk.Entry(pt_bac_nhat, width=30)
    entry_pt.place(relx=0.32, rely=0.15)
    #tạo button submit
    button = tk.Button(pt_bac_nhat, text="SUBMIT", font=("Arial", 13), bg="white", command=lambda: button_cliked())
    button.place(relx=0.4, rely=0.2)
    #tạo màn hình trả về
    awnser_screen = tk.Frame(parent, width=parent.winfo_screenwidth()/2, bg="lightblue")
    awnser_screen.pack(side="right", fill="both", expand=True)
    awnser_screen.pack_propagate(False)
    awnser_title = tk.Label(awnser_screen, text="AWNSER SCREEN", font=("Arial", 16), bg="white")
    awnser_title.pack(side="top")
    def button_cliked():
        try:
            phuong_trinh = entry_pt.get()
            left,right = phuong_trinh.split("=")
            left_real = sympify(left)
            right_real = sympify(right)
            pt = Eq(left_real,right_real)
            n0 = solve(pt, x)

            if len(n0) == 0:
                vo_n0 = tk.Label(awnser_screen, text="Phương trình vô nghiệm", font=("Arial", 11), bg="white")
                vo_n0.place(relx=0.1, rely=0.1)
            else:
                co_n0 = tk.Label(awnser_screen, text=f"Phương trình có nghiệm là: {n0[0]}", font=("Arial", 11), bg="white")
                co_n0.place(relx=0.1, rely=0.1)
        except:
            syntax_error = tk.Label(awnser_screen, text="SYNTAX ERROR", font=("Arial", 11), color="red", bg="white")
            syntax_error.place(relx=0.1, rely=0.1)

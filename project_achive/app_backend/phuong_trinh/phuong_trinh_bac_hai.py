import tkinter as tk
from sympy import symbols, Eq, solve, sympify

root = tk.Tk()
root.state("zoomed")

x = symbols("x")


def PT_bac_hai():
    #tạo frame phương trình bậc hai
    pt_bac2 = tk.Frame(root, width=root.winfo_screenwidth()/2, bg="white")
    pt_bac2.pack(side="left", fill="y")
    pt_bac2.pack_propagate(False)
    #tạo title phương trình
    bac2_title = tk.Label(pt_bac2, text="PHƯƠNG TRÌNH BẬC HAI", font=("Arial", 16))
    bac2_title.pack(side="top")
    #tạo label phương trình
    ptrinh_label = tk.Label(pt_bac2, text="phương trình bậc hai một ẩn: ax² + bx + c = 0, a khác 0", font=("Arial", 13))
    ptrinh_label.place(relx=0.1, rely=0.1)
    #tạo input phương trình
    ptrinh_input = tk.Label(pt_bac2, text="nhập phương trình: ", font=("Arial", 11))
    ptrinh_input.place(relx=0.1, rely=0.15)
    ptrinh_entry = tk.Entry(pt_bac2, width=35)
    ptrinh_entry.place(relx=0.31, rely=0.15)
    #tạo button submit
    button = tk.Button(pt_bac2, text="SUBMIT", font=("Arial", 11), command=lambda:button_clicked())
    button.place(relx=0.4, rely=0.2)

    #tạo màn hình trả về
    awnser_frame = tk.Frame(root, width=root.winfo_screenwidth()/2, bg="lightblue")
    awnser_frame.pack(side="left", fill="y")
    #tạo hàm button trả về
    def button_clicked():
        phuong_trinh = ptrinh_entry.get()
        phuong_trinh = phuong_trinh.replace("^", "**")
        left,right = phuong_trinh.split("=")
        ptrinh = sympify(left) - sympify(right)
        n0 = solve(ptrinh, x)

        if len(n0) == 0:
            vo_n0 = tk.Label(awnser_frame, text="Phương trình vô nghiệm", font=("Arial", 13))
            vo_n0.place(relx=0.1, rely=0.1)
        elif len(n0) == 1:
            n0_kep = tk.Label(awnser_frame, text=f"Phương trình có nghiệm kép x1 = x2 = {n0[0]}", font=("Arial", 13))
            n0_kep.place(relx=0.1, rely = 0.1)
        elif len(n0) == 2:
            n0_phanbiet = tk.Label(awnser_frame, text="Phương trình có 2 nghiệm phân biệt:", font=("Arial", 13))
            n0_phanbiet.place(relx=0.1, rely=0.1)
            x1 = tk.Label(awnser_frame, text=f"x1 = {n0[0]}, x2 = {n0[1]}")
            x1.place(relx=0.1, rely=0.2)
PT_bac_hai()
root.mainloop()
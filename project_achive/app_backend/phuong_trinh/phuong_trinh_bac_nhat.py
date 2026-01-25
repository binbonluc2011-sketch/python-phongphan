import tkinter as tk
from sympy import symbols, Eq, solve

root = tk.Tk()
root.state("zoomed")

x = symbols("x")

def PT_bac_nhat():
    #tạo frame phương trình bậc nhất
    pt_bac_nhat = tk.Frame(root, width=root.winfo_screenwidth()/2, bg="lightblue")
    pt_bac_nhat.pack(side="left", fill="y")
    #tạo tạo title phương trình bậc nhất
    pt_title = tk.Label(pt_bac_nhat, text="PHƯƠNG TRÌNH BẬC NHẤT", font=("Arial", 16), bg="white")
    pt_title.place(relx=0.5)
    #tạo label phương trình bậc nhất

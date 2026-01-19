import tkinter as tk
from sympy import symbols, sympify, solve


x,y = symbols("x y")

def he_PT(parent):
    #tạo ra màn hình chứa hệ phương trình
    he_phuong_trinh = tk.Frame(parent, width=parent.winfo_screenwidth()/2, bg="white")
    he_phuong_trinh.pack(side="left", fill="y")
    he_phuong_trinh.pack_propagate(False) #ngăn không cho wiget tự động co lại
    #tạo title
    top_title = tk.Label(he_phuong_trinh, text="HỆ PHƯƠNG TRÌNH", font=("Arial", 16))
    top_title.place(relx=0.5)
    #tạo title cho phương trình 1:
    ptrinh1 = tk.Label(he_phuong_trinh, text="phương trình 1: ax + by = c hoặc ax - by = c", font=("Arial", 13))
    ptrinh1.place(relx=0.1, rely=0.1)
    #tạo label cho nhập phương trình 1:
    ptrinh1_label = tk.Label(he_phuong_trinh, text="nhập phương trình:", font=("Arial", 11))
    ptrinh1_label.place(relx=0.1, rely=0.15)
    #tạo entry phương trình 1:
    ptrinh1_entry = tk.Entry(he_phuong_trinh, width=30)
    ptrinh1_entry.place(relx=0.31, rely=0.15)    
    #tạo title cho phương trình 2
    ptrinh2 = tk.Label(he_phuong_trinh, text="phương trình 2: a'x + b'y = c hoặc a'x - b'y = c'", font=("Arial", 13))
    ptrinh2.place(relx=0.1, rely=0.2)
    #tạo label cho phương trình 2:
    ptrinh2_label = tk.Label(he_phuong_trinh, text="nhập phương trình:", font=("Arial", 11))
    ptrinh2_label.place(relx=0.1, rely=0.25)
    #tạo entry cho phương trình 2:
    ptrinh2_entry = tk.Entry(he_phuong_trinh, width=30)
    ptrinh2_entry.place(relx=0.31, rely=0.25)
    #tạo button submit
    submit_button = tk.Button(he_phuong_trinh, text="SUBMIT", command=lambda: button_submit())
    submit_button.place(relx=0.5, rely=0.3)

    #tạo awnser screen
    awnser_screen = tk.Frame(parent, width= parent.winfo_screenwidth()/2, bg="lightblue")
    awnser_screen.pack(side="right", fill="y")
    awnser_title = tk.Label(awnser_screen, text="AWNSER_SCREEN", font=("Arial", 16))
    awnser_title.place(relx=0.5)
    #tạo hàm giải toán
    def button_submit():
        try:
            for wiget in awnser_screen:
                wiget.destroy()

            pt1 = ptrinh1_entry.get()
            pt2 = ptrinh2_entry.get()
            
            left1, right1 = pt1.split("=")
            left2, right2 = pt2.split("=")
            
            eq1 = sympify(left1) - sympify(right1)
            eq2 = sympify(left2) - sympify(right2)
            
            result = solve([eq1, eq2], [x, y])

            x_real = result[x]
            y_real = result[y]
            x_awnser = tk.Label(awnser_screen, text=f"x có nghiệm là {x_real}", font=("Arial", 11))
            x_awnser.place(relx=0.1, rely=0.2)
            y_awnser = tk.Label(awnser_screen, text=f"y có nghiệm là {y_real}", font=("Arial", 11))
            y_awnser.place(relx=0.1, rely=0.25)
        except:
            syntax_error = tk.Label(awnser_screen, text="syntax error")
            syntax_error.place(relx=0.1, rely=0.1)


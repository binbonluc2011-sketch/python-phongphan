import tkinter as tk



def do_thi(parent):
    #tạo đồ thị screen
    dothi_screen = tk.Frame(parent, width=parent.winfo_screenwidth()/2, bg="white")
    dothi_screen.pack(side="left", fill="y")
    dothi_screen.pack_propagate(False)
    #tạo title
    dothi_title = tk.Label(dothi_screen, text="ĐỒ THỊ HÀM SỐ BẬC NHẤT", font=('Arial',16), bg='white')
    dothi_title.pack(side="top")
    #tạo label
    dothi_label = tk.Label(dothi_screen, text="Đồ thị hàm số y = ax + b(a ≠ 0)", font=("Arial", 13), bg="white")
    dothi_label.place(relx=0.1, rely=0.15)
    #tạo input a
    input_a = tk.Label(dothi_screen, text="Nhập a: ", font=("Arial", 11), bg="white")
    input_a.place(relx=0.1, rely=0.2)
    entry_a = tk.Entry(dothi_screen, width=10)
    entry_a.place(relx=0.2, rely=0.2)
    #tạo input b
    input_b = tk.Label(dothi_screen, text="Nhập b: ", font=("Arial", 11), bg="white")
    input_b.place(relx=0.1, rely=0.25)
    entry_b = tk.Entry(dothi_screen, width=10)
    entry_b.place(relx=0.2, rely=0.25)
    #tạo button 
    button = tk.Button(dothi_screen, text="SUBMIT", font=("Arial", 11), bg="white", command=lambda: button_clicked())
    button.place(relx=0.25, rely=0.3)
    #tạo awnser screen
    awnser_screen = tk.Frame(parent, width=parent.winfo_screenwidth()/2, bg="lightblue")
    awnser_screen.pack(side="right", fill="y")
    awnser_screen.pack_propagate(False)
    awnser_title = tk.Label(awnser_screen, text="AWNSER SCREEN", font=("Arial", 16), bg="white")
    awnser_title.pack(side="top")
    #tạo hàm button clicked
    def button_clicked():
        a = entry_a.get()
        b = entry_b.get()

        try:
            if a == 0:
                pt_error = tk.Label(awnser_screen, text="Phương trình lỗi", font=("Arial", 13), bg="white")
                pt_error.place(relx=0.1, rely=0.1)
            else:
                pos1 = ()
                pos1 += (0,)
                pos1 += (b,)
                output_pos1 = tk.Label(awnser_screen, text=f"với x = 0, ta có y = {b}, được điểm ({pos1})", font=("Arial", 11), bg="white")
                output_pos1.place(relx=0.1, rely=0.1)
                pos2 = ()
                pos2 += (-b/a,)
                pos2 += (0,)
                x = -b / a
                output_pos2 = tk.Label(awnser_screen, text=f"với y = o, ta có y = {x}, được điểm ({pos2})", font=("Arial", 11), bg="white")

        except:
            syntax_error = tk.Label(awnser_screen, text="SYNTAX ERROR", font=("Arial", 11), bg="white")

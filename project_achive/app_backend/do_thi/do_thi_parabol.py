import tkinter as tk

def parabol(parent):
     #tạo frame parabol
     dt_parabol = tk.Frame(parent, width=parent.winfo_screenwidth()/2, bg="lightblue")
     dt_parabol.pack(side="left", fill="y")
     dt_parabol.pack_propagate(False)
     #tạo title
     parabol_title = tk.Label(dt_parabol, text="ĐỒ THỊ PARABOL", font=("Arial", 16), bg="white")
     parabol_title.pack(side="top")
     #tạo label
     parabol_label = tk.Label(dt_parabol, text="Đồ thị parabol y = ax²(a ≠ 0)", font=("Arial", 13), bg="white")
     parabol_label.place(relx=0.1, rely=0.1)
     #tạo input a
     input_a = tk.Label(dt_parabol, text="Nhập a: ", font=("Arial", 11), bg="white")
     input_a.place(relx=0.1, rely=0.15)
     #entry a
     entry_a = tk.Entry(dt_parabol, width=10)
     entry_a.place(relx=0.2, rely=0.15)
     #tạo button
     submit = tk.Button(dt_parabol, text="SUBMIT", font=("Arial", 11), command=lambda: button_clicked())
     submit.place(relx=0.25, rely=0.2)
     #tạo awnser frame
     awnser_screen = tk.Frame(parent, wid=parent.winfo_screenwidth()/2, bg="white")
     awnser_screen.pack(side="right", fill="y")
     awnser_screen.pack_propagate(False)
     awnser_title = tk.Label(awnser_screen, text="AWNSER SCREEN", font=("Arial", 16), bg="white")
     awnser_title.pack(side="top")
     #tạo hàm def button clicked
     def button_clicked():
          try:
               a = entry_a.get()
               y1 = -3*a
               p1 = ()
               p1 += (-2,)
               p2 = ()
               p2 += (-1,)
               p3 = ()
               p3 += (0,)
               p4 = ()
               p4 += (1,)
               p5 = ()
               p5 += (2,)
               if a == 0:
                    pt_error = tk.Label(awnser_screen, text="Phương trình lỗi, a phải khác 0z", font=("Arial", 11), bg="white")
                    pt_error.place(relx=0.1, rely=0.1)
               else:
                    

          except:
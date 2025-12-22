import tkinter as tk

def menu(root):
    main = tk.Frame(root, height=100, bg="white")
    main.pack_propagate(False)

    main_title = tk.Label(main, text="PROJECT ACHIVE - DELEVOPED BY PHONG PHAN", font=("Arial", 15), bg="white")
    main_title.pack(side="top")

    select_option = tk.StringVar()
    select_option.set("giải phương trình")

    option = ["giải phương trình", "giải đồ thị"]
    
    option_menu = tk.OptionMenu(main, select_option, *option)
    option_menu.place(relx=0.03, rely=0.6)

    main.pack_forget()
    root.after(3000, lambda: main.pack(side="top", fill="x"))

    return select_option
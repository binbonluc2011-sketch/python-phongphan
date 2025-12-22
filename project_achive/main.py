import tkinter as tk
from app_frontend import intro
from app_backend import menu, phuong_trinh

root = tk.Tk()
root.state("zoomed")
root.title("Project Achive - developed by Phong Phan - Early access")

intro.intro(root)
a = menu.menu(root)

if a == "giải phương trình":
    phuong_trinh.pt(root)
elif a == "giải đồ thị":
    pass
tk.mainloop()
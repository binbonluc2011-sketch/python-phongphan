from PIL import Image, ImageTk
import tkinter as tk

img = Image.open("app_frontend/image/intro.jpg")

def intro(parent):
    intro_frame = tk.Frame(parent, bg="white")
    intro_frame.pack(fill="both", expand=True)
    intro_frame.lift()

    photo = ImageTk.PhotoImage(img)
    photo.image = photo
    import_image = tk.Label(intro_frame, image=photo, bd=0)
    import_image.place(relx=0.5, rely=0.5, anchor="center")

    parent.after(3000, intro_frame.destroy)
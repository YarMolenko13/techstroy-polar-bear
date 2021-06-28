from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from main import *

root = Tk()
root.configure(background = "#B0BA84")
root.title('Polar bear')
# root.geometry("550x300+500+350")
root.geometry("200x70+650+300")
root.resizable(width=True, height=True)

def open_img():
    filename = filedialog.askopenfilename(title='open')
    img = Image.open(filename)
    root.geometry("700x550+390+100")
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img, pady=40)
    panel.image = img
    panel.pack()

btn = Button(root, text="Выбери фото", bg="#266E67", fg="#fff", command=open_img).pack(pady=20)

root.mainloop()

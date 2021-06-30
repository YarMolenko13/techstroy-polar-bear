from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk
from main import *

# style = Style()
# style.configure("BW.Tlabel", foreground=)

root = Tk()
root.configure(background="#B0BA84")
root.title('Polar bear')
# root.geometry("550x300+500+350")
root.geometry("300x70+650+300")
root.resizable(width=True, height=True)


def open_img():
    filename = filedialog.askopenfilename(title='open')
    # foldername = filedialog.askdirectory(title='open')
    # print(foldername)
    img = Image.open(filename)
    root.geometry("700x570+390+100")
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img, padding=(0,10,0,0), background="#B0BA84")
    panel.image = img
    panel.pack()

def open_folder():
    filename = filedialog.askopenfilename(title='open')

# btn = Button(root, text="Выбери фото", bg="#266E67", fg="#fff", command=open_img)
frame_btn = Label(root, background="#B0BA84")
# frame_btn.configure(bg="#B0BA84", pady=20)
frame_btn.pack(pady=20)

btn = Button(frame_btn, text="Выберите фото", command=open_img)
btn2 = Button(frame_btn, text="Выберите папку", command=open_folder)
empty = Label(frame_btn, background="#B0BA84", width=5)
btn.pack(side="left")
empty.pack(side="left")
btn2.pack(side="right")


root.mainloop()

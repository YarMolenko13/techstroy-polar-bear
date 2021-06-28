from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from main import *

orig_photo_dir = 'D:/Projects/Python/PolarBear/img/test.png'

root = Tk()
root.configure(background = "#B0BA84")
root.title('Polar bear')
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

# button = Button(root, text="Выбери фото", )
# button.grid(column=0, row=0)
#
# root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

btn = Button(root, text='open image', command=open_img).pack()

root.mainloop()

root.mainloop()


# window = Tk()
# window.configure(background = "#B0BA84")
# window.title('Polar bear')
# window.geometry('300x300')
#
# img = ImageTk.PhotoImage(Image.open(orig_photo_dir))
# panel = Label(window, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")
#
# # def ask_open():
# #     orig_photo_dir = filedialog.askopenfilename(filetypes = (("Photo files", "*.png *.gif *.jpg *.jpeg"),("Png","*.png")))
# #     print(orig_photo_dir)
# #     # img = ImageTk.PhotoImage(Image.open(orig_photo_dir))
# #     # print(img)
# #     # panel = Label(window, image=img)
# #     # panel.pack(side="bottom", fill="both", expand="yes")
# #
# #     # canvas =
#
#
#
# btn = Button(window, text="Выбери фото", bg="#266E67", fg="#fff")
# btn.pack(side="bottom")
#
#
#



# lbl = Label(window, text="Привет", font=("Arial Bold", 24, "normal"), background = "#B0BA84", fg="#fff", padx=5, pady=5)
# lbl.pack(side="bottom", fill="both", expand="yes")
# lbl.grid(column=0, row=0)

# img = ImageTk.PhotoImage(Image.open(path))
# panel = Label(window, image=img)
# panel.pack(side="bottom", fill="both", expand="yes")

# print(find_bear('asf'))

# def ask_open():
#     photo_dir = filedialog.askopenfilename(filetypes = (("Photo files", "*.png *.gif *.jpg *.jpeg"),("Png","*.png")))
#     lbl.configure(text=photo_dir)
#     img_window = Tk()
#     # canvas = Canvas(img_window, height=400, width=700)
#     # image = Image.open(photo_dir)
#     # photo = ImageTk.PhotoImage(image)
#     # image = canvas.create_image(0, 0, anchor='nw', image=photo)
#     # # canvas.grid(row=2, column=1)
#
    # img = ImageTk.PhotoImage(Image.open(photo_dir))
    # panel = Label(img_window, image = img)
    # panel.pack(side="bottom", fill="both", expand="yess")
#     img_window.mainloop()

# btn = Button(window, text="Выбери фото", bg="#266E67", fg="#fff", command=ask_open)
# btn.configure(padx=5, pady=5)
# btn.grid(column=0, row=1)
# btn.grid(column=0, row=1)


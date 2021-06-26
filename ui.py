from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

path = 'D:/Projects/Python/PolarBear/img/test.png'


window = Tk()
window.configure(background = "#B0BA84")
window.title('Polar bear')
window.geometry('300x300')

lbl = Label(window, text="Привет", font=("Arial Bold", 24, "normal"), background = "#B0BA84", fg="#fff", padx=5, pady=5)
lbl.pack(side="bottom", fill="both", expand="yes")
# lbl.grid(column=0, row=0)

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

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

photo_dir = ''

window.mainloop()

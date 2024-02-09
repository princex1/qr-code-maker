from pyqrcode import create
from tkinter import *

root = Tk()
root.title("qr code generator")
root.geometry("500x500")
root.config(bg="white")
input_text = Entry(bg="light blue")


def make_qr():
    global get
    get = input_text.get()
    if get == "":
        img_view.config(text="*text not be blank", fg="red", font="w 10 bold")
        print("text not be blank")
    else:
        get = create(get)
        scale = get.xbm(scale=5)
        global image_row
        image_row = BitmapImage(data=scale, foreground="black")
        img_view.config(image=image_row)


title = Label(text="qr code generator", font="a 15 bold", bg="white")
input_text_l = Label(text="enter qr code text:", bg="white")
make_button = Button(text="make qr code", command=make_qr)
img_view = Label(bg="white")

title.grid(row=0, column=2)
input_text_l.grid(row=1, column=1)
make_button.grid(row=3, column=2)
img_view.grid(row=2, column=2)
input_text.grid(row=1, column=2)

mainloop()

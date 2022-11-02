import tkinter
from PIL import Image,ImageTk,ImageDraw
from main import *


def image_file():
    file=tkinter.filedialog.askopenfile(mode="rb",filetypes=[('JPG File', '*.jpg'),('PNG File','*./png')])
    if file is not None:
        file.save('user_image.jpg')
    else:
        tkinter.messagebox.showerror('Upload error','No such file found')




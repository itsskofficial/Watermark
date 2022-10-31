import tkinter
from tkinter import filedialog
from tkinter import messagebox


def image_file():
    file=filedialog.askopenfile(mode="rb",filetypes=[('JPG File', '*.jpg'),('PNG File','*./png')])
    if file is not None:
        img=file.read()
    else:
        messagebox.showerror('Upload error','No such file found')
import tkinter
from tkinter import filedialog


def image_file():
    file=filedialog.askopenfile(mode="rb",filetypes=[('JPG File', '')])
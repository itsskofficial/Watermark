import tkinter
from PIL import Image, ImageTk
from utils import *

screen = tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas = tkinter.Canvas(screen, height=100, width=100, bg="black")
canvas.place(x=200, y=50)
logo=Image.open("./logo.jpg")
resized_logo=logo.resize((100,100),Image.ANTIALIAS)
new_logo=ImageTk.PhotoImage(image=resized_logo)
canvas.create_image(0, 0, image=new_logo, anchor=tkinter.NW)
label = tkinter.Label(screen, text="Get your image watermarked", font=())
label.place(x=185, y=200)

button=tkinter.Button(screen,text="Upload image",command=image_file)

screen.mainloop()

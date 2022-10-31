from io import BytesIO
import tkinter
from tkinter import NW, messagebox
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from numpy import rint

def image_file():
    file=askopenfile(mode="rb",filetypes=[('JPG File', '*.jpg'),('PNG File','*.png')])
    if file is not None:
        img_bytes=file.read()
        stream = BytesIO(img_bytes)
        stream.close()
        print(img)
        watermark_page(img)
    else:
        messagebox.showerror('Upload error','No such file found')

def watermark_page(img):
    global canvas1
    global label1
    global button1
    canvas1.destroy()
    label1.destroy()
    button1.destroy()
    canvas2 = tkinter.Canvas(screen, height=300, width=300, bg="black")
    canvas2.place(x=100, y=50)
    resized_img=img.resize((300,300),Image.ANTIALIAS)
    new_img=ImageTk.PhotoImage(image=resized_img)
    print(new_img)
    canvas2.create_image(0,0,image=new_img,anchor=tkinter.NW)

screen = tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas1 = tkinter.Canvas(screen, height=100, width=100, bg="black")
canvas1.place(x=200, y=50)
logo=Image.open("./logo.jpg")
resized_logo=logo.resize((100,100),Image.ANTIALIAS)
new_logo=ImageTk.PhotoImage(image=resized_logo)
canvas1.create_image(0, 0, image=new_logo, anchor=tkinter.NW)
label1 = tkinter.Label(screen, text="Get your image watermarked", font=('Montserrat 10 bold'))
label1.place(x=155, y=200)
button1=tkinter.Button(screen,text="Upload image",command=image_file)
button1.place(x=205,y=250)
screen.mainloop()
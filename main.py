from io import BytesIO
import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

def image_file():
    file=askopenfile(mode="rb",filetypes=[('JPG File', '*.jpg'),('PNG File','*.png')])
    if file is not None:
        img_bytes=file.read()
        stream = BytesIO(img_bytes)
        img = Image.open(stream).convert("RGBA")
        stream.close()
        image=ImageTk.PhotoImage(image=img)
        # img=Image.open(img_bytes)
        # img.show()
    else:
        messagebox.showerror('Upload error','No such file found')

screen = tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas = tkinter.Canvas(screen, height=100, width=100, bg="black")
canvas.place(x=200, y=50)
logo=Image.open("./logo.jpg")
resized_logo=logo.resize((100,100),Image.ANTIALIAS)
new_logo=ImageTk.PhotoImage(image=resized_logo)
canvas.create_image(0, 0, image=new_logo, anchor=tkinter.NW)
label = tkinter.Label(screen, text="Get your image watermarked", font=('Montserrat 10 bold'))
label.place(x=155, y=200)
button=tkinter.Button(screen,text="Upload image",command=image_file)
button.place(x=205,y=250)

def watermark_page(img):
    canvas.destroy()
    label.destroy()
    button.destroy()
    canvas = tkinter.Canvas(screen, height=100, width=100, bg="black")
    canvas.place(x=200, y=50)
    user_image=ImageTk.PhotoImage(img)
    

screen.mainloop()

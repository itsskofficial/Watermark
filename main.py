from re import X
import tkinter

screen=tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas=tkinter.Canvas(screen,height=100,width=100,bg="black")
canvas.place(x=200,y=50)
logo=tkinter.PhotoImage(file="./logo.jpg")
canvas.create_image(image=logo)
label=tkinter.Label(screen,text="Upload your image below")
label.place(x=185,y=200)

screen.mainloop()

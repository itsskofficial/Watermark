import tkinter

screen=tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas=tkinter.Canvas()
label=tkinter.Label(screen,text="Welcome")
label.grid(row=0,column=1)
screen.mainloop()

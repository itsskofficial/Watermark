import tkinter

screen=tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas=tkinter.Canvas(screen,height=100,width=100,bg="black")
canvas.grid(row=0,column=1)
label=tkinter.Label(screen,text="Welcome")
label.grid(row=1,column=1)
screen.mainloop()

import tkinter

screen=tkinter.Tk()
screen.title("Watermark")
screen.geometry("500x500")
canvas=tkinter.Canvas(screen,height=200,width=300,bg)
label=tkinter.Label(screen,text="Welcome")
label.grid(row=0,column=1)
screen.mainloop()

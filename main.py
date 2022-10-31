import tkinter

screen=tkinter.Tk()
screen.geometry("500x500")
label=tkinter.Label(screen,text="Hello")
label.grid(row=0,column=0)
screen.mainloop()

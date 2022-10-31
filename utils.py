import tkinter



def image_file():
    file=tkinter.filedialog.askopenfile(mode="rb",filetypes=[('JPG File', '*.jpg'),('PNG File','*./png')])
    if file is not None:
        img=file.read()
    else:
        tkinter.messagebox.showerror('Upload error','No such file found')

def watermark_image(img):
    base=img.convert("RGBA")
    text=image

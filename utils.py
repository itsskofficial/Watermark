import tkinter
from PIL import Image,ImageTk,ImageDraw


def image_file():
    file=tkinter.filedialog.askopenfile(mode="rb",filetypes=[('JPG File', '*.jpg'),('PNG File','*./png')])
    if file is not None:
        img=file.read()
    else:
        tkinter.messagebox.showerror('Upload error','No such file found')

def watermark_image(img):
    base=img.convert("RGBA")
    text=Image.new("RGBA",base.size,(255,255,255,0))
    d=ImageDraw.Draw(text)
    d.text((0,0),"SK",font="Arial",fill=(255,255,255,128))

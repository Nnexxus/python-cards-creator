import tkinter
from PIL import Image,ImageTk
from sys import argv

root = tkinter.Tk()
root.title("Image Preview")
label = tkinter.Label(root)
label.pack()
img = None
tkimg = [None]  # This, or something like it, is necessary because if you do not keep a reference to PhotoImage instances, they get garbage collected.

filename = argv[-1]

delay = 500   # in milliseconds
def loopCapture():
    img = Image.open(filename)
    tkimg[0] = ImageTk.PhotoImage(img)
    label.config(image=tkimg[0])
    root.update_idletasks()
    root.after(delay, loopCapture)

loopCapture()
root.mainloop()

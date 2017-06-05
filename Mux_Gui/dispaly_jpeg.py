'''
Created on Jun 4, 2017
http://www.python-course.eu/tkinter_labels.php
https://stackoverflow.com/questions/19532125/cant-install-pil-after-mac-os-x-10-9

sudo pip install pillow
Try this to check it:

from PIL import Image
image = Image.open("file.jpg")
image.show()

@author: rduvalwa2
'''
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("/Users/rduvalwa2/git/Mux/AlbumCovers/52nd Street.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
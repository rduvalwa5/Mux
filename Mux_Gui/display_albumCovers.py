'''
Created on Jun 7, 2017
http://www.python-course.eu/tkinter_labels.php
https://stackoverflow.com/questions/19532125/cant-install-pil-after-mac-os-x-10-9

@author: rduvalwa2
'''
from tkinter import *
from PIL import ImageTk, Image
import os


def get_albums():
        albums = []
        base =   "/Users/rduvalwa2/Music/Album Covers"
        for root, _, files in os.walk(base):
            for file in files:
                albums.append(base + "/" + file)
        return  albums

def display_albums():
    f = get_albums()
    for x in f:
# if "blah" not in somestring: 
        if ".DS_Store" not in x:
            root = Tk()
            img = ImageTk.PhotoImage(Image.open(x))
            panel = Label(root, image = img)
            panel.pack(side = "bottom", fill = "both", expand = "yes")
            root.mainloop()


if __name__  == '__main__':
    display_albums()
#    x = get_albums()
#    for f in x:
#        print(f)
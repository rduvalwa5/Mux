#!/usr/bin/env python

"""This is a small script to demonstrate using Tk to show PIL Image objects.
The advantage of this over using Image.show() is that it will reuse the
same window, so you can show multiple images without opening a new
window for each image.

This will simply go through each file in the current directory and
try to display it. If the file is not an image then it will be skipped.
Click on the image display window to go to the next image.

Noah Spurrier 2007
"""

import os, sys
import tkinter
from PIL import ImageTk, Image
from tkinter import Toplevel

base = '/Users/rduvalwa2/Music/Album Covers/'
dirlist = os.listdir('/Users/rduvalwa2/Music/Album Covers')


#This creates the main window of an application
window = tkinter.Tk()
window.title("Album Cover")
window.geometry("1000x1000")
window.configure(background='grey')

path = base + dirlist[1]

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tkinter.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()
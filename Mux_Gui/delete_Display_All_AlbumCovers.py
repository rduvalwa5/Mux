'''
http://code.activestate.com/recipes/521918-pil-and-tkinter-to-display-images/
'''
from Music_Get_Functions import musicGet_Functions
from PIL import ImageTk, Image
import MySQLdb   as connDb
import os, sys
import tkinter


def button_click_exit_mainloop (event):
    albums = []
    base =   "/Users/rduvalwa2/Music/Album Covers"
    for root, _, files in os.walk(base):
        for file in files:
            albums.append(base + "/" + file)
    
    
    event.widget.quit() # this will cause mainloop to unblock.

    root = Tkinter.Tk()
    root.bind("<Button>", button_click_exit_mainloop)
    root.geometry('+%d+%d' % (100,100))
#    dirlist = os.listdir('.')
    old_label_image = None
#    for f in dirlist:
    try:
        for f in albums:
            print(f)
            image1 = Image.open(f)
            root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
            tkpi = ImageTk.PhotoImage(image1)
            label_image = Tkinter.Label(root, image=tkpi)
            label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])
            root.title(f)
            if old_label_image is not None:
                print("Old image not none")
                old_label_image.destroy()
                old_label_image = label_image
                root.mainloop() # wait until user clicks the window
    except Exception:
                # This is used to skip anything not an image.
                # Image.open will generate an exception if it cannot open a file.
                # Warning, this will hide other errors as well.
                pass
    
        
'''
sudo pip install pillow
Try this to check it:

from PIL import Image
image = Image.open("file.jpg")
image.show()

OSXAir:bin rduvalwa2$ sudo pip3.6 install pillow
The directory '/Users/rduvalwa2/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/rduvalwa2/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting pillow
  Downloading Pillow-4.1.1-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (3.5MB)
    100% |████████████████████████████████| 3.5MB 379kB/s 
Collecting olefile (from pillow)
  Downloading olefile-0.44.zip (74kB)
    100% |████████████████████████████████| 81kB 3.7MB/s 
Installing collected packages: olefile, pillow
  Running setup.py install for olefile ... done
Successfully installed olefile-0.44 pillow-4.1.1
OSXAir:bin rduvalwa2$ 


@author: rduvalwa2
'''
from tkinter import *
from PIL import ImageTk, Image
import os

albums = []
base =   "/Users/rduvalwa2/git/Mux/AlbumCovers"
for root, _, files in os.walk(base):
    for file in files:
        albums.append(base + "/" + file)


root = Tk()
for file in albums:
    if ".DS_Store" not in file:
        img = ImageTk.PhotoImage(Image.open(file))
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
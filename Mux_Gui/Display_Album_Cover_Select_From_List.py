'''
List of album covers
@author: rduvalwa2
/Library/Frameworks/Python.framework/Versions/3.6/bin
sudo pip3 install pillow

select
http://effbot.org/imagingbook/pil-index.htm

1) UI list of album covers
2) Select one cover 
3) Double click displays cover

'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
# from Mux_src.Music_Get_Functions import musicGet_Functions
import os, sys , platform
from PIL import Image  # , ImageTk


class displaySelectCover():
    
    def getCoverList(self):
        root = Tk()
        root.geometry("1000x500+30+30")
        albumCoverList = []
        mux = musicGet_Functions(True)
        coversIn = mux.get_all_album_covers()
        print(coversIn)
        if coversIn != []:
            for cover in coversIn:
                print("coverIn ", cover)
                albumCoverList.append((cover[0]  , cover[1], cover[2]))
        else:
            albumCoverList.append("None found!")
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        mylist = Listbox(root, yscrollcommand=scrollbar.set, width=100, selectmode=EXTENDED)

        for n in range(len(albumCoverList)):
#            item = str(albumCoverList[n][1])
            item = (str(albumCoverList[n][0]), albumCoverList[n][1], albumCoverList[n][2])
            print("print item ", item)
#            mylist.insert(END,albumCoverList[n][1])
            mylist.insert(END, item)
        mylist.insert(END, "Total Albums " + str(mylist.size()))
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)
        mylist.bind("<Double-Button-1>", self.OnDouble)
        mainloop()

    def OnDouble(self, event):
        root = Toplevel
        HOST = platform.uname().node            
        if HOST == 'osxair.local':
                base = '/Users/rduvalwa2/Documents/GitHub/Mux/AlbumCovers/'
        elif HOST == 'Macbook16.local':
                base = '/Users/rduvalwa2/Documents/GitHub/Mux/AlbumCovers/'
        else:
            base = '/Users/rduvalwa2/Documents/GitHub/Mux/AlbumCovers/'
            
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        print("print value ", value)
        print ("print selection:", selection, ": '%s" % value[1])
        imagefile = base + value[1] 
        print("cover is ", imagefile)
        image = Image.open(imagefile)
        image.show()          


if __name__ == "__main__":
    app = displaySelectCover()
    app.getCoverList()


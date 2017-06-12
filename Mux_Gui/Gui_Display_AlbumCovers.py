'''
List of album covers
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
#import mysql.connector

root = Tk()

albumCoverList = []
mux = musicGet_Functions(True)
coversIn = mux.get_all_album_covers()
print(coversIn)
if coversIn != []:
    for cover in coversIn:
        print(cover)
        albumCoverList.append((cover[2],cover[0]))
else:
    albumCoverList.append("None found!")

print(albumCoverList)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED )

for n in range(len(albumCoverList)):
    mylist.insert(END," " + str(albumCoverList[n][0]) + "  " + albumCoverList[n][1] )
mylist.insert(END,"Total Albums " + str(mylist.size()))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()
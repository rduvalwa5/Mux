'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
#from Music_Get_Functions import musicGet_Functions
from Music_Get_Functions import *
# import mysql.connector

root = Tk()

albumList = []
mux = Music_Get_Functions.musicGet_Functions()
albumsIn = mux.get_all_albums()
print(albumsIn)
if albumsIn != []:
    for album in albumsIn:
        print(album)
        albumList.append((album[0], album[1], album[2]))
else:
    albumList.append("None found!")

print(albumList)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set, width=100, selectmode=EXTENDED)

for n in range(len(albumList)):
    mylist.insert(END, " " + str(albumList[n][0]) + " | " + albumList[n][1] + " | " + albumList[n][2])
mylist.insert(END, "Total Albums " + str(mylist.size()))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()

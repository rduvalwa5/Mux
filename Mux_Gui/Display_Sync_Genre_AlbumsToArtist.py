'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
# import mysql.connector

root = Tk()

GenreSyncList = []
mux = musicGet_Functions(True)
genreSyncIn = mux.get_sync_Album_ArtistGenre()
# print(genreSyncIn)
if genreSyncIn != []:
    for result in genreSyncIn:
#        print(result)
        GenreSyncList.append(result)
else:
    GenreSyncList.append("None found!")

# print("TypeSyncList  ", TypeSyncList)
for l in GenreSyncList:
    print(l)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set, width=100, selectmode=EXTENDED, bg='yellow' , fg='red')

mylist.insert(END, " | " + "Album Album  " + "    | " + "Album  Artist  " "    | " + "Album  Genre  " + " | " + "Artist  " + " | " + "Artist Genre   ")
for n in range(len(GenreSyncList)):
    mylist.insert(END, "  " + str(n) + "  " + str(GenreSyncList[n][0]) + "  |  " + GenreSyncList[n][1] + "   |   " + GenreSyncList[n][2] + "  |  " + GenreSyncList[n][3] + "  |  " + GenreSyncList[n][4])
mylist.insert(END, "Total Diffs " + str(len(GenreSyncList)))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()

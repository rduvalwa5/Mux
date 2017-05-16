'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
#import mysql.connector

root = Tk()

songList = []
mux = musicGet_Functions()
songIn = mux.verify_normalized_table()
print(songIn)
if songIn != []:
    for song in songIn:
#        print(song)
        songList.append(song)
else:
    artistList.append("None found!")

print(songList)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'yellow' , fg = 'red')

for n in range(len(songList)):
    mylist.insert(END,str(n) + "\t  " + str(songList[n][0]) + "\t  " + songList[n][1] + "\t  " + songList[n][2] + "\t  " + songList[n][3] + "\t  " + songList[n][4] )
mylist.insert(END,"Total Songs " + str(mylist.size()))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()
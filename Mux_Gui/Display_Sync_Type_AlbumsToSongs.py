'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
#import mysql.connector

root = Tk()

TypeSyncList = []
mux = musicGet_Functions(True)
typeSyncIn = mux.get_sync_type()
# print(typeSyncIn)
if typeSyncIn != []:
    for result in typeSyncIn:
#        print(result)
        TypeSyncList.append(result)
else:
    TypeSyncList.append("None found!")

#print("TypeSyncList  ", TypeSyncList)
for l in TypeSyncList:
    print(l)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'yellow' , fg = 'red')

mylist.insert(END," | " + "Album Album  " + "    | " + "Album  Type  " + " | " + "Songs  Album  " + " | " + "songs Type   ")
for n in range(len(TypeSyncList)):
    mylist.insert(END,"  " + str(n) + "  " + str(TypeSyncList[n][0]) + "  |  " + TypeSyncList[n][1] + "   |   " + TypeSyncList[n][2] + "  |  " + TypeSyncList[n][3]+ "  |  " + TypeSyncList[n][4])
mylist.insert(END,"Total Diffs " + str(len(TypeSyncList)))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()
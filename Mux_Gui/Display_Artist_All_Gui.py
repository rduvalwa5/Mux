'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
# import mysql.connector

root = Tk()

artistList = []
mux = musicGet_Functions()
artistIn = mux.get_all_artist()
print(artistIn)
if artistIn != []:
    for artist in artistIn:
        print(artist)
        artistList.append((artist[0]))
else:
    artistList.append("None found!")

print(artistList)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set, width=100, selectmode=EXTENDED, bg='yellow' , fg='red')

for artist in mylist:
    mylist.insert(str(artist))
#    mylist.insert(END, str(n) + "  " + str(artistList[n][0])  + "  " + artistList[n][1])
mylist.insert(END, "Total Artist " + str(mylist.size()))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

mainloop()

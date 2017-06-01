'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions

root = Tk()

mux = musicGet_Functions()

table = 'Music.album2songs'
criteria = ""
totalSongs = mux.get_count(table, criteria)
print("Total songs " ,str(totalSongs))
      

tipeCountList = []


typeCounts = mux.get_all_type_count()


print(typeCounts)
if typeCounts != []:
    for tipe in typeCounts:
        print(tipe)
        tipeCountList.append((tipe[0],tipe[1]))
else:
    tipeCountList.append("None found!")

print(tipeCountList)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'black' , fg = 'yellow')

for n in range(len(tipeCountList)):
    mylist.insert(END,str(n + 1) + "  " + tipeCountList[n][0] + "  " + str(tipeCountList[n][1]))


mylist.insert(END,"Total Songs " + str(totalSongs))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()
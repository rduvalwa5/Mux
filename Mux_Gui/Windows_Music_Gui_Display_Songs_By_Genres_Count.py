'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Windows_Music_Get_Functions import musicGet_Functions

root = Tk()

mux = musicGet_Functions()

table = 'Music.album2songs'
criteria = ""
totalSongs = mux.get_count(table, criteria)
print("Total songs " ,str(totalSongs))
      

genreCountList = []


genrecounts = mux.get_all_genre_count()


print(genrecounts)
if genrecounts != []:
    for genre in genrecounts:
        print(genre)
        genreCountList.append((genre[0],genre[1]))
else:
    genreCountList.append("None found!")

print(genreCountList)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'black' , fg = 'yellow')

for n in range(len(genreCountList)):
    mylist.insert(END,str(n + 1) + "  " + genreCountList[n][0] + "  " + str(genreCountList[n][1]))


mylist.insert(END,"Total Songs " + str(totalSongs))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()
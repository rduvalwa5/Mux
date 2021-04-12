'''
Created on March 2 2017
https://www.tutorialspoint.com/python/tk_listbox.htm 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
#import mysql.connector

root = Tk()

genreList = []
mux = musicGet_Functions('isNotTest')
genresIn = mux.get_genres()
print(genresIn)
if genresIn != []:
    for genre in genresIn:
        print(genre)
        genreList.append((genre[0],genre[1]))
else:
    genreList.append("None found!")

print(genreList)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'black' , fg = 'yellow')

mylist.insert(END,"#" + "\t" + "Genre" + "\t\t\t" + "Index")
for n in range(len(genreList)):
    mylist.insert(END,str(n + 1) + "\t" + genreList[n][0] + "\t\t\t" + str(genreList[n][1]))
mylist.insert(END,"Total Genres " + str(mylist.size() - 1 ))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )



mainloop()
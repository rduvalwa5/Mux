'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions

root = Tk()

mux = musicGet_Functions()

artist = text_in.get()
songList = mux.get_artist_songs(artist)
frame = Frame()
text_in2.insert(END, artist + " songs: \n")
if songList != []:
    for song in songList:
            print(song[0])
            s = song[0]
            text_in2.insert(END, s)
else:
    text_in2.insert(END, "None found! \n") 
       
mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'yellow' , fg = 'red')
master.rowconfigure(0, weight=1)
master.columnconfigure(0, weight=1)
grid(sticky=N+S+W+E)
myButtonTxt = 'Get songs'
myButtonCmd = openHandler
Button(self,text=myButtonTxt.format(1),command=myButtonCmd).grid(row=26, column=1, sticky=E+W)

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

for n in range(len(songList)):
    mylist.insert(END,str(n) + "  " + str(songtList[n][1]) + "  " + songtList[n][0])
mylist.insert(END,"Total Artist " + str(mylist.size()))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


mainloop()

    '''
    
from tkinter import *
from Music_Get_Functions import musicGet_Functions
import MySQLdb   as connDb

 
class Application(Frame):
    def __init__(self, master=None):
        def openHandler():
            mux = musicGet_Functions()
            artist = self.text_in.get()
            try:
                songList = mux.get_artist_songs(artist)
                self.text_in2.insert(END, artist + " songs: \n")
                if songList != []:
                    for song in songList:
                        print(song[0])
                        s = song[0]
                        self.text_in2.insert(END, s)
                else:
                    self.text_in2.insert(END, "None found! \n")
            except self.conn.Error as err:
                print("Exception is ", err)
                self.text_in2.insert(END, err)
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N+S+W+E)
        myButtonTxt = 'Get songs'
        myButtonCmd = openHandler
        Button(self,text=myButtonTxt.format(1),command=myButtonCmd).grid(row=26, column=1, sticky=E+W)
        frame3 = Frame(self) 
#        frame3.grid(row=0, column=0, rowspan=14, columnspan=3, sticky=N+S+W+E)
        frame3.grid(row=0, column=0, rowspan=14, columnspan=3) #, sticky=N+S+W+E)
        entryText = "Input Artist Name"
        self.text_in = Entry(frame3)
        self.text_in.config(fg = "black")
        self.text_in.insert(0, entryText)
        self.text_in.pack(side="top",fill='both',expand=1)
        self.text_in2 = Listbox(frame3,height=25,width=100)     
        self.text_in2.pack(side='left', fill='both',expand=1)
        
root = Tk()
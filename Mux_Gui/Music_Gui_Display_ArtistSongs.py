'''
Created on March 23 2017
This code prints the songs by an artist
@author: rduvalwa2
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
app = Application(master=root)                
app.mainloop()
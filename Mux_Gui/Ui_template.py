'''
Created on Feb 12, 2021

@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
# import MySQLdb   as connDb
import pymysql.cursors

 
class Application(Frame):

    def __init__(self, master=None):

        def frame1ClickHandler(event):
            print("Frame 1", event.x, event.y)

        def frame2ClickHandler(event):
            print("Frame 2", event.x, event.y)

        def openHandler():
            mux = musicGet_Functions(True)
            album_name = self.text_in.get()
            print("Input Album: ", album_name)
            try:
                songList = mux.get_album_songs(album_name)
                self.text_in2.insert(END, album_name + " songs: \n")
                if songList != []:
                    for song in songList:
                        print(song[0])
                        print("\n") 
                        s = song[0]
                        self.text_in2.insert(END, s)
                        self.text_in2.insert(END, "\n")
                else:
                    self.text_in2.insert(END, "None found! \n")                
            except self.conn.Error as err:
                print("Exception is ", err)
                self.text_in2.insert(END, err)

        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N + S + W + E)
        for r in range(14):
            self.rowconfigure(r, weight=1)
            if r == 7:
                Label(self, text="".format(r)).grid(row=r, column=3)
            else:
                Label(self, text="".format(r)).grid(row=r, column=0)
        self.rowconfigure(5, weight=1)
        myButtonTxt = 'Get songs'
        quitButtonTxt = 'Quit'
        myButtonCmd = openHandler
        Button(self, text=myButtonTxt.format(1), command=myButtonCmd).grid(row=14, column=0, sticky=E + W)
        Button(self, text=quitButtonTxt.format(1), command=self.quit).grid(row=14, column=2, sticky=E + W)
        frame3 = Frame(self) 
        frame3.grid(row=0, column=0, rowspan=14, columnspan=3, sticky=N + S + W + E)
        entryText = "Input Album Name"
        self.text_in = Entry(frame3)
        self.text_in.config(fg="black")
        self.text_in.insert(0, entryText)
        self.text_in.pack(side="top", fill='both', expand=1)
        self.text_in2 = Text(frame3)
        self.text_in2.pack(side='left', fill='both', expand=1)


root = Tk()
app = Application(master=root)                
app.mainloop()

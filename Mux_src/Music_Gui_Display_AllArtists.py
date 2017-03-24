'''
Created on March 23 2017
This code prints the songs in the album 
@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
import mysql.connector

 
class Application(Frame):
    def __init__(self, master=None):
        def frame1ClickHandler(event):
            print("Frame 1", event.x, event.y)
        def frame2ClickHandler(event):
            print("Frame 2", event.x, event.y)
        def makeRed():
            self.text_in2.config(fg = "red")
        def makeBlue():
            self.text_in2.config(fg = "blue")
        def makeGreen():
            self.text_in2.config(fg = "green")
        def makeBlack():
            self.text_in2.config(fg = "black")
        def openHandler():
            mux = musicGet_Functions()
 #           artist = self.text_in.get()
            try:
                artistList = mux.get_all_artist()
                self.text_in2.insert(END," All artist: \n")
                if artistList != []:
                    for artist in artistList:
                        print(artist[0])
                        print("\n") 
                        s = artist[0]
                        self.text_in2.insert(END, s)
                        self.text_in2.insert(END, "\n")
                else:
                    self.text_in2.insert(END, "None found! \n")
            except mysql.connector.Error as err:
                print("Exception is ", err)
                self.text_in2.insert(END, err)
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N+S+W+E)
        for r in range(14):
            self.rowconfigure(r, weight=1)
            if r == 7:
                Label(self, text="".format(r)).grid(row=r, column=3)
            else:
                Label(self, text="".format(r)).grid(row=r, column=0)
        self.rowconfigure(5, weight=1)
        myButtonTxt = 'Get All Artist'
        myButtonCmd = openHandler
        Button(self,text=myButtonTxt.format(1),command=myButtonCmd).grid(row=14, column=1, sticky=E+W)
        frame3 = Frame(self) 
        frame3.grid(row=0, column=0, rowspan=14, columnspan=3, sticky=N+S+W+E)
        entryText = "Retrun All Artists"
        self.text_in = Entry(frame3)
        self.text_in.config(fg = "black")
        self.text_in.insert(0, entryText)
        self.text_in.pack(side="top",fill='both',expand=1)
        self.text_in2 = Text(frame3)
        self.text_in2.pack(side='left', fill='both',expand=1)
root = Tk()
app = Application(master=root)                
app.mainloop()
'''
Created on Feb 5, 2017

@author: rduvalwa2
'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createSongWidgets()
        
    def createSongWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.labelInput = Label(top_frame, text="Song Name")
        self.text_in = Entry(top_frame)
        self.labelResult = Label(top_frame, text="Result")
        self.labelInput.pack()
        self.text_in.pack()
        self.labelResult.pack()
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='disabled')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Submit", command=self.handle)
        self.handleb.pack(side=LEFT)
                
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        song = self.text_in.get()
        muxGet = musicGet_Functions()
        result = muxGet.get_song(song)
        if result != []:
            songs = []
            idx = 0
            for i in result:
                print(i)
                songs.append((result[idx][0],result[idx][3],result[idx][4], result[idx][5]))
                idx = idx + 1
            print(songs)            
            output = songs
        else:
            output = song + " not found"
            
 # use .config to change the state of the button           
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

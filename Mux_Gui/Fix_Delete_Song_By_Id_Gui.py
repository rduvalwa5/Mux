'''
Created on Feb 5, 2017
Saint-Saëns_ Danse Macabre
@author: rduvalwa2
'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions
import Music_Load


class Application(Frame):
    """Application main window class."""

    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createArtistWidgets()
        
    def createArtistWidgets(self):
        """Add all the widgets to the main frame."""
        
        songId_Frame = Frame(self)
        
        self.labelInputSongId = Label(songId_Frame, text="Delete Song Id")        
        self.labelResult = Label(songId_Frame, text="Result Song")
        self.text_in_SongId = Entry(songId_Frame)
        self.labelInputSongId.pack()
        self.text_in_SongId.pack()
        self.labelResult.pack()     
        songId_Frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
# how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='active')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Submit", command=self.handle)
        self.handleb.pack(side=LEFT)
                
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        songId = self.text_in_SongId.get()
        DeleteSong = musicGet_Functions(True)
        result = DeleteSong.delete_song(songId)
        print("delete result from function: ", result)
        self.labelResult.config(text=result)
        if result == None:
            print("Result Success")
            self.labelResult.config(text="Result Success")
        else:
            print(result)
            self.labelResult.config(text=result)
        
        self.QUIT.config(state='active')
        self.QUIT.pack(side=TOP)


root = Tk()
app = Application(master=root)
app.mainloop()  

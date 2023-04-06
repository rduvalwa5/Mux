'''
Created on Feb 5, 2017

Updated April 3 2023

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
        self.createArtistWidgets()
        
    def createArtistWidgets(self):
        """Add all the widgets to the main frame."""
        Artist_Frame = Frame(self)
        Genre_Frame = Frame(self)
        self.labelInputArtist = Label(Artist_Frame, text="Delete Artist Name")
        self.text_in_Artist = Entry(Artist_Frame)
        self.labelResult = Label(Artist_Frame, text="Result Artist")
        self.labelInputArtist.pack()
        self.text_in_Artist.pack()
        self.labelResult.pack()
        Artist_Frame.pack(side=TOP)
        Genre_Frame.pack(side=TOP)
        
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
        artist = self.text_in_Artist.get()
        print("delete " + artist)
        muxDeleteArtist = musicGet_Functions()
#        muxAddArtist = Music_Load.artist_Add_Update_Delete(True)
        result = muxDeleteArtist.delete_artist(artist)
        print(result)
        output = result
        self.labelResult.config(text=output)
        self.QUIT.config(state='active')
        self.QUIT.pack(side=TOP)


root = Tk()
app = Application(master=root)
app.mainloop()  

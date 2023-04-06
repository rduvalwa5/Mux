'''
Created on Feb 5, 2017

Updated April 3 2023


@author: rduvalwa2
'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions
#import Music_Load

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
        
        self.labelInputArtist = Label(Artist_Frame, text="Artist Name")
        self.labelInputGenre = Label(Genre_Frame, text="Artist Genre")
        
        self.text_in_Artist = Entry(Artist_Frame)
        self.text_in_Genre = Entry(Genre_Frame)
        
        self.labelArtistResult = Label(Artist_Frame, text="Result Artist")
#        self.labelGenreResult = Label(Genre_Frame, text="Result Genre")
        
        self.labelInputArtist.pack()
        self.labelInputGenre.pack()
        
        self.text_in_Artist.pack()
        self.text_in_Genre.pack()
        
        self.labelArtistResult.pack()
#        self.labelGenreResult.pack()
                
        Artist_Frame.pack(side=TOP)
        Genre_Frame.pack(side=TOP)
        
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
        artist = self.text_in_Artist.get()
        genre = self.text_in_Genre.get()
        print(artist  +  genre)
        muxAddArtist = musicGet_Functions()  #.artist_Add_Update_Delete(True)
        resultArtist = muxAddArtist.add_artist(artist, genre)
        print("Result " + resultArtist)
        self.labelArtistResult.config(text=resultArtist)
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

'''
Updated april 4 2023

problem thoough the delete query is good but does not disconnect if the data base
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
        
        song_Frame = Frame(self)
        album_Frame = Frame(self)
        result_Frame = Frame(self)
        
        self.labelInputSong = Label(song_Frame, text="Delete Song")  
        self.labelInputAlbum = Label(song_Frame, text="Delete Song Album")         
        self.labelResult = Label(song_Frame, text="Result Delete Song")

        self.labelInputSong.pack()
        self.text_in_Song = Entry(song_Frame)
        self.text_in_Song.pack()
        
        self.labelInputAlbum.pack()
        self.text_in_Album = Entry(album_Frame)
        self.text_in_Album.pack()

        

    
        song_Frame.pack(side=TOP)
        album_Frame.pack(side=TOP)
        
        self.labelResult.pack(side=TOP) 
        
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
        song = self.text_in_Song.get()
        album = self.text_in_Album.get()
        
        DeleteSong = musicGet_Functions()
        result = DeleteSong.delete_song(song, album)
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

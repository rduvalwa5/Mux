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
        self.createArtistWidgets()
        
    def createArtistWidgets(self):
        """Add all the widgets to the main frame."""
        tag_name = Frame(self)
        artist_name = Frame(self)
        song_name = Frame(self)
        album_name = Frame(self)
        self.labeltag = Label(tag_name, text="Update Song Artist")
        self.labelSong = Label(song_name, text="Song Name")
        self.labelAlbum = Label(album_name, text="Album Name")
        self.labelArtist = Label(artist_name, text="Artist Name")
        self.labelResult = Label(artist_name, text="Result")
                
        self.text_in_song = Entry(song_name)        
        self.text_in_album = Entry(album_name)
        self.text_in_artist = Entry(artist_name)
        
        self.labeltag.pack()
        self.labelArtist.pack()
        self.labelSong.pack()
        self.labelAlbum.pack()   
        
             
        self.text_in_song.pack()
        self.text_in_artist.pack()
        self.text_in_album.pack()
        self.labelResult.pack()  
        
        tag_name.pack(side=TOP)
        artist_name.pack(side=TOP)
        song_name.pack(side=TOP)
        album_name.pack(side=TOP) 
            
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='active')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Submit", command=self.handle)
        self.handleb.pack(side=LEFT)
                
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        artist = self.text_in_artist.get()
        song = self.text_in_song.get()
        album = self.text_in_album.get()
        update = musicGet_Functions(True)
        result = update.update_song_artist(artist,song,album)
        output = result
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

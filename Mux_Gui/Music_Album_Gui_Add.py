'''
Created on Feb 5, 2017
@author: rduvalwa2
'''

from tkinter import *
#from Music_Get_Functions  import musicGet_Functions
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
        
        Album_Frame = Frame(self)
        Artist_Frame = Frame(self)
        Type_Frame = Frame(self)
        Genre_Frame = Frame(self)
        
        self.labelInputAlbum = Label(Album_Frame, text="Album Name")        
        self.labelInputArtist = Label(Artist_Frame, text="Artist Name")
        self.labelInputType = Label(Type_Frame, text="Type")
        self.labelInputGenre = Label(Genre_Frame, text="Artist Genre")
        self.labelResult = Label(Album_Frame, text = "Result Album")
        
        self.text_in_Album  = Entry(Album_Frame)
        self.text_in_Artist = Entry(Artist_Frame)
        self.text_in_Type = Entry(Type_Frame)
        self.text_in_Genre = Entry(Genre_Frame)
        
        self.labelInputAlbum.pack()
        self.labelInputArtist.pack()
        self.labelInputGenre.pack()
        self.labelInputType.pack()
        
        self.text_in_Album.pack()
        self.text_in_Artist.pack()
        self.text_in_Type.pack()
        self.text_in_Genre.pack()
        
        self.labelResult.pack()
        
        Album_Frame.pack(side=TOP)
        Artist_Frame.pack(side=TOP)
        Type_Frame.pack(side=TOP)
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
        album = self.text_in_Album.get()
        artist = self.text_in_Artist.get()
        tipe = self.text_in_Type.get()
        genre = self.text_in_Genre.get()
        print(artist  +  genre)
        muxAddAlbum = Music_Load.album_Add_Update_Delete(True)
        result = muxAddAlbum.add_album(album, artist, tipe, genre)
        print("Gui result ", result)
        self.labelResult.config(text=result)
        
        print("Result "  + result)
        self.labelResult.config(text=result)
        
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

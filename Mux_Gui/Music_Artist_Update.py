'''
Created on Feb 6, 2018

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
        self.updateArtistWidgets()
        
    def updateArtistWidgets(self):
        """Add all the widgets to the main frame."""
        tag_name = Frame(self)
        artist_name = Frame(self)
        newGenre_name = Frame(self)
#        result = Frame()
        self.labeltag = Label(tag_name, text="Update Artist Genre")
        self.labelArtist = Label(artist_name, text="Artist Name")
        self.labelNewGenre = Label(newGenre_name, text="New Genre Name")
        self.labelResult = Label(artist_name, text="Result")
                
        self.text_in_artist = Entry(artist_name)
        self.text_in_genre = Entry(newGenre_name)        
        
        self.labeltag.pack()
        self.labelArtist.pack()
        self.labelNewGenre.pack()  
        
        self.text_in_artist.pack()
        self.text_in_genre.pack()
        self.labelResult.pack()  
        
        tag_name.pack(side=TOP)
        artist_name.pack(side=TOP)
        newGenre_name.pack(side=TOP)
#        result.pack(side=TOP) 
            
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
        genre = self.text_in_genre.get()
        muxGet = musicGet_Functions(True)
        result = muxGet.update_artist(artist, genre)
        output = result
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

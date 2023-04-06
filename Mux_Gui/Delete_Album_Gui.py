'''
updated 04/04/2023
Saint-Saëns_ Danse Macabre
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
        
        Album_Frame = Frame(self)
        Artist_Frame = Frame(self)
        Type_Frame = Frame(self)
        Genre_Frame = Frame(self)
        
        self.labelInputAlbum = Label(Album_Frame, text="Delete Album Name")        
        self.labelResult = Label(Album_Frame, text="Result Album")
        self.text_in_Album = Entry(Album_Frame)
        self.labelInputAlbum.pack()
        self.text_in_Album.pack()
        self.labelResult.pack()     
        Album_Frame.pack(side=TOP)
        
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
        album = self.text_in_Album.get()
        DeleteAlbum = musicGet_Functions()
        result = DeleteAlbum.delete_album_by_name(album)
        print("Gui result ", result)
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

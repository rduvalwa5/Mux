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
        
        Album_Cover_Frame = Frame(self)
        NewAlbumCoverName = Frame(self)
        self.labelInputAlbumCover = Label(Album_Cover_Frame, text="Update Album Cover Name") 
        self.labelInputNewAlbumCover = Label(NewAlbumCoverName, text="New Album Cover Name")        
        self.labelResult = Label(NewAlbumCoverName, text = "Album Cover Result")
        
        self.text_in_Album_Cover  = Entry(Album_Cover_Frame)
        self.text_in_NewAlbum_CoverName  = Entry(NewAlbumCoverName)
        
        self.labelInputAlbumCover.pack()
        self.text_in_Album_Cover.pack()
        self.labelInputNewAlbumCover.pack()
        self.text_in_NewAlbum_CoverName.pack()
        
        self.labelResult.pack()
        Album_Cover_Frame.pack(side=TOP)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        
        NewAlbumCoverName.pack(side=TOP)
        
        
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='disabled')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Submit", command=self.handle)
        self.handleb.pack(side=LEFT)
                
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        albumCover = self.text_in_Album_Cover.get()
        newName = self.text_in_NewAlbum_CoverName.get()
        mux = musicGet_Functions(True)
        result = mux.update_album_cover(albumCover, newName)

        print("Gui result ", str(result))
#        self.labelResult.config(text=result)
        
        print("Result "  + str(result))
 
        self.labelResult.config(text= str(result))
        
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

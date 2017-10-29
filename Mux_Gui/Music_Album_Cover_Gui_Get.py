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
        self.labelInputAlbumCover = Label(Album_Cover_Frame, text="Album Cover Name") 
        self.labelResult = Label(Album_Cover_Frame, text = "Album Cover Result")
        
        self.text_in_Album_Cover  = Entry(Album_Cover_Frame)
        
        self.labelInputAlbumCover.pack()
        self.text_in_Album_Cover.pack()
        
        self.labelResult.pack()
        Album_Cover_Frame.pack(side=TOP)
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
        albumCover = self.text_in_Album_Cover.get()
        mux = musicGet_Functions(True)
        result = mux.get_album_cover(albumCover)
        print("Gui result ", result)
        self.labelResult.config(text=str(result))
        
        print("Result ",result)
        self.labelResult.config(text=result)
        
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

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
        Album_Frame = Frame(self)
        Result_Frame = Frame(self)
        
        self.labelInputAlbumCover = Label(Album_Cover_Frame, text="Add Album Cover Name")
        self.labelInput_Album =  Label(Album_Frame, text="Add Album Name")  
        self.labelResult = Label(Result_Frame, text = "Album Cover Result") 
        
        
        self.text_in_Album_Cover  = Entry(Album_Cover_Frame)
        self.text_in_Album  = Entry(Album_Frame)
        
        
        self.labelInputAlbumCover.pack()
        self.text_in_Album_Cover.pack()
        self.labelInput_Album.pack()
        self.text_in_Album.pack_configure()
        self.labelResult.pack()
        
        Album_Cover_Frame.pack(side=TOP)
        Album_Frame.pack(side=TOP)
        Result_Frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        
        
#        bottom_frame = Frame(self)
#        bottom_frame.pack(side=TOP)
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
        album = self.text_in_Album.get()
        mux = musicGet_Functions(True)
        result = mux.add_album_cover(albumCover,album)
        print(result)
        print("Gui result ", result[0]) #,  result[2])
        self.labelResult.config(text=str(result))
        
        print("Result " , result[0])
        self.labelResult.config(text=result[0])
        
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  
'''
Created on Feb 2, 2018

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
        self.addCoverWidgets()
        
    def addCoverWidgets(self):
        """Add all the widgets to the main frame."""
        Widget_Label_Frame = Frame(self)
        Album_Cover_Frame = Frame(self)
        Album_Name_Frame = Frame(self)
        AlbumCoveResult = Frame(self)
        
        self.WidgetLabel = Label(Widget_Label_Frame, text="Album Cover Add Widget")
        self.labelInputAlbumCover = Label(Album_Cover_Frame, text="Add Album Cover Name") 
        self.labelInputAlbumName = Label(Album_Name_Frame, text="Album Name")        
        self.labelResult = Label(AlbumCoveResult, text = "Album Cover Result")
        
        self.text_in_Album_Cover  = Entry(Album_Cover_Frame)
        self.text_in_Album_Name  = Entry(Album_Name_Frame)
        
        self.WidgetLabel.pack()
        self.labelInputAlbumCover.pack()
        self.labelInputAlbumName.pack()
        self.labelResult.pack()
        self.text_in_Album_Cover.pack()
        self.labelInputAlbumCover.pack()
        self.text_in_Album_Name.pack()
        
        Widget_Label_Frame.pack(side=TOP)
        Album_Cover_Frame.pack(side=TOP)
        Album_Name_Frame.pack(side=TOP)
        AlbumCoveResult.pack(side=TOP)
        
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
        album = self.text_in_Album_Name.get()
        mux = musicGet_Functions(True)
        result = mux.add_album_cover(albumCover, album)

        print("Gui result ", str(result))
#        self.labelResult.config(text=result)
        
        print("Result "  + str(result))
 
        self.labelResult.config(text= str(result))
        
        self.QUIT.config(state = 'active')
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  

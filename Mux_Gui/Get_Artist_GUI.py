'''
Updated 04/05/2023

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
        top_frame = Frame(self)
        self.labelInput = Label(top_frame, text="Artist Name")
        self.text_in = Entry(top_frame)
        self.labelResult = Label(top_frame, text="Result")
        self.labelInput.pack()
        self.text_in.pack()
        self.labelResult.pack()
        top_frame.pack(side=TOP)
        
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
        artist = self.text_in.get()
        muxGet = musicGet_Functions()
        result = muxGet.get_artist(artist)
        print("Result is ", result)
        if len(result) != 0:
            artist = []
            idx = 0
            for i in result:
                print(i)
                artist.append((result[idx][0], result[idx][1]))
                idx = idx + 1
            print(artist)            
            output = artist
        else:
            output = artist + " not found"
        self.labelResult.config(text=output)
        self.QUIT.config(state='active')
        self.QUIT.pack(side=TOP)


root = Tk()
app = Application(master=root)
app.mainloop()  

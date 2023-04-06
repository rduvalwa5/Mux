'''
Created on Feb 5, 2017
update 04/04/2023

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
        self.createAlbumWidgets()
        
    def createAlbumWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.labelInput = Label(top_frame, text="Get Album Name")
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
        album = self.text_in.get()
        muxGet = musicGet_Functions()
        result = muxGet.get_album(album)
        print("result is ", result)
        if result != ():
#            for i in result:
#                print(i)
#                albums.append([result][0], result[1], result[2], result[3], result[4], result[5])
            print("albums are ", result[0])            
            output = result[0]
        else:
            output =  album +" not found"
            print(output)
            
 # use .config to change the state of the button           
        self.labelResult.config(text=output)
        self.QUIT.config(state='active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)


root = Tk()
app = Application(master=root)
app.mainloop()  

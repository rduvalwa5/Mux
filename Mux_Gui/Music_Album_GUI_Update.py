'''
Created on Feb 4 2017

@author: rduval
'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
# Labels
        self.label = Label(top_frame, text="Album Name of album to update")       
        self.album_in = Entry(top_frame)
        self.label1 = Label(top_frame, text="Value")
        self.text_in = Entry(top_frame)
        self.label2 = Label(top_frame, text="Result")
#Pack
        self.label.pack()
        self.album_in.pack()
        self.label1.pack()
        self.text_in.pack()
        self.label2.pack()
        self.label.pack()
        self.r = IntVar()
# Buttons
        Radiobutton(top_frame, text="Album Name", variable=self.r, value=1).pack(side=LEFT)
        Radiobutton(top_frame, text="Artist", variable=self.r, value=2).pack(side=LEFT)
        Radiobutton(top_frame, text="Genre", variable=self.r, value=3).pack(side=LEFT)
        Radiobutton(top_frame, text="Type", variable=self.r, value=4).pack(side=LEFT)
        Radiobutton(top_frame, text="Album Cover", variable=self.r, value=5).pack(side=LEFT)
        Radiobutton(top_frame, text="Cover Index", variable=self.r, value=6).pack(side=LEFT)

        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='disabled')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Update", command=self.handle)
        self.handleb.pack(side=LEFT)
        
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        value = self.text_in.get()
        album = self.album_in.get()
        
        operation = self.r.get()
        if operation == 1:
            item = 'album'
            muxGet = musicGet_Functions(True)
            muxGet.update_album(album,item,value)
            result = muxGet.get_album(album)
            if result != []:
                output = result
            else:
                output = " not found"
            
        elif operation == 2:
            item = 'artist'
            muxGet = musicGet_Functions(True)
            muxGet.update_album(album,item,value)
            result = muxGet.get_album(album)
            if result != []:
                output = result
            else:
                output = " not found"
                
        elif operation == 3:
            item = 'genre'
            muxGet = musicGet_Functions(True)
            muxGet.update_album(album,item,value)
            result = muxGet.get_album(album)
            if result != []:
                output = result
            else:
                output =  " not found"
                
        elif operation == 4:
            item = 'type'
            muxGet = musicGet_Functions(True)
            muxGet.update_album(album,item,value)
            result = muxGet.get_album(album)
            if result != []:
                output = result
            else:
                output = " not found"
                
        elif operation == 5:
            item = 'cover_name'
            muxGet = musicGet_Functions(True)
            muxGet.update_album(album,item,value)
            result = muxGet.get_album(album)
            if result != []:
                output = result
            else:
                output = " not found"
                
        elif operation == 6:
            item = 'cover_idx'
            muxGet = musicGet_Functions(True)
            muxGet.update_album(album,item,value)
            result = muxGet.get_album(album)
            if result != []:
                output = result
            else:
                output =  " not found"

 # use .config to change the state of the button           
        self.label.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)
root = Tk()
app = Application(master=root)
app.mainloop()  
    
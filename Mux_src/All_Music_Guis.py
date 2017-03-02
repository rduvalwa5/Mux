'''
Created on Feb 12, 2017

@author: rduvalwa2
'''

from tkinter import *
from Music_Get_Functions import musicGet_Functions

class getSong_UI(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createSongWidgets()
        
    def createSongWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.labelInput = Label(top_frame, text="Song Name \n mp3 aiff m4p ")
        self.text_in = Entry(top_frame)
        self.labelResult = Label(top_frame, text="Result")
        self.labelInput.pack()
        self.text_in.pack()
        self.labelResult.pack()
        top_frame.pack(side=TOP)
        
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
        song = self.text_in.get()
        muxGet = musicGet_Functions()
        result = muxGet.get_song(song)
        if result != []:
            songs = []
            idx = 0
            for i in result:
                print(i)
                songs.append((result[idx][0],result[idx][3],result[idx][4], result[idx][5]))
                idx = idx + 1
            print(songs)            
            output = songs
        else:
            output = song + " not found"
            
 # use .config to change the state of the button           
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)

class getArtist_UI(Frame):
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
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='disabled')
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
        if result != []:
            artist = []
            idx = 0
            for i in result:
                print(i)
                artist.append((result[idx][0],result[idx][1],result[idx][2]))
                idx = idx + 1
            print(artist)            
            output = artist
        else:
            output = artist + " not found"
            
 # use .config to change the state of the button           
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)
        

class getAlbum_UI(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createAlbumWidgets()
        
    def createAlbumWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.labelInput = Label(top_frame, text="Album Name")
        self.text_in = Entry(top_frame)
        self.labelResult = Label(top_frame, text="Result")
        self.labelInput.pack()
        self.text_in.pack()
        self.labelResult.pack()
        top_frame.pack(side=TOP)
        
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
        album = self.text_in.get()
        muxGet = musicGet_Functions()
        result = muxGet.get_album(album)
        if result != []:
            albums = []
            idx = 0
            for i in result:
                print(i)
                albums.append((result[idx][0],result[idx][2]))
                idx = idx + 1
            print(albums)            
            output = albums
        else:
            output = album + " not found"
            
 # use .config to change the state of the button           
        self.labelResult.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)


class getById_UI(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.label1 = Label(top_frame, text="ID")
        self.text_in = Entry(top_frame)
#        self.label2 = Label(top_frame, text="Item Type")
#        self.text_in2 = Entry(top_frame)        
        self.label = Label(top_frame, text="Result")
        self.label1.pack()
        self.text_in.pack()
 #       self.label2.pack()
 #       self.text_in2.pack()
        self.label.pack()
        self.r = IntVar()
        Radiobutton(top_frame, text="Song", variable=self.r, value=1).pack(side=LEFT)
        Radiobutton(top_frame, text="Artist", variable=self.r, value=2).pack(side=LEFT)
        Radiobutton(top_frame, text="Album", variable=self.r, value=3).pack(side=LEFT)
        top_frame.pack(side=TOP)
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
#how to disable a button
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit, state='disabled')
        self.QUIT.pack(side=LEFT)
        self.handleb = Button(bottom_frame, text="Get Id", command=self.handle)
        self.handleb.pack(side=LEFT)
        
    def handle(self):
        """Handle a click of the button by processing any text the
        user has placed in the Entry widget according to the selected
        radio button."""
        text = self.text_in.get()
        operation = self.r.get()
        if operation == 1:
            item = 'song'
            muxGet = musicGet_Functions()
            result = muxGet.get_by_id(text, item)
            if result != []:
                output = result
            else:
                output = text + " not found"
            
        elif operation == 2:
            item = 'artist'
            muxGet = musicGet_Functions()
            result = muxGet.get_by_id(text, item)
            if result != []:
                output = result
            else:
                output = text + " not found"
        elif operation == 3:
            item = 'album'
            muxGet = musicGet_Functions()
            result = muxGet.get_by_id(text, item)
            if result != []:
                output = result
            else:
                output = text + " not found"
        else:
            output = "*******"
 # use .config to change the state of the button           
        self.label.config(text=output)
        self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
        self.QUIT.pack(side=TOP)



class Application(Frame):
    def create_getArtist(self):
        getArtist_UI(self)
           
    def create_getAlbum(self):
        getAlbum_UI(self)
        
    def create_getSong(self):
        getSong_UI(self)
        
    def create_getById(self):
        getById_UI(self)

    def create_widgets(self):
        
        self.x_button = Button(self, text="Get Artist", fg = "black", bg = "white", command=self.create_getArtist)
        self.x_button.pack({"side": "left"})
        
        self.d_button = Button(self, text="Get Album", fg = "white", bg = "black",command=self.create_getAlbum)
        self.d_button.pack({"side": "left"})
        
        self.d_button = Button(self, text="Get song", fg = "white", bg = "black",command=self.create_getSong)
        self.d_button.pack({"side": "left"})
        
        self.d_button = Button(self, text="Get By Id", fg = "white", bg = "black",command=self.create_getById)
        self.d_button.pack({"side": "left"})

        self.QUIT = Button(self, text="Quit", fg="red",bg="black", command=self.quit)
        self.QUIT.pack({"side": "right"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()


    
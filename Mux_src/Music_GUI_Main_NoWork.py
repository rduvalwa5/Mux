'''
Created on Feb 12, 2017

@author: rduvalwa2
'''
#from tkinter import *

#import Music_GUI_Get_Album
#import Music_GUI_Get_Artist
#import Music_GUI_Get_Song
#import Music_GUI_GetBy_Id

#import Music_GUI_Get_Artist, Music_GUI_Get_Song, Music_GUI_Get_Album, Music_GUI_GetBy_Id
# from tkinter.simpledialog import Dialog
# from Music_Get_Functions import musicGet_Functions

#class getAlbum:   
#    def getabumUi(self):
#        print("Start Get Albums")
#        Music_GUI_Get_Album
 
 
#class Application(Frame):
#    """Application main window class."""
#    def __init__(self, master=None):
#        """Main frame initialization (mostly delegated)"""
#        Frame.__init__(self, master)
#        self.pack()
#        self.create_widgets()
 
#    def getAlbumUi(self):
#        print("Start Get Albums")
#        Music_GUI_Get_Album
     
      
#    def create_widgets(self):
#        self.QUIT = Button(self, text="Quit", fg="red",bg="white", command=self.quit)
#        self.QUIT.pack({"side": "left"})
        
#        self.album_button = Button(self, text="Get Albums", fg = "blue", bg = "white",command=self.getAlbumUi())
#        self.album_button.pack({"side": "right"})

#        self.x_button = Button(self, text="Get Song", fg = "white", bg = "white",command=Music_GUI_Get_Song.Application)
#        self.x_button.pack({"side": "right"})

#        self.d_button = Button(self, text="Get Artist",fg = "red", bg = "white", command=Music_GUI_Get_Artist.Application)
#        self.d_button.pack({"side": "left"})

#        self.d_button = Button(self, text="Get By Id",fg = "black", bg = "white", command=Music_GUI_GetBy_Id.Application)
#        self.d_button.pack({"side": "left"})   
        


from tkinter import *
from tkinter.simpledialog import Dialog
import Music_GUI_Get_Album

class GetAlbum(Dialog):
    
    def body(self,master):
        self.result = None
        print("GetAlbum running")
#        Music_GUI_Get_Album
        
    def apply(self):
         self.result = "getting album"

class MyDialog(Dialog):
    def body(self, master):
        self.result = None
        for r in range(5):
            for c in range(5):
                b = Button(master, text="Row {0} Col {1}".format(r, c))
                b.grid(row=r, column=c)
        print("Dialog created")

    def apply(self):
        self.result = "OK"


class MyColors(Dialog):
    def body(self, master):
        self.result = None
#        for r in range(5):
#            for c in range(5):
        a = Button(master, text="Button Red",fg = "black", bg = "red")
        b = Button(master, text="Button White",fg = "black", bg = "white")
        c = Button(master, text="Button Blue",fg = "black", bg = "blue")
        a.grid(row=1, column=1)
        b.grid(row=2, column=1)
        c.grid(row=3, column=1)
        
        print("Colors created")

    def apply(self):
        self.result = "OK"
        
class Application(Frame):
    def create_dialog(self):
        d = MyDialog(self)
        print(d.result)
        
    def create_Colors(self):
        c = MyColors(self)
        print(c.result)

    def create_Album(self):
        c = GetAlbum(self)
        print(c.result)

        

    def create_widgets(self):
        
        self.x_button = Button(self, text="Colors", fg = "black", bg = "green", command=self.create_Colors)
        self.x_button.pack({"side": "right"})
        
        self.d_button = Button(self, text="Dialog...", command=self.create_dialog)
        self.d_button.pack({"side": "left"})

        self.album_button = Button(self, text="Get Albums", fg = "blue", bg = "white",command=self.create_Album())
        self.album_button.pack({"side": "right"})

        self.QUIT = Button(self, text="Quit", fg="red",bg="black", command=self.quit)
        self.QUIT.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()


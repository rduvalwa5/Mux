'''
Created on Apr 11, 2017

@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions

class Music_GUI_Get_Album(Frame):
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
#root = Tk()
#app = Music_GUI_Get_Album(master=root)
#app.mainloop()  


class Main_Gui():
    gui = ""
    while gui != "Q":
        print("Select MUSIC UI")
        print("1  Get ALbum")
        print("2  Get Song")
        print("3  Get Artist")
        print("4  Get By ID")
        print("Q to Quit")

        gui = input('Input UI: ')
        print("inpt is ", gui)
        if gui == "1":
            print("Music_GUI_Get_Album")
            root = Tk()
            app = Music_GUI_Get_Album(master=root)
            app.mainloop()  
        if gui == "2":
            print("Music_GUI_Get_Song")
        #    Music_GUI_Get_Song      
#        gui = input('Input UI: ')      
        if gui == "3":
            print("Music_GUI_Get_Artist")
#    Music_GUI_Get_Artist
#        gui = input('Input UI: ')
        if gui == "4":
            print("Music_GUI_GetBy_Id")
#    Music_GUI_GetBy_Id
        else:
            print("Invalid Input")
        print(gui + "is now")
#    gui = input('Input UI: ')
print("Exiting")
exit

if __name__  == '__main__':
    Main_Gui
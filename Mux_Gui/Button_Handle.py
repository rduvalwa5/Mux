'''
Created on Apr 12, 2017

@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions

class Application(Frame):
    def __init__(self, master=None):
 #       def getAlbum():
 #           Album
#        def frame1ClickHandler(event):
#            print("Frame 1", event.x, event.y)
#        def frame2ClickHandler(event):
#            print("Frame 2", event.x, event.y)
        def makeRed():
            self.Album
        def makeBlue():
            self.text_in2.config(fg="blue")
        def makeGreen():
            self.text_in2.config(fg="green")
        def makeBlack():
            self.text_in2.config(fg="black")
        def openHandler():
            try:
                #Music_GUI_Display_AlbumSongs
                pass
            except IOError as e:
                    self.text_in2.insert(END, e)\
                    
                    
        def Album(Frame):
            def __init__(self, master=None):
                Frame.__init__(self, master)
                self.pack()
                self.createAlbumWidgets()
        
            def createAlbumWidgets(self):
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
                self.QUIT = Button(bottom_frame, text="Quit", command=self.quit(), state='disabled')
                self.QUIT.pack(side=LEFT)
                self.handleb = Button(bottom_frame, text="Submit", command=self.handle)
                self.handleb.pack(side=LEFT)
                
            def handle(self):
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
                self.labelResult.config(text=output)
            self.QUIT.config(state = 'active')
#        self.QUIT.pack(side=BOTTOM)
            self.QUIT.pack(side=TOP)
            root = Tk()
            app = Album(master=root)
            app.mainloop()                      
        
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=N + S + W + E)
        self.rowconfigure(5, weight=1)
        for c in range(1, 4):
            self.columnconfigure(c, weight=1)
            myButtonTxt = ['Album', 'Songs', 'Artist']
            myButtonCmd = [makeRed, makeBlue, makeGreen, makeBlack]
            Button(self, text=myButtonTxt[c - 1].format(c), command=myButtonCmd[c - 1]).grid(row=14, column=c, sticky=E + W)

root = Tk()
app = Application(master=root)                
app.mainloop()

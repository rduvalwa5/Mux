'''
Created on Dec 22, 2019

@author: rduvalwa2
'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
import os, sys , platform

class Music_Main_GUI(Frame):
    def getSongList(self):
        root = Tk()       
        root.geometry("1000x500+30+30")
        menuItems = ["1 Get By ALbum","2 Get Song","3 Get Song By Artist","4 Get Song By Genre","5 Get Song By Type" ]
        menuList = []
        mux = musicGet_Functions(True)
#        songsIn = mux.get_AllSongs()
#        print(songsIn)
        menuList = Listbox(root, yscrollcommand = scrollbar.set, width = 150, selectmode = EXTENDED )
#        menuList.insert(END,"End" )
#       for n in range(len(songList)):
#            item = str(albumCoverList[n][1])
#            item = songList[n]
#            print("print item ", item)
#            mylist.insert(END,albumCoverList[n][1])
#            mylist.insert(END, item)
#        menuList.insert(END,"Total Albums " + str(menuList.size()))
        menuList.pack( side = LEFT, fill = BOTH )

#        scrollbar.config( command = menuList.yview )
        menuList.bind("<Double-Button-1>", self.OnDouble)
        mainloop()

    def play_song(self,songPath):
        self.aPath = songPath
        print(self.aPath)
        self.songAndPath =  self.aPath
        print("song path is ",self.songAndPath)
#        self.comd = "afplay -t 30 "  + "\"" + self.songAndPath + "\""
        self.comd = "afplay "  + "\"" + self.songAndPath + "\""
        print("command is ",self.comd)
        os.system(self.comd)

    def OnDouble(self, event):
        root = Toplevel
        if platform.uname().node == 'OSXAir.home.home':
            base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/"
            print(base)
        else:
            print("Not playable on this platform")
            
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print("print value ",value)
        print ("print selection:", selection, ": '%s" % value)
        songfile =  value
        print("song is ", songfile)
        self.play_song(value)

if __name__ == "__main__":

    app = Music_Main_GUI()
    app.getSongList()
 #   app.QuitButton()

'''
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
            print("Music_GUI_MAIN")
            root = Tk()
            app = Music_Main_GUI(master=root)
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

    app = Music_Main_GUI()
 #   app.getSongList()
 #   Main_Gui
 
 '''
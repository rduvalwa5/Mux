'''
List of album covers
@author: rduvalwa2
/Library/Frameworks/Python.framework/Versions/3.6/bin
sudo pip3 install pillow

select
http://effbot.org/imagingbook/pil-index.htm

1) UI list of album covers
2) Select one cover 
3) Double click displays cover

'''
from tkinter import *
from Music_Get_Functions import musicGet_Functions
import MySQLdb   as connDb
import os, sys , platform
from Music_PlaySong import Play_Song

class displaySongList():
    

    
    def getSongList(self):
        root = Tk()       
        root.geometry("1000x500+30+30")
        songList = []
        base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/"
        mux = musicGet_Functions(True)
        songsIn = mux.get_AllSongs()
        print(songsIn)
        if songsIn != []:
            for song in songsIn:
                print("Song is ",song)
                aSong = base +  song[1] + "/" + song[2] + "/" + song[3] 
                songList.append(aSong)
        else:
            songList.append("None found!")
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill=Y )

        mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 150, selectmode = EXTENDED )
        mylist.insert(END,"Total Songs " + str(len(songList)))
        for n in range(len(songList)):
#            item = str(albumCoverList[n][1])
            item = songList[n]
            print("print item ", item)
#            mylist.insert(END,albumCoverList[n][1])
            mylist.insert(END, item)
        mylist.insert(END,"Total Albums " + str(mylist.size()))
        mylist.pack( side = LEFT, fill = BOTH )

        scrollbar.config( command = mylist.yview )
        mylist.bind("<Double-Button-1>", self.OnDouble)
        mainloop()

    def play_song(self,songPath):
        self.aPath = songPath
        print(self.aPath)
        self.songAndPath =  self.aPath
        print("song path is ",self.songAndPath)
        self.comd = "afplay -t 30 "  + "\"" + self.songAndPath + "\""
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

    app = displaySongList()
    app.getSongList()
    app.QuitButton()


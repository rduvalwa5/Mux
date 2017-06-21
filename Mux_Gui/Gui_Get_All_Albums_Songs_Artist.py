from tkinter import *
from Music_Get_Functions import musicGet_Functions

def getSongs():
    root = Tk()
    
    songList = []
    mux = musicGet_Functions(True)
    songsIn = mux.get_AllSongs()
    if songsIn != []:
        for song in songsIn:
            print(song)
            songList.append((song[0],song[1],song[2],song[3]))
    else:
        songList.append("None found!")
    print(songList[0])
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill=Y )
    mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 150, selectmode = EXTENDED, bg = 'cyan' , fg = 'black')
    for n in range(len(songList)):
        mylist.insert(END,str(n) + "  " + str(songList[n][0]) + "  " + songList[n][1] + "  " + songList[n][2] + "  " + songList[n][3])
    mylist.insert(END,"Total Artist " + str(mylist.size()))
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
#mainloop()


def getAlbums():
        root = Tk()
        albumList = []
        mux = musicGet_Functions(True)
        albumsIn = mux.get_all_albums()
        print(albumsIn)
        if albumsIn != []:
            for album in albumsIn:
                print(album)
                albumList.append((album[0],album[1],album[2]))
        else:
            albumList.append("None found!")

#        print(albumList)
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill=Y )
        mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED )
        for n in range(len(albumList)):
            mylist.insert(END," " + str(albumList[n][0]) + "  " + albumList[n][1] + "  " + albumList[n][2] )
            mylist.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = mylist.yview )
        mylist.insert(END,"Total Albums " + str(mylist.size()))
#        mainloop()

def getArtists():
        root = Tk()
        artistList = []
        mux = musicGet_Functions(True)
        artistIn = mux.get_all_artist()
        print(artistIn)
        if artistIn != []:
            for artist in artistIn:
                print(artist)
                artistList.append((artist[0],artist[1]))
            else:
                artistList.append("None found!")
        print(artistList)

        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill=Y )

        mylist = Listbox(root, yscrollcommand = scrollbar.set, width = 100, selectmode = EXTENDED, bg = 'yellow' , fg = 'red')

        for n in range(len(artistList)):
                mylist.insert(END,str(n) + "  " + str(artistList[n][1]) + "  " + artistList[n][0])
        mylist.insert(END,"Total Artist " + str(mylist.size()))
        mylist.pack( side = LEFT, fill = BOTH )
        scrollbar.config( command = mylist.yview )
#        mainloop() 


def create_window():
    window = Toplevel(root)

root = Tk()
#b = Button(root, text="Create new window", command=create_window)
# Button(self, text=myButtonTxt[c - 1].format(c), command=myButtonCmd[c - 1]).grid(row=14, column=c, sticky=E + W)

buttonAlbums = Button(root, text="Get All Albums",command=getAlbums)
buttonAlbums.pack()
buttonArtist = Button(root,text="Get All Artist", command=getArtists)
buttonArtist.pack()
buttonAllSongs = Button(root,text="Get All Songs",command = getSongs)
buttonAllSongs.pack()

root.mainloop()
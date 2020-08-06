import os, platform

class musicLoad_Write:

    def __init__(self):
        
        self.server = platform.node()
        self.fileName = self.server + "_songs.txt"
        print(self.server)
        if self.server == "MaxBookPro17OSX":
                self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music"
        if self.server == "RandallDuvalsMBP":
                self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music"
        if self.server == "OSXAir.hsd1.wa.comcast.net":
                self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music"               
                
    
    def get_music_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index, directory))
                index = index + 1
        return artist

    def get_all_songs(self):
        index = 0
        albums = []
        songs = []
        artist = self.get_music_artist()
        for a in artist:
            if os.path.isdir(self.base + "/" + a[1]):
                artist_albums = os.listdir(self.base + "/" + a[1])
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((a, album))
                        album_songs = os.listdir(self.base + "/" + a[1] + "/" + album)
                        for song in album_songs:
                            if song != '.DS_Store' and song != 'side1.mp3' and song != 'side2.mp3' and song != 'side3.mp3' and song != 'side4.mp3':
                                songs.append((self.server, index, a[1], album, song))
                                index = index + 1
        return songs
    
    def getFile(self):
            songFiles = open(self.fileName, "w+")
            return songFiles
        
    def readFile(self):
        print("Reading File", self.fileName)
        f = open(self.fileName, "r")
        print(f.read())
#        f.close()
        
if __name__ == '__main__':
    a = musicLoad_Write()
    theseSongs = a.get_all_songs()
    fileOfSongs = a.getFile()
    for song in theseSongs:
#        print(song)
        fileOfSongs.write(str(song) + "\n")
#    fileOfSongs.close()
    myFileObject = open(a.fileName, "r")
#    f = a.getFile()
    
    print(myFileObject.read())
    myFileObject.close()
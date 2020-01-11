'''
Created on Oct 19, 2017
@author: rduvalwa2
Count aritst folders in directory structure
path = 
'''
import os, sys

class get_music_counts():
    def __init__(self, root = '/Users/rduvalwa2/Music/iTunes/iTunes Media/Music'):
        self.path = root
        self.artistDirs = os.listdir( self.path )
        self.artistCount = 0
        self.albumCount = 0
        self.songCount = 0
        self.listOfSongs = []
        self.listOfArtist = []
        self.listOfAlbums = []
        self.listMusicFiles = []
        self.listMusicDirecories = []
        
    def get_artist_count(self):
#        dirs = os.listdir( self.path )
        for file in self.artistDirs:
            os.listdir( self.path )
            if os.path.isdir(self.path + file):
                if ".DS_Store" in file or ".com.apple" in file:
                    continue
                else:
                    self.artistCount = self.artistCount + 1
        return self.artistCount
    
    def get_album_count(self):
        artist = []
        for file in self.artistDirs:
            artist.append(file)
        for art in artist:
            if os.path.isdir(self.path + art):
                albums = os.listdir(self.path + art)
                for album in albums:
                    if os.path.isdir(self.path + art + '/' + album):
#                        print(album)
                        self.albumCount = self.albumCount + 1
        return self.albumCount

    def get_song_count(self):     
        artist = []
#        albums = []
        listOfFiles = []
        for file in self.artistDirs:
            artist.append(file)
         
        for art in artist:   
            if os.path.isdir(self.path + art):
                albums = os.listdir(self.path + art)
                for album in albums:
                    if os.path.isdir(self.path + art + '/' + album):
                        filess = os.listdir(self.path + art + '/' + album)
                        for f in filess: 
#                            if os.path.isfile(self.path + art + '/' + album + '/' + f):
#                                if '.DS_Store' in f or '.com.apple' in f or '.jpg' in f:
#                                    continue
                               if ".m" in f or ".aiff" in f:
#                                else:
                                    self.songCount = self.songCount + 1
        return self.songCount

    def get_list_songs(self):     
        for file in self.artistDirs:
            self.listOfArtist.append(file)     
        for art in self.listOfArtist:   
            if os.path.isdir(self.path + art):
                albums = os.listdir(self.path + art)
                for album in albums:
                    if os.path.isdir(self.path + art + '/' + album):
                        self.listOfAlbums.append(album)
                        filess = os.listdir(self.path + art + '/' + album)
                        for f in filess: 
                            if os.path.isfile(self.path + art + '/' + album + '/' + f):
                                if ".m" in f or ".aiff" in f:
                                    self.listOfSongs.append(f)
        return self.listOfSongs
    
    def get_list_artist(self):     
        for file in self.artistDirs:
            if ".DS_Store" in file or ".com.apple" in file:
                continue
            else:
                self.listOfArtist.append(file)
        return self.listOfArtist

    def get_list_albums(self):     
        for file in self.artistDirs:
            self.listOfArtist.append(file)     
        for art in self.listOfArtist:   
            if os.path.isdir(self.path + art):
                albums = os.listdir(self.path + art)
                for album in albums:
                    if os.path.isdir(self.path + art + '/' + album):
                        self.listOfAlbums.append(album)
                        filess = os.listdir(self.path + art + '/' + album)
        return self.listOfAlbums
    
    def walk_music(self):
        '''
        https://www.tutorialspoint.com/python/os_walk.htm
        '''
        # listMusicDirecories
        for root, dirs, files in os.walk(self.path, topdown=False):
            for name in files:
#                print(os.path.join(root, name))
                self.listOfSongs.append(name)
        for name in dirs:
#                print(os.path.join(root, name))
                self.listOfArtist.append(name)

if __name__ == '__main__':
    a = get_music_counts()
    print(a.get_artist_count())
    print(a.get_album_count())
    print(a.get_song_count())
    '''
    for artist in a.get_list_artist():
        print(artist)

    for album in a.get_list_albums():
            print(album)
        
    for song in a.get_list_songs():
            print(song)
        '''
    a.walk_music()
    artistCount = 0
    for artist in a.listOfArtist:
#        print(artist)
        artistCount = artistCount + 1
        
    songCount = 0  # song count will be greater by 3 because of test files in directory that are not in data base
    for song in a.listOfSongs:
        if ".m" in song or ".aif" in song: 
#            print(song)
            songCount = songCount + 1 
        else:
#            print(song)
            continue

    print("Number of artist from list",len(a.listOfArtist))
    print("Number of songs from list",len(a.listOfSongs))
    print("Artist count", artistCount)
    print("Song Count",songCount)
import os, platform

class musicLoad_Write:

    def __init__(self, test=False):
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music"
        self.server = platform.node()
    
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
        
if __name__ == '__main__':
    a = musicLoad_Write()
    theseSongs = a.get_all_songs()
    for song in theseSongs:
        print(song)
        
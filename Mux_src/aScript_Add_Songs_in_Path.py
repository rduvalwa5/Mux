'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/music/music/Media.localized/John Cafferty & The Beaver Brown Band/Tough All Over"    
    album = "Tough All Over"
    artist = "John Cafferty & The Beaver Brown Band"
    genre = "Rock"
    inType = "Itunes"
    Medium = 'Download'    
    mux.add_songs_in_path(myPath, album, artist, genre, inType, Medium)
#    mux.add_album(album, artist, genre, inType, Medium)
#    mux.add_artist(artist, genre)

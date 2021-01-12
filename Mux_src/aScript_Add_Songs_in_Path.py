'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/The Who/The Who At Filllmore East 1968"    
    album = "The Who"
    artist = "The Who At Filllmore East 1968"
    genre = "Rock"
    inType = "Vinyl"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)
#    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)

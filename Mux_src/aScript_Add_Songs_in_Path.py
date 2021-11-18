'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/The Stooges/The Stooges [Disc 2]"    
    album = "The Stooges [Disc 2]"
    artist = "The Stooges"
    genre = "Rock"
    inType = "CD"
    Medium = 'CD'    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType, Medium)
    mux.add_album(album, artist, genre, inType, Medium)
#    mux.add_artist(artist, genre)

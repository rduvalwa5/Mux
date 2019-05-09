'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/The Spinners/The Definitive Soul Collection Of The Spinners [Disc 1]"    
    album = "The Definitive Soul Collection Of The Spinners [Disc 2]"
    artist = "The Spinners"
    genre = "R&B"
    inType = "CD"    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType)
    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)

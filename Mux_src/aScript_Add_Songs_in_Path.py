'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/Nat King Cole/Love Is the Thing"    
    album = "Love Is the Thing"
    artist = "Nat King Cole"
    genre = "Pop"
    inType = "Vinyl"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)
#    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)

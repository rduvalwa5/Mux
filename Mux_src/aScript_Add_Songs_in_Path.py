'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/iTunes/iTunes Media/Music/John Mayall & The Bluesbreakers & Eric Clapton/Bluesbreakers"    
    album = "Bluesbreakers"
    artist = "John Mayall & The Bluesbreakers & Eric Clapton"
    genre = "Blues"
    inType = "Vinyl"    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType)
    mux.add_album(album, artist, genre, inType)
    mux.add_artist(artist, genre)

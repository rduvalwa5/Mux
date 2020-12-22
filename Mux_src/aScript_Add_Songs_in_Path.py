'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/Edith Piaf/The Voice Of The Sparrow_ The Very Best Of Édith Piaf"    
    album = "The Voice Of The Sparrow_ The Very Best Of Édith Piaf"
    artist = "Edith Piaf"
    genre = "French Pop"
    inType = "CD"    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType)
    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)

'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__": 
    mux = musicGet_Functions()
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/Keith Jarrett/Paris Concert [Live]"    
    album = "Paris Concert [Live]"
    artist = "Keith Jarrett"
    genre = "Jazz"
    inType = "Amazon"
    Medium = 'CD'    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType, Medium)
    mux.add_album(album, artist, genre, inType, Medium)
#   mux.add_artist(artist, genre)

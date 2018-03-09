'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/The Doobie Brothers/Farewell Tour (Live) [Remastered]"
    
    album = "Farewell Tour (Live) [Remastered]"
    artist = "The Doobie Brothers"
    genre = "Rock"
    inType = "Download"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)
#    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)

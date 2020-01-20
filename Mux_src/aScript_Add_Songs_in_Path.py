'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Lester Young With The Oscar Peterson Trio/Lester Young With The Oscar Peterson Trio"    
    album = "Lester Young With The Oscar Peterson Trio/Lester Young With The Oscar Peterson Trio"
    artist = "Lester Young With The Oscar Peterson Trio"
    genre = "Jazz"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)
#    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)

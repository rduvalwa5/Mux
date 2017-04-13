'''
Created on Mar 16, 2017

@author: rduvalwa2

'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions()
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Edgar Winter/The Best of Edgar Winter"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Kenny Rogers & The First Edition/Anthology Kenny Rogers & The First Edition"
    album = "The Best of Edgar Winter"
    artist = "Edgar Winter"
    genre = "Rock"
    inType = "Download"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Elton John/The One"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Kenny Rogers & The First Edition/Anthology Kenny Rogers & The First Edition"
    album = "The One"
    artist = "Elton John"
    genre = "Rock"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

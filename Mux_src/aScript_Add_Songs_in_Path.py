'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions()
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/John Scofield/A Go Go"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Kenny Rogers & The First Edition/Anthology Kenny Rogers & The First Edition"
    album = "A Go Go"
    artist = "John Scofield"
    genre = "Jazz"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

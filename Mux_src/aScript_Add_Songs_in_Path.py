'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Joni Mitchell/Hits/"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Kenny Rogers & The First Edition/Anthology Kenny Rogers & The First Edition"
    album = "Hits"
    artist = "Joni Mitchell"
    genre = "Folk"
    inType = "Vinyl"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

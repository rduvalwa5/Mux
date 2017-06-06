'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions()
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Pete Seeger & Arlo Guthrie/Pete Seeger & Arlo Guthrie - Together In Concert"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Kenny Rogers & The First Edition/Anthology Kenny Rogers & The First Edition"
    album = "Pete Seeger & Arlo Guthrie - Together In Concert"
    artist = "Pete Seeger & Arlo Guthrie"
    genre = "Folk"
    inType = "Vinyl"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

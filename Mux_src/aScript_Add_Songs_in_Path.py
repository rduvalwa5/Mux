'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Linda Ronstadt & Emmylou Harris/Western Wall_ The Tucson Sessions"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Kenny Rogers & The First Edition/Anthology Kenny Rogers & The First Edition"
    album = "Western Wall: The Tucson Sessions"
    artist = "Linda Ronstadt & Emmylou Harris"
    genre = "Country"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

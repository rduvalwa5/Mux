'''
Created on Mar 16, 2017
@author: rduvalwa2

'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions()
    myPath = "/Users/rduvalwa2/music/iTunes/iTunes Music/Music/Seals & Crofts/Seals & Crofts Greatist Hits"
    album = "Seals & Crofts/Seals & Crofts Greatist Hits"
    artist = "Seals & Crofts"
    genre = "Rock"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

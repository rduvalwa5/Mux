'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/music/iTunes/iTunes Music/Music/Marty Robbins/Gunfighter Ballads And Trail Songs"    
    album = "Gunfighter Ballads And Trail Songs"
    artist = "Marty Robbins"
    genre = "Country"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)
#    mux.add_album(album, artist, genre, inType)
#    mux.add_artist(artist, genre)
    

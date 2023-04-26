'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__": 
    mux = musicGet_Functions()
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/The Statler Brothers/The Best of the Statler Bros_"    
    album = "The Best of the Statler Bros_"  
    artist = "The Statler Brothers"
    genre = "Country"
    inType = "Itunes"
    Medium = 'Download'    
#    mux.add_songs_in_path(myPath, album, artist, genre, inType, Medium)
    mux.add_album(album, artist, genre, inType, Medium)
    mux.add_artist(artist, genre)

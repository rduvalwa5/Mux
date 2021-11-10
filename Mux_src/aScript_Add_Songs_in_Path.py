'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/Music/Media.localized/Ivan Shekov/Ludwig Van Beethoven, Johannes Brahms und Frederic Chopin"    
    album = "Ludwig Van Beethoven, Johannes Brahms und Frederic Chopin"
    artist = "Ivan Shekov"
    genre = "Classical"
    inType = "Vinyl"
    Medium = 'Vinyl'    
    mux.add_songs_in_path(myPath, album, artist, genre, inType, Medium)
#    mux.add_album(album, artist, genre, inType, Medium)
#    mux.add_artist(artist, genre)

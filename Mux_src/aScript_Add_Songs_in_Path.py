'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :       
    mux = musicGet_Functions(True)
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Cream/Live Cream Vol 2"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Duran Duran/Greatest"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Drive-By Truckers/American Band"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Black Sabbath/Black Sabbath"
#    myPath =  "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Gregg Allman/Live Back To Macon GA Disc 1"
#    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Eric Clapton/Live In San Diego With Special Guest JJ Cale Disc 2"
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Cream/Goodbye"
    
    album = "Goodbye"
    artist = "Cream"
    genre = "Rock"
    inType = "CD"    
    mux.add_songs_in_path(myPath, album, artist, genre, inType)   

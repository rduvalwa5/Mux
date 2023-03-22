'''
Created on Mar 16, 2017

@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__": 
    mux = musicGet_Functions()
    print(mux.get_count('artist', ''))
    artistsList = ["Seals & Crofts", "Herb Alpert & The Tijuana Brass", "Joni Mitchell"]  # "Seals & Crofts",
    for artist in artistsList:
        mux.delete_artist(artist)
    print(mux.get_count('artist', ''))

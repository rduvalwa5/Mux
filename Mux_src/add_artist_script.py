'''
Created on Mar 16, 2017

@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :    
    mux =  musicGet_Functions()
    print(mux.get_count('artist', ''))
    artistsList = [("Seals & Crofts","Rock"),("Herb Alpert & The Tijuana Brass","Alternative"),("Joni Mitchell","Rock")]
    for artist in artistsList:
        mux.add_artist(artist[0], artist[1])
    print(mux.get_count('artist', ''))
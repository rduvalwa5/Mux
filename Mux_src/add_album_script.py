'''
Created on Mar 16, 2017
@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :    
    mux =  musicGet_Functions()
    print(mux.get_count('artist_albums', ''))
    albumList = [("Seals & Crofts/Seals & Crofts Greatist Hits","Seals & Crofts","Rock","CD"),("Lost Treasures_ Rare & Unreleased","Herb Alpert & The Tijuana Brass","Alternative","CD"),("Joni Mitchell Hits","Joni Mitchell","Rock","CD")] 
    for album in albumList:
#        mux.add_album(album, artist, tipe)
        mux.add_album(album[0], album[1],album[2],album[3])
    print(mux.get_count('artist_albums', ''))
    
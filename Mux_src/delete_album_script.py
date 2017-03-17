'''
Created on Mar 16, 2017
@author: rduvalwa2
'''
from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :
    mux =  musicGet_Functions()
    print(mux.get_count('artist_albums', ''))
    albumList = ["Seals & Crofts/Seals & Crofts Greatist Hits","Lost Treasures_ Rare & Unreleased","Joni Mitchell Hits"] 
    for album in albumList:
        mux.delete_album(album)
    print(mux.get_count('artist_albums', ''))

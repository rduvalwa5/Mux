'''
Created on Mar 16, 2017

@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__": 
    mux = musicGet_Functions(True)
    print(mux.get_count('album2songs', ''))
    songidList = [7513, 7514, 7515, 7516, 7517] 
    for id in songidList:
        mux.delete_song(id)
    print(mux.get_count('album2songs', ''))

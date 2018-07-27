'''
Created on May 31, 2018

@author: rduvalwa2
'''


import Derived_Music_Load
from Derived_Music_Load import derived_musicLoad_Functions
        
if __name__ == "__main__" :    
    mux = derived_musicLoad_Functions(True)
    mux.initial_insert_into_artist()
    mux.initial_insert_into_artistAlbums()
    mux.initial_insert_into_album2songs()
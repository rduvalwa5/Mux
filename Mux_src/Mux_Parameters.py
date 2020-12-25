'''
Created on Dec 20, 2020

@author: rduvalwa2
'''

import os, platform


#class Mux_Parameters:


hostName = platform.uname().node

if platform.uname().node == 'C1246895-XPS':
            print("Host is " , hostName)
            base = "To be determined"
            coverbase =  "To be determined"
            server = hostName
elif platform.uname().node == 'C1246895-osx.home.home':
            print("Host is " ,  hostName)
            base = "/Users/rduvalwa2/music/Music/Media.localized"
            coverbase = "To be determined"
            server= hostName
elif platform.uname().node == 'OsxAir.hsd1.wa.comcast.net':
            print("Host is " ,  hostName)
            base = "To be determined"
            coverbase = "/Users/rduvalwa2/Code_Projects/Active_Mux/AlbumCovers/"
            server= hostName
            base = "/Users/rduvalwa2/Music/Music/Media.localized"
else:
            print("Host is " , 'default')
            base = "To be determined"
            coverbase = "/Users/rduvalwa2/Code_Projects/Active_Mux/AlbumCovers/"
            server= hostName
            base = "/Users/rduvalwa2/Music/Music/Media.localized"

genreList =['Rock','Alternative','BlueGrass','Blues','Classical','Country','Folk','Holiday','Jazz','Latino','Pop', \
                         'Regae','RockaBilly','Soul','Talk','TestGenre','TexMex','Traditional','World','NewGenre','Easy Listening', \
                         'Classic','R&B','French Pop']
    
    
if __name__ == '__main__':
     
#     a = Mux_Parameters()   
#     a.__init__()
     print("Base ",base)
     print("Cover Base ", coverbase)
     print("Genres ", genreList)
     print("server ", server)
     
        
'''
Created on Jan 30, 2018

@author: rduvalwa2
'''
import Music_Get_Functions
#import pymysql 
import pymysql.cursors
import os
import platform
from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx




class Load_Album_Covers():
    def __init__(self):
        if platform.uname().node == 'C1246895-XPS':
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduval', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home':
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = pymysql.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
#            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduvalwa2', password='blu4jazz', db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.hsd1.wa.comcast.net',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = pymysql.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = pymysql.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduvalwa2', password='blu4jazz', db='Music')
        self.server = 'OSXAir.hsd1.wa.comcast.net' 
        self.base = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
        
    def get_all_album_covers(self):
        albumCovers = []
        albumCover_list = os.listdir(self.base)
        for cover in albumCover_list:
            if os.path.isfile(self.base + "/" + cover):
                albumCovers.append((cover))
                albumCovers.sort()
        return albumCovers
    
    def initial_load_album_covers_temp(self):
        idx = 0
        covers = self.get_all_album_covers()
        cursor = self.conn.cursor()
        trunkate = "truncate  `Music`.temp_album_covers ;"
        cursor.execute(trunkate)
        for cov in covers:
            insertStatement = "INSERT into Music.temp_album_covers (album_cover,cover_idx)  values(\"" + cov + "\"," + str(idx) + ");"
            idx = idx + 1
            print(insertStatement)
            cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        
    def initial_load_album_covers(self):
        idx = 0
        covers = self.get_all_album_covers()
        cursor = self.conn.cursor()
        trunkate = "truncate  `Music`.temp_album_covers ;"
        cursor.execute(trunkate)
        for cov in covers:
            insertStatement = "INSERT into Music.temp_album_covers(album_cover,cover_idx)  values(\"" + cov + "\"," + str(idx) + ");"
            idx = idx + 1
            print(insertStatement)
            cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()    
        
        
if __name__  == '__main__':
    loadCov = Load_Album_Covers()
#    covers = loadCov.get_all_album_covers()
#    for cov in covers:
#        print(cov)
    loadCov.initial_load_album_covers_temp()
    
'''
Created on Aug 7, 2017
for testing data base connectivity
@author: rduvalwa2
'''
import os
import platform
import pymysql.cursors # as connDb
#from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx
#from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx

class TestResults:
    if platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
        cover_count = 787
        songs_count = 11944
        artist_count = 585
        artist_albums_count = 1238

    elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
        cover_count = 782
        songs_count = 11935
        artist_count = 576
        artist_albums_count = 1227

class dbInfo:
    def dbSpecs(self):
        USERNAME="rduvalwa2"
        PASSWORD="blu4jazz"
        #HOST="OSXAir.home.home"
        HOST="localhost"
        DATABASE="Music"
        PORT=3306

    def login_spec(self):
        login_info_default = "host='OSXAir.hsd1.wa.comcast.net',user='root',password='blu4jazz',db='Music'"
        #login_info_osxAir = {"host":"OSXAir.home","user":"rduvalwa2","password":"blu4jazz","db":"Music"}
        login_info_osxAir = {"host":"OSXAir.hsd1.wa.comcast.net","user":"rduval","password":"blu4jazz","db":"Music"}
        login_info_xps = {"host='OSXAir.hsd1.wa.comcast.net',user='rduval',password='blu4jazz',db='Music'"}
        login_info_WIN64_Air = "host='OSXAir.hsd1.wa.comcast.net',user='rduvalwa2',password='blu4jazz',db='Music'"
        login_info_osx = "host='OSXAir.hsd1.wa.comcast.net',user='root',password='blu4jazz',db='Music'"


class musicGet_Functions:   
    def __init__(self,isNotTest):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = pymysql.connect(host='OSXAir', user='rduval', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music')
            self.server = 'MaxBookPro17OSX' 
            self.base = "/Users/rduvalwa2/iTunes/iTunes Media/Music"
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='OSXAir', user='rduvalwa2', password='blu4jazz', db='Music')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduval', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = pymysql.connect(host='OSXAir', user='rduvalwa2', password='blu4jazz', db='Music')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
 
        self.notTestRun =  isNotTest
                
    def get_count(self,table = 'music.album2songs', criteria = " "):
        statement = "select count(*) from " + table + " "  + criteria + ";"
        print("get count statement ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            count = cursor.fetchone()  
            print("Count is from get count ", count[0])
            cursor.close()
            return count[0]       
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_album_cover_count(self):
        cursor = self.conn.cursor()
        statement = "select count(*)  from `Music`.album_covers;"
        try:
            cursor.execute(statement)
            result =cursor.fetchone()
            return result[0]
            cursor.close()
#            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
        
    def dbConnectionClose(self):
        self.conn.close()    

if __name__  == '__main__':
    import unittest
    import DB_Test_Results
    
    class TestConnector(unittest.TestCase):
            
        def test_get_count_Artist(self):
            mux = musicGet_Functions(True)
            table = 'Music.artist'
            criteria = ""
            expected = TestResults.artist_count
            result = mux.get_count(table, criteria)
            print("get_count artist",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
              
        def test_get_count_Artist_Albums(self):
            mux = musicGet_Functions(True)
            table = 'Music.artist_albums'
            criteria = ""
            expected = TestResults.artist_albums_count
            result = mux.get_count(table, criteria)
            print("get_count albums",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
        def test_get_count_album2Songs(self):
            mux = musicGet_Functions(True)
            table = 'Music.album2songs'
            criteria = ""
            expected = TestResults.songs_count
            result = mux.get_count(table, criteria)
            print("get_count songs",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)              
                    
        def test_get_album_count(self):  
            mux = musicGet_Functions(True)
            expected = TestResults.cover_count
            result = mux.get_album_cover_count()
#            print("***** album cover count is ",result)
            self.assertEqual(expected, result, "cover count wrong")
 

    unittest.main()    

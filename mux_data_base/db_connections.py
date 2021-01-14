'''
Created on Aug 7, 2017
for testing data base connectivity
@author: rduvalwa2
'''

import os
import platform
import pymysql.cursors # as connDb

class TestResults:
    if platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net': #wireless name
        cover_count = 1263
        songs_count = 12110
        artist_count = 592
        artist_albums_count = 1242

    elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
        cover_count = 1263
        songs_count = 12110
        artist_count = 592
        artist_albums_count = 1242

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
        login_info_osx = "host='MaxBookPro17OSX.hsd1.wa.comcast.net',user='root',password='blu4jazz',db='Music'"


class musicGet_Functions:   
    def __init__(self,isNotTest):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music')
            self.server = 'MaxBookPro17OSX' 
            self.base = "/Users/rduvalwa2/iTunes/iTunes Media/Music"
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='OSXAir', user='rduvalwa2', password='blu4jazz', db='Music')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
        else:
            print("Host is " , 'default')
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduvalwa2', password='blu4jazz', db='Music')
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
#    import DB_Test_Results
    
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

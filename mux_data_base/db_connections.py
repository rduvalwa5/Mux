'''
Created on Aug 7, 2017
for testing data base connectivity
@author: rduvalwa2
'''
import os
import platform
import MySQLdb  # as connDb
#from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx

class dbInfo:
    def dbSpecs(self):
        USERNAME="rduvalwa2"
        PASSWORD="blu4jazz"
        #HOST="OSXAir.home.home"
        HOST="localhost"
        DATABASE="Music"
        PORT=3306

    def login_spec(self):
        login_info_default = "host='OSXAir.home',user='root',password='blu4jazz',db='Music'"
        #login_info_osxAir = {"host":"OSXAir.home","user":"rduvalwa2","password":"blu4jazz","db":"Music"}
        login_info_osxAir = {"host":"OSXAir.home","user":"rduval","password":"blu4jazz","db":"Music"}
        login_info_xps = "host='OSXAir.home',user='rduval',password='blu4jazz',db='Music'"
        login_info_WIN64_Air = "host='osxair.home.home',user='rduvalwa2',password='blu4jazz',db='Music'"
        login_info_osx = "host='OSXAir.home',user='root',password='blu4jazz',db='Music'"


class musicGet_Functions:   
    def __init__(self,isNotTest):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn  = MySQLdb.connect(host='OSXAir.local',user='rduval',password='blu4jazz',db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home':
            self.conn  = MySQLdb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
            self.conn  = MySQLdb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
#            self.conn  = MySQLdb.connect(host=login_info_osxAir['host'],user=login_info_osxAir['user'],password=login_info_osxAir['password'],db=login_info_osxAir['db'])
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn  = MySQLdb.connect(login_info_WIN64_Air)
        else:
#            self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
            self.conn  = MySQLdb.connect(login_info_default)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
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
            expected = DB_Test_Results.artist_count # 564
            result = mux.get_count(table, criteria)
            print("get_count artist",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
              
        def test_get_count_Artist_Albums(self):
            mux = musicGet_Functions(True)
            table = 'Music.artist_albums'
            criteria = ""
            expected = DB_Test_Results.artist_albums_count  #932
            result = mux.get_count(table, criteria)
            print("get_count albums",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
        def test_get_count_album2Songs(self):
            mux = musicGet_Functions(True)
            table = 'Music.album2songs'
            criteria = ""
            expected = DB_Test_Results.songs_count
            result = mux.get_count(table, criteria)
            print("get_count songs",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)              
                    
        def test_get_album_count(self):  
            mux = musicGet_Functions(True)
            expected = DB_Test_Results.cover_count
            result = mux.get_album_cover_count()
#            print("***** album cover count is ",result)
            self.assertEqual(expected, result, "cover count wrong")
 

    unittest.main()    

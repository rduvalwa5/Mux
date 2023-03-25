'''
Created on Aug 7, 2017
for testing data base connectivity
@author: rduvalwa2
'''

import os
import platform
import pymysql  # as connDb
import Test_Results

class musicGet_Functions:   
    def __init__(self):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'Macbook16.local':
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music_Test')
            self.server = 'MaxBookPro17OSX' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
        elif platform.uname().node == 'OSXAir.local':
            print("Host is " , 'OsxAir')
            self.conn = pymysql.connect(host='OSXAir.local', user='rduvalwa2', password='blu4jazz', db='Music_Test')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
        
        else:
            print('Node is localhost')
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"           
                
    def get_count(self,table = 'Music_Test.album2songs', criteria = " "):
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
        statement = "select count(*)  from `Music_Test`.album_covers;"
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
    
    class TestConnector(unittest.TestCase):
            
        def test_get_count_Artist(self):
            mux = musicGet_Functions()
            table = 'Music_Test.artist'
            criteria = ""
            expected = Test_Results.artist_count
            result = mux.get_count(table, criteria)
            print("get_count artist",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
              
        def test_get_count_Artist_Albums(self):
            mux = musicGet_Functions()
            table = 'Music_Test.artist_albums'
            criteria = ""
            expected = Test_Results.artist_albums_count
            result = mux.get_count(table, criteria)
            print("get_count albums",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
        def test_get_count_album2Songs(self):
            mux = musicGet_Functions()
            table = 'Music_Test.album2songs'
            criteria = ""
            expected = Test_Results.songs_count
            result = mux.get_count(table, criteria)
            print("get_count songs",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)              
                    
        def test_get_album_count(self):  
            mux = musicGet_Functions()
            expected = Test_Results.cover_count
            result = mux.get_album_cover_count()
#            print("***** album cover count is ",result)
            self.assertEqual(expected, result, "cover count wrong")
 

    unittest.main()    

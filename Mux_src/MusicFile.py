'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2
'''
import mysql.connector
from  Musicdb_info import login_info_Albums
from Musicdb_info import login_info_Artist
from mysql.connector.errors import Error


class connection_db:
    def connect_music(self):
        pass


class musicFile:
    def get_select_Album(self, fields, constraints):
        conn = mysql.connector.Connect(**login_info_Albums)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.Albums " + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
#        print(row)
        dbCursor.close()
        conn.close()
        return row

    def get_select_Artist(self, fields, constraints):
        conn = mysql.connector.Connect(**login_info_Albums)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.Artist " + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
#        print(row)
        dbCursor.close()
        conn.close()
        return row        
    
    def get_select_ArtistAlbums(self, fields, constraints):
        conn = mysql.connector.Connect(**login_info_Albums)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.Artist_Albums" + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
#        print(row)
        dbCursor.close()
        conn.close()
        return row        
    
    

if __name__  == '__main__':
    import unittest
    class TestConnector(unittest.TestCase):
 
        def test_get_select_ArtistAlbums(self):
            fields = "count(*)"
            constraints = " "
            expected = 751
            mux = musicFile()
            result = mux.get_select_Album(fields, constraints)
            self.assertEqual(expected,result[0])
 

        def test_get_select_Album(self):
            fields = "count(*)"
            constraints = " "
            expected = 748
            mux = musicFile()
            result = mux.get_select_ArtistAlbums(fields, constraints)
            self.assertEqual(expected,result[0])

        def test_get_select_Artist(self):
            fields = "count(*)"
            constraints = " "
            expected = 441
            mux = musicFile()
            result = mux.get_select_Artist(fields, constraints)
            self.assertEqual(expected,result[0])

    unittest.main()    
    '''
    mux = musicFile()
    fields = "*"
    constraints = "where Albums.index = 3"
    result = mux.get_select_Album(fields, constraints)
    print(result)
    fields = "count(*)"
    constraints = ""
    result = mux.get_select_Album(fields, constraints)
    print(result)
    result = mux.get_select_ArtistAlbums(fields, constraints)
    print(result)
    '''
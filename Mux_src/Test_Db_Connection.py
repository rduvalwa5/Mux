'''
Created on Jan 25, 2018

@author: rduvalwa2
'''
'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2

mysql -u root -b music -p
mysql -u rduvalwa2 -b music -p

'''
from MusicFile import musicFile
import unittest
import mysql.connector
import MySQLdb
from  Musicdb_info import login_info_osxAir
from Musicdb_info import login_info_default
from Musicdb_info import login_info_xps
from mysql.connector.errors import Error


class TestMusicDb(unittest.TestCase):

    '''    
    def test_music_Albums_Rows_XPS(self):
        
        # Test access remote database
        
        db = mysql.connector.Connect(**login_info_xps)
        cursor = db.cursor()
        statement = "select count(*) from Music.artist_albums;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " , row[0])
        expected = 904
        self.assertTrue(row[0] == expected)
        cursor.close()
        db.close()
        
    def test_music_artist_Rows_XPS(self):
        
        # Test access remote database
        
        db = mysql.connector.Connect(**login_info_xps)
        cursor = db.cursor()
        statement = "select count(*) from Music.artist;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " , row[0])
        expected = 536
        self.assertTrue(row[0] == expected)
        cursor.close()
        db.close()
        
    def test_music_song_Rows_XPS(self):
        # Test access remote database
        db = mysql.connector.Connect(**login_info_xps)
        cursor = db.cursor()
        statement = "select count(*) from Music.album2songs;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " , row[0])
        expected = 6596
        self.assertTrue(row[0] == expected)
        cursor.close()
        db.close()


    def testGetMaxArtist(self):
            mux = musicFile()
            table = 'Artist'
            expected = 537
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected, result[0])
               
    def testGetMaxAlbums(self):
            mux = musicFile()
            table = 'artist_albums'
            expected = 909
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected, result[0])
    
    def testGetMaxSongs(self):
            mux = musicFile()
            table = 'album2songs'
            expected = 6624
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected, result[0])
        
    def testGetMaxAlbumSongs(self):
            mux = musicFile()
            table = 'artist_albums'
            expected = 909
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected, result[0])           
   '''       
    def test_connection_Artist_Albums_os_rduvalwa2_music_Albums_Rows(self):
 #       db = MySQLdb.connect(host='localhost', user='root', password='blu4jazz', db='Music')
        db = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        cursor = db.cursor()
        statement = "select count(*) from Music.artist_albums;"
        expected = 970
        try:
            cursor.execute(statement)
            row = cursor.fetchone()
            print("Row is " , row[0])
            self.assertEqual(row[0], expected)
            cursor.close()
            db.close()
        except db.Error as err:
                print("Exception is ", err)
#        db.close()

    def test_connection_Artist_Table_As_Root_localhost(self):
        db = MySQLdb.connect(host='localhost', user='root', password='blu4jazz', db='Music')
        cursor = db.cursor()
        expected = 576
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from Music.Artist;"
        try:
            cursor.execute(statement)
            row = cursor.fetchone()
            print("Row is " , row[0])     
            self.assertTrue(row[0] == expected)
            cursor.close()
        except db.Error as err:
            print("Exception is ", err)
#        db.close()
    
    def test_select_song_type_MusicSongs_By_Criteria(self):
        db = MySQLdb.connect(host='localhost', user='root', password='blu4jazz', db='Music')
        cursor = db.cursor()
        expected = 'Sleep Walk.mp3' # 'Kansas City.mp3'
        statement = 'select Music.album2songs.song from Music.album2songs where album2songs.type = \'tape\';'
        try:
            cursor.execute(statement)
            rows = cursor.fetchall()
#            print("length ", len(rows))
            for i in range(len(rows)):
#                print(rows[i][0])
                if rows[3][0] == expected:
                    self.assertEqual(expected,rows[3][0], 'Not there')
                if rows[3][0] != expected:
                    self.assertEqual(expected,rows[3][0], 'Not there')
                    
        except db.Error as err:
            print("Exception is ", err)

        
    '''
        
    def test_get_select_Albums(self):
        fields = "count(*)"
        constraints = " "
        expected = 909
        mux = musicFile()
        result = mux.get_select_Album(fields, constraints)
        self.assertEqual(expected, result[0])

    def test_get_select_ArtistAlbums(self):
        fields = "count(*)"
        constraints = " "
        expected = 909
        mux = musicFile()
        result = mux.get_select_ArtistAlbums(fields, constraints)
        self.assertEqual(expected, result[0])

    def test_get_select_Artist(self):
        fields = "count(*)"
        constraints = " "
        expected = 537
        mux = musicFile()
        result = mux.get_select_Artist(fields, constraints)
        print("result is ", result[0][0])
        self.assertEqual(expected, result[0][0])
    '''
        
if __name__ == "__main__":
    unittest.main()
    

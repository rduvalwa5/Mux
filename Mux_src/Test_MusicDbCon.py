'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2
'''
from MusicFile import musicFile
import unittest
import mysql.connector
from  Musicdb_info import login_info_Albums
from Musicdb_info import login_info_Artist
from mysql.connector.errors import Error


class TestMusicDb(unittest.TestCase):
    
    
    def test_music_Albums_Rows(self):
        db = mysql.connector.Connect(**login_info_Albums)
        cursor = db.cursor()
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from Music.Albums;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 751)
        cursor.close()
        db.close()

    def test_Music_Artist_RowsJ(self):
        db = mysql.connector.Connect(**login_info_Artist)
        cursor = db.cursor()
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from Music.Artist;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 441)
        cursor.close()
        db.close()

        
    def test_Music_Album_values(self):
        db = mysql.connector.Connect(**login_info_Albums)
        cursor = db.cursor()
#        statement = "select album from Music.Albums where Albums.index = 3;"
        statement = "select * from Music.Albums where Albums.index = 3;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print(row)
#        print("Album is " ,row[0], row[1], row[2])
        self.assertTrue(row[1] == "1st 10 years")
        self.assertTrue(row[0] == 3)
        self.assertTrue(row[2] == 0)
        cursor.close()
        db.close()

    def test_Crud_AlbumTable(self):
        albumName = "Test Album"
        db = mysql.connector.Connect(**login_info_Albums)
        cursor = db.cursor()
        max_index_statement = "select max(Albums.Index) from Music.Albums; "
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        print("Max Index is " ,maxIndex[0])
        indexDb = maxIndex[0] + 1
        insertStatement = "INSERT into Music.Albums (Albums.Album,Albums.Index,Albums.`Artist Id`) values(\""+albumName+"\"," + str(indexDb) + ",801)"
        cursor.execute( insertStatement)
        selectStatement = "select * from Music.Albums where Albums.index = " + str(indexDb) + ";"
        cursor.execute(selectStatement) 
        result = cursor.fetchone()
        print("Result ", result)
        newAlbumName = "NewTestAlbum"
        updateStatement = "UPDATE Music.Albums SET Albums.Album = \"NewTestAlbum\" where Albums.index = " + str(indexDb) +";"
        cursor.execute(updateStatement) 
        cursor.execute(selectStatement) 
        result1 = cursor.fetchone()
        print("Result 1 ", result1)
        deleteStatement = "Delete from Music.Albums where Albums.index = " + str(indexDb) + ";"
        cursor.execute(deleteStatement) 
        cursor.execute(selectStatement) 
        result2 = cursor.fetchone()
        print("Result 2 ", result2)
        cursor.close()
        db.close()
        
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



if __name__ == "__main__":
    unittest.main()
    
    '''
    Finding files... done.
    Importing test modules ... done.
    
    ap
    uid
    pwd
    AP is  password_db UID rduval pwd  reddog
    Row is  40

    '''
'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2
'''
from MusicFile_old import musicFile
import unittest
import mysql.connector
from  Musicdb_info import login_info_rd
from Musicdb_info import login_info_root
from Musicdb_info import login_info_xps
from mysql.connector.errors import Error


class TestMusicDb(unittest.TestCase):
    
    def test_music_Albums_Rows_XPS(self):
        '''
        Test access remote database
        '''
        db = mysql.connector.Connect(**login_info_xps)
        cursor = db.cursor()
        statement = "select count(*) from Music.Albums;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 751)
        cursor.close()
        db.close()

    def test_Crud_AlbumTable_XPS(self):
        '''
        Test Create, Review, Update and Delete to Music.Albums table remote server
        '''
        albumName = "Test Album"
        db = mysql.connector.Connect(**login_info_xps)
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
#        newAlbumName = "NewTestAlbum"
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

    def testGetMaxArtist(self):
            mux = musicFile()
            table = 'Artist'
            expected = 535
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])
               
    def testGetMaxAlbums(self):
            mux = musicFile()
            table = 'artist_albums'
            expected = 900
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])
    
    def testGetMaxSongs(self):
            mux = musicFile()
            table = 'album2songs'
            expected = 6589
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])
        
    def testGetMaxAlbumSongs(self):
            mux = musicFile()
            table = 'artist_albums'
            expected = 900
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])           
    '''       
    def test_music_Albums_Rows(self):
        db = mysql.connector.Connect(**login_info_rd)
        cursor = db.cursor()
        statement = "select count(*) from Music.Albums;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 751)
        cursor.close()
        db.close()
    
    def test_Music_Artist_RowsJ(self):
        db = mysql.connector.Connect(**login_info_root)
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
        db = mysql.connector.Connect(**login_info_rd)
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
        db = mysql.connector.Connect(**login_info_rd)
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
#        newAlbumName = "NewTestAlbum"
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
 
    def test_MusicSongs_By_Criteria(self):
        statement = 'select Music.songs.song from Music.songs where songs.type = \'tape\';'
        mux = musicFile()
        result = mux.select_song_by_criteria(statement)
        for item in result:
            if item == 'Purple Rain.mp3':
                self.assertCountEqual('Purple Rain.mp3',item,'Not there')
        
    def test_get_select_Albums(self):
        fields = "count(*)"
        constraints = " "
        expected = 751
        mux = musicFile()
        result = mux.get_select_Album(fields, constraints)
        self.assertEqual(expected,result[0])

    def test_get_select_ArtistAlbums(self):
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
'''

if __name__ == "__main__":
    unittest.main()
    

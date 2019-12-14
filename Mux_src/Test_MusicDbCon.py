'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2

mysql -u root -b music -p
mysql -u rduvalwa2 -b music -p

'''
import pymysql.cursors
from MusicFile import musicFile
import unittest
from  Musicdb_info import login_info_osxAir
from Musicdb_info import login_info_default
from Musicdb_info import login_info_xps
#from mysql.connector.errors import Error


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

    def test_Crud_AlbumTable_XPS(self):

        db = mysql.connector.Connect(**login_info_xps)
        cursor = db.cursor()
        max_index_statement = "select max(Music.artist_albums.Index) from Music.artist_albums; "
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        print("Max Index is " , maxIndex[0])
        indexDb = maxIndex[0] + 1
        albumName = "Test_album"
        albumArtist = "Test_artist"
        albumGenre = "Test_genre"
        albumType = "Test_type"
        
#                            INSERT into Music.artist_albums (artist_albums.album,artist_albums.artist,artist_albums.genre,artist_albums.Index,artist_albums.type) values("Test_album",Test_artis",Test_genre",905",Test_type);
#       insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(artist[0]) + ",\"" + artist[1] + "\",\""  + "rock" + "\")"
        insertStatement = "INSERT into Music.artist_albums (artist_albums.album,artist_albums.artist,artist_albums.genre,artist_albums.Index,artist_albums.type) values(\"" + albumName + "\",\"" + albumArtist + "\",\"" + albumGenre + "\",\"" + str(indexDb) + "\",\"" + albumType + "\")"
        print("insertStatement ", insertStatement)
        cursor.execute(insertStatement)
        selectStatement = "select * from Music.artist_albums where artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(selectStatement) 
        result = cursor.fetchone()
        print("Result ", result)
        newAlbumName = "NewTestAlbum"
        updateStatement = "UPDATE Music.artist_albums SET artist_albums.album = \"NewTestAlbum\" where artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(updateStatement) 
        cursor.execute(selectStatement) 
        result1 = cursor.fetchone()
        print("Result 1 ", result1)
        deleteStatement = "Delete from Music.artist_albums where artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(deleteStatement) 
        cursor.execute(selectStatement) 
        result2 = cursor.fetchone()
        print("Result 2 ", result2)
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
    def test_music_Albums_Rows(self):
        db = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music')
#        db = mysql.connector.Connect(**login_info_osxAir)
        cursor = db.cursor()
        statement = "select count(*) from Music.artist_albums;"
        try:
            cursor.execute(statement)
            row = cursor.fetchone()
            print("Row is " , row[0])
            self.assertEqual(row[0], 909)
            cursor.close()
            db.close()
        except db.Error as err:
                print("Exception is ", err)
    '''
    def test_Music_Artist_RowsJ(self):
        db = mysql.connector.Connect(**login_info_osxAir)
        cursor = db.cursor()
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from Music.Artist;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " , row[0])
        expected = 537
        self.assertTrue(row[0] == expected)
        cursor.close()
        db.close()
    
    def test_Music_Album_values(self):
        db = mysql.connector.Connect(**login_info_osxAir)
        cursor = db.cursor()
#        statement = "select album from Music.Albums where Albums.index = 3;"
        statement = "select * from Music.artist_albums where artist_albums.index = 337;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print(row)
#        print("Album is " ,row[0], row[1], row[2])
        self.assertTrue(row[0] == 337)
        self.assertTrue(row[1] == 'Joan Baez')
        self.assertTrue(row[2] == "1st 10 years")
        self.assertTrue(row[3] == 'Folk')
        self.assertTrue(row[4] == 'Vinyl')
        cursor.close()
        db.close()
 
    def test_Crud_AlbumTable(self):
        albumName = "Test Album"
        db = mysql.connector.Connect(**login_info_osxAir)
        cursor = db.cursor()
        max_index_statement = "select max(artist_albums.Index) from Music.artist_albums; "
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        print("Max Index is " , maxIndex[0])
        indexDb = maxIndex[0] + 1
        albumName = "Test_album"
        albumArtist = "Test_artist"
        albumGenre = "Test_genre"
        albumType = "Test_type"
        insertStatement = "INSERT into Music.artist_albums (artist_albums.album,artist_albums.artist,artist_albums.genre,artist_albums.Index,artist_albums.type) values(\"" + albumName + "\",\"" + albumArtist + "\",\"" + albumGenre + "\",\"" + str(indexDb) + "\",\"" + albumType + "\")"
        print("insertStatement ", insertStatement)
        cursor.execute(insertStatement)
        selectStatement = "select * from Music.artist_albums where artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(selectStatement) 
        result = cursor.fetchone()
        print("Result ", result)
        newAlbumName = "NewTestAlbum"
        updateStatement = "UPDATE Music.artist_albums SET artist_albums.album = \"NewTestAlbum\" where artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(updateStatement) 
        cursor.execute(selectStatement) 
        result1 = cursor.fetchone()
        print("Result 1 ", result1)
        deleteStatement = "Delete from Music.artist_albums where artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(deleteStatement) 
        cursor.execute(selectStatement) 
        result2 = cursor.fetchone()
        print("Result 2 ", result2)
        cursor.close()
        db.close()
 
    def test_MusicSongs_By_Criteria(self):
        statement = 'select Music.album2songs.song from Music.album2songs where album2songs.type = \'tape\';'
        mux = musicFile()
        result = mux.select_song_by_criteria(statement)
        for item in result:
            if item == 'Purple Rain.mp3':
                self.assertCountEqual('Purple Rain.mp3', item, 'Not there')
        
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
    

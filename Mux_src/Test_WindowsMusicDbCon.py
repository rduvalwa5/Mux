'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2

Use command window as administrator:
C:\Program Files\Python36-32\Scripts>pip install mysqlclient
Collecting mysqlclient
  Using cached mysqlclient-1.3.10-cp36-cp36m-win32.whl
Installing collected packages: mysqlclient
Successfully installed mysqlclient-1.3.10
C:\Program Files\Python36-32\Scripts>


http://connDb.readthedocs.io/en/latest/user/examples.html

connection = connDb.connect(host='OSXAir.home.home',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=connDb.cursors.DictCursor)

'''
from WindowsMusicFile import musicFile
import unittest
import MySQLdb as connDb
from  Musicdb_info import login_info_rd
from Musicdb_info import login_info_root
from Musicdb_info import login_info_xps


class TestMusicDb(unittest.TestCase):
    
    def test_music_Albums_Rows_XPS(self):
        '''
        Test access remote database
        http://zetcode.com/db/mysqlpython/
        '''
        db = connDb.connect(host='OSXAir.home.home',user='rduval',password='blu4jazz',db='Music')
#        db = MySQLdb.Connect(host='OSXAir.home.home',user='rduval',password='blu4jazz',db='Music',charset='utf8mb4',cursorclass=connDb.cursors.DictCursor)
        cursor = db.cursor()
        statement = "select count(*) from Music.artist_albums;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print(row)
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 909)
        cursor.close()
        db.close()

    def test_Crud_AlbumTable_Windows(self):
        albumName = "Test Album"
        db = connDb.connect(host='OSXAir.home.home',user='rduval',password='blu4jazz',db='Music')
#        db = connDb.connect(**login_info_xps)
        cursor = db.cursor()
        max_index_statement = "select max(artist_albums.index) from Music.artist_albums; "
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        print("Max Index is " ,maxIndex[0])
        indexDb = maxIndex[0] + 1
        print(indexDb)
        insertStatement =  "INSERT into Music.artist_albums (artist_albums.album,artist_albums.index,artist_albums.artist,artist_albums.genre,artist_albums.type) values('" + albumName + "',"  + str(indexDb) +  ",'TestArtist','TestGenre','TestType');"
#        insertStatement = "INSERT into Music.artist_albums (artist_albums.album,artist_albums.index,artist_albums.artist,artist_albums.genre,artist_albums.type) values(\""+albumName+"\"," + str(indexDb) + "TestArtist" + "Test_Genre" + "Test_Type" +")"
#        insertStatement = "INSERT into Music.artist_albums (artist_albums.album,artist_albums.index) values(\""+albumName+"\"," + str(indexDb) + ")"
        print("insert statement ", insertStatement)
        cursor.execute(insertStatement)
        selectStatement = "select * from Music.artist_albums where Music.artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(selectStatement) 
        result = cursor.fetchone()
        print("Select Insert Result ", result)
        expected = (910, 'TestArtist', 'Test Album', 'TestGenre', 'TestType')
#        expected =  {'index': 910, 'artist': 'TestArtist', 'album': 'Test Album', 'genre': 'TestGenre', 'type': 'TestType'}
        self.assertEqual(expected, result,"Insert failed")
        newAlbumName = "NewTestAlbum"
        updateStatement = "UPDATE Music.artist_albums SET artist_albums.album = '" + newAlbumName + "' where artist_albums.index = " + str(indexDb) +";"
        cursor.execute(updateStatement)
        selectStatement = "select * from Music.artist_albums where Music.artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(selectStatement) 
        result = cursor.fetchone()
        print("Update Insert Result ", result)
        updateExpected =  (910, 'TestArtist', 'NewTestAlbum', 'TestGenre', 'TestType')
#        expected =  {'index': 910, 'artist': 'TestArtist', 'album': 'NewTestAlbum', 'genre': 'TestGenre', 'type': 'TestType'}
        self.assertEqual(updateExpected, result,"Update failed")
        deleteStatement = "Delete from Music.artist_albums where Music.artist_albums.index = " + str(indexDb) + ";"
        cursor.execute(deleteStatement) 
        cursor.execute(selectStatement) 
        result2 = cursor.fetchone()
        print("Result 2 ", result2)
        self.assertEqual(None, result2,"Delete failed")
        cursor.close()
        db.close()
        

    def testGetMaxArtist(self):
            mux = musicFile()
            table = 'artist'
            expected = 537
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
               
    def testGetMaxAlbums(self):
            mux = musicFile()
            table = 'artist_albums'
            expected = 909
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
 
    def testGetMaxSongs(self):
            mux = musicFile()
            table = 'album2songs'
            expected = 6624
            result = mux.get_max_index(table)
            print(result)
            self.assertEqual(expected,result[0])
       
    def test_music_Albums_Rows(self):
        db = connDb.connect(host='OSXAir.home.home',user='rduval',password='blu4jazz',db='Music')
        cursor = db.cursor()
        statement = "select count(*) from Music.artist_albums;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 909)
        cursor.close()
        db.close()
  
    def test_Music_Artist_RowsJ(self):
        db = connDb.connect(host='OSXAir.home.home',user='rduval',password='blu4jazz',db='Music')
        cursor = db.cursor()
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from Music.Artist;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 537)
        cursor.close()
        db.close()
    
    def test_Music_Album_values(self):
        db = connDb.connect(host='OSXAir.home.home',user='rduval',password='blu4jazz',db='Music')
        cursor = db.cursor()
#        statement = "select album from Music.Albums where Albums.index = 3;"
        statement = "select * from Music.artist_albums where Music.artist_albums.index = 337;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("album values is ", row)
#        print("Album is " ,row[0], row[1], row[2])
        self.assertTrue(row[0] == 337)
        self.assertTrue(row[1] == 'Joan Baez')
        self.assertTrue(row[2] == "1st 10 years")
        self.assertTrue(row[3] == 'Folk')
        self.assertTrue(row[4] == 'Vinyl')        
        cursor.close()
        db.close()
 
    def test_MusicSongs_By_Criteria(self):
        statement = 'select Music.album2songs.album from Music.album2songs where Music.album2songs.type = \'tape\';'
        mux = musicFile()
        result = mux.select_song_by_criteria(statement)
        print("list size ", len(result))
        self.assertEqual(24,len(result),'list size wrong')
        for item in result:
            if item == 'Purple Rain.mp3':
                self.assertCountEqual('Purple Rain.mp3',item,'Not there')
        
    '''
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
    

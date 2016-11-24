'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2
'''
import mysql.connector
from  Musicdb_info import login_info_rd
from Musicdb_info import login_info_root
from mysql.connector.errors import Error


class connection_db:
    def connect_music(self):
        pass


class musicFile:
    def get_max_index(self, table):
        self.table = '`Music`.' + table
#        print(self.table)       
        self.tableIndex = table + "." + 'Index'
#        print(self.tableIndex)
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
#        print(max_index_statement)
        conn = mysql.connector.Connect(**login_info_rd)
        cursor = conn.cursor()
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        conn.close()   
        return maxIndex

    def get_select_Album(self, fields, constraints):
        conn = mysql.connector.Connect(**login_info_rd)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.Albums " + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
#        print(row)
        dbCursor.close()
        conn.close()
        return row

    def get_select_Artist(self, fields, constraints):
        conn = mysql.connector.Connect(**login_info_rd)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.Artist " + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
#        print(row)
        dbCursor.close()
        conn.close()
        return row        
    
    def get_select_ArtistAlbums(self, fields, constraints):
        conn = mysql.connector.Connect(**login_info_rd)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.Artist_Albums" + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
#        print(row)
        dbCursor.close()
        conn.close()
        return row        
    
    def create_Artist(self,artist):
        self.artist = artist
        conn = mysql.connector.Connect(**login_info_rd)
        
#        db = mysql.connector.Connect(**login_info_xps)
        cursor = conn.cursor()
        max_index_statement = "select max(Artist.Index) from Music.Artist; "
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        indexDb = maxIndex[0] + 1
      
#        insertStatement = "INSERT into Music.Albums (Albums.Album,Albums.Index,Albums.`Artist Id`) values(\""+albumName+"\"," + str(indexDb) + ",801)"
        insertStatement = "INSERT into Music.Artist (Artist.Artist, Artist.Index) values(\""+self.artist+"\"," + str(indexDb) + ")"
        cursor.execute( insertStatement)
        selectStatement = "select * from Music.Artis where Artis.index = " + str(indexDb) + ";"
        cursor.execute(selectStatement) 
        result = cursor.fetchone()
        print("Result ", result)
        cursor.close()
        conn.close()
        return result


    def delete_record_Artist(self,artist):
        self.artist = artist
        self.index = artist
        conn = mysql.connector.Connect(**login_info_rd)
        cursor = conn.cursor()
        selectStatement = "select Index from Music.Artis where Artis.Artist = " + artist + ";"
        cursor.execute(selectStatement) 
        index = cursor.fetchone()
        deleteStatement = "Delete from Music.Artist where Artist.index = " + str(index) + ";"
        cursor.execute(deleteStatement) 
        cursor.execute(selectStatement) 
        result2 = cursor.fetchone()
        print("Result 2 ", result2)
        cursor.close()
        conn.close()

    def select_song_by_criteria(self,statement):
        '''
        Select a song or songs by criteria.
        '''
        rows = []
        db = mysql.connector.Connect(**login_info_rd)
        cursor = db.cursor()
        self.statement = statement
        print(statement)
        cursor.execute(statement)
        row = cursor.fetchone()
        while row is not None:
                rows.append(row)
                row = cursor.fetchone()
        cursor.close()
        db.close()
        return rows



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

        def testGetMaxArtist(self):
            mux = musicFile()
            table = 'Artist'
            expected = 441
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])
            
        def testGetMaxAlbums(self):
            mux = musicFile()
            table = 'Albums'
            expected = 751
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])

        def testGetMaxSongs(self):
            mux = musicFile()
            table = 'songs'
            expected = 6578
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
            self.assertEqual(expected,result[0])
            
        def testGetMaxAlbumSongs(self):
            mux = musicFile()
            table = 'album_songss'
            expected = 6578
#            mux.get_max_index(table)
            result = mux.get_max_index(table)
            print(result[0])
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
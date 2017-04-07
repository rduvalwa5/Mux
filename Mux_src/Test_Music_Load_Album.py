'''
'''
import unittest 
#from Musicdb_info import login_info_root
#from Musicdb_info import login_info_osx 
#import mysql.connector
import os, platform
#import self.conn.Error
import MySQLdb   as connDb
import Music_Get_Functions
from  Music_Load import musicLoad_Functions, song_Add_Update_Delete, album_Add_Update_Delete, artist_Add_Update_Delete

class Test_MusicLoad(unittest.TestCase):
        def setUp(self):
#   self.albumAddUpDel.add_album(self.album,self.addArtist,self.addType,self.addGenre)

            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
            self.albumAddUpDel = album_Add_Update_Delete(False)
            self.artistAdd = 'Test_Add_Artist'
            self.genreAdd = 'Add_Gen'
            self.albumAdd = 'Test_Add_Album'
            self.typeAdd = 'Add_Type'
            
    # Update attributes
            self.song = 'Song_Song.mp3'    
 
            self.addAlbum = 'Test_SongAlbum'
            self.addType = 'Song_Type'
            self.addArtist = 'Song_Artist'
            self.addGenre = 'Song_genre'
            self.addServer = 'song_server'
            self.addPath = '/Test/Music'

            self.albumUpdate = 'Up_SongAlbum'
            self.typeUpdate = 'Up_Song_Type'
            self.artistUpdate = 'Up_Song_Artist'
            self.genreUpdate = 'Up_Song_genre'
            self.serverUpdate = 'up_song_server'
            self.pathUpdate = '/Test/Up_Music'
            
        def tearDown(self):
            self.Restore_testAlbum()
            self.albumAddUpDel.dbConnectionClose()
            self.getInfo.dbConnectionClose()
        
        """
            Test Artist_Albums Table Functions
        """  
        
        def test_DoesAlbumExist_True(self):
            expected = "True" 
            album = 'Heart Like A Wheel'
            result = self.albumAddUpDel.doesAlbumExist(album)
            self.assertEqual(expected,result, "Result expected True but was False")  
  
        def test_DoesAlbumExist_False(self):
            expected = "False" 
            album = "Long Long Road"
            result = self.albumAddUpDel.doesAlbumExist(album)
            self.assertEqual(expected,result, "Result expected False but was True")  
            
        """
            Test Support Functions
        """                    
        def Restore_testAlbum(self):   
            print("*************** Node Name is ",platform.uname().node)
            if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
                self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')

            elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
                self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
                self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
            else:
                self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')

            statement = "UPDATE `Music`.artist_albums SET artist = 'ZZ_ZTest',genre = 'Test GenX',type = 'TestTape' WHERE album = 'Test_AlbumA';"
            print(statement)
            self.albumAddUpDel.conn 
            cursor = self.conn.cursor()
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
            cursor.close()
            self.conn.close()
       
                    
'''
        def test_Add_Album(self):
            """
             Test Add Album to artist_albums table.
            """
            self.albumAddUpDel.add_album(self.albumAdd,self.artistAdd,self.typeAdd,self.genreAdd)
            result = self.getInfo.get_Album_from_ArtistAlbums(self.albumAdd)
            self.assertEqual(self.artistAdd, result[0][1], "artist does not match")
            self.assertEqual(self.albumAdd, result[0][2], "album does not match")
            self.assertEqual(self.genreAdd, result[0][3], "genre does not match")
            self.assertEqual(self.typeAdd, result[0][4], "type does not match")
         
        def test_Update_Album_Artist(self):
            """
            update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
            """
            update_artist = 'ZZ Top'
            test_album = 'Test_AlbumA'
            
            self.albumAddUpDel.update_album(test_album, update_artist)
            result = self.getInfo.get_Album_from_ArtistAlbums(test_album)
            print("update result is ", result)
            self.assertEqual(update_artist, result[0][1], "album update artist failed")
            self.assertEqual(test_album, result[0][2], 'album name is wrong')
        
        def test_Update_Album_Artist_genre(self):
            """
            update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
            """
            original_artist = 'ZZ_ZTest'
            update_artist = 'no_change'
            test_album = 'Test_AlbumA'
            update_genre = 'up_genre'
            
            self.albumAddUpDel.update_album(test_album, update_artist,update_genre)
            result = self.getInfo.get_Album_from_ArtistAlbums(test_album)
            print("update result is ", result)
            self.assertEqual(original_artist, result[0][1], "album update artist failed")
            self.assertEqual(update_genre, result[0][3], 'genre failed')
            self.assertEqual(test_album, result[0][2], 'album name is wrong')
        
        def test_Update_Album_type(self):
            """
            update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
            """
            original_artist = 'ZZ_ZTest'
            original_genre = 'Test GenX'
            test_album = 'Test_AlbumA'
            update_type = 'Up_Type'
            
            self.albumAddUpDel.update_album(test_album, 'no_change','no_change',update_type)
            result = self.getInfo.get_Album_from_ArtistAlbums(test_album)
            print("update result is ", result)
            self.assertEqual(original_artist, result[0][1], "album update artist failed")
            self.assertEqual(original_genre, result[0][3], 'genre failed')
            self.assertEqual(test_album, result[0][2], 'album name is wrong')
            self.assertEqual(update_type, result[0][4], 'type failed')

        def test_Delete_Album(self): 
            self.albumAddUpDel.delete_album(self.albumAdd)
            result = self.getInfo.get_Album_from_ArtistAlbums(self.albumAdd)
            print(result)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")   
            
'''
                               

                 
if __name__ == "__main__":
    unittest.main()
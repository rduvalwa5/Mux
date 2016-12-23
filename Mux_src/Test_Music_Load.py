'''
'''
import unittest 
from Musicdb_info import login_info_root
from Musicdb_info import login_info_osx 
import mysql.connector
import os
import Music_Get_Functions
from  Music_Load import musicLoad_Functions, song_Add_Update_Delete, album_Add_Update_Delete, artist_Add_Update_Delete

class Test_MusicLoad(unittest.TestCase):
        def setUp(self):
            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
            self.addArtistInfo = artist_Add_Update_Delete()
            self.addAlbum = album_Add_Update_Delete()
            self.arts = 'Test_Add_Artist'
            self.genre = 'Add_Gen'
            self.album = 'Test_Add_Album'
            self.tipe = 'Add_Type'
            
        def tearDown(self):
            self.Restore_testAlbum()
            self.addArtistInfo.dbConnectionClose()
            self.addAlbum.dbConnectionClose()
            self.getInfo.dbConnectionClose()
         
        """
            Test Artist Table Functions
        """
            
        def test_Add_Artist(self): 
            self.addArtistInfo.add_artist(self.arts ,self.genre)
            result = self.getInfo.get_artist_from_artistTable(self.arts)
            print("Add artist result ",result)
            self.assertEqual(self.arts,result[0][1],"artist name add failed")
            self.assertEqual(self.genre,result[0][2],"artist genre add failed")           
            
        def testDoesArtistAlreadyExist_False(self):
            expected = "False" 
            result = self.addArtistInfo.doesArtistExist("Bill Wither")
            self.assertEqual(expected,result, "Result expected False but was True")  
            
        def testDoesArtistAlreadyExist_True_(self):
            testArtist = "Bill Withers"
            testIndex = 42
            expected = "True" 
            result = self.addArtistInfo.doesArtistExist("Bill Withers")
            self.assertEqual(expected,result, "Result expected True but was False")   
            self.addArtistInfo.add_artist(testArtist,self.genre)
            result = self.getInfo.get_artist_from_artistTable("Bill Withers")
            self.assertEqual(testIndex,result[0][0],"artist index not " + str(testIndex))
            self.assertEqual(testArtist,result[0][1],"artist not in data table")
            
        def test_update_date_artist_genre_update(self):
            newGenre = "Update"
            updateArtist = "Bill Withers"
            self.addArtistInfo.update_artist(updateArtist, newGenre)
            result = self.getInfo.get_artist_from_artistTable(updateArtist)
            print("Update result newGenre",result)
            self.assertEqual(newGenre,result[0][2],"genre update failed") 
         
        def test_update_date_artist_genre_rock(self): 
            '''
            This test retores the updated record
            '''
            original = 'Rock'
            updateArtist = "Bill Withers"      
            self.addArtistInfo.update_artist(updateArtist, original)
            result = self.getInfo.get_artist_from_artistTable(updateArtist)
            print("Update result Rock",result)
            self.assertEqual(original,result[0][2],"genre update failed")               
            
        def test_Delete_Artist(self): 
            self.addArtistInfo.delete_artist(self.arts)
            result = self.getInfo.get_artist_from_artistTable(self.arts)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")  
         
        """
            Test Artist_Albums Table Functions
        """  
        def test_DoesAlbumExist_True(self):
            expected = "True" 
            album = 'Heart Like A Wheel'
            result = self.addAlbum.doesAlbumExist(album)
            self.assertEqual(expected,result, "Result expected True but was False")  
  
        def test_DoesAlbumExist_False(self):
            expected = "False" 
            album = "Long Long Road"
            result = self.addAlbum.doesAlbumExist(album)
            self.assertEqual(expected,result, "Result expected False but was True")          

        def test_Add_Album(self):
            '''
             Test Add Album to artist_albums table.
            '''
            self.addAlbum.add_album(self.album,self.arts,self.tipe,self.genre)
            result = self.getInfo.get_Album_from_ArtistAlbums(self.album)
            self.assertEqual(self.arts, result[0][1], "artist does not match")
            self.assertEqual(self.album, result[0][2], "album does not match")
            self.assertEqual(self.genre, result[0][3], "genre does not match")
            self.assertEqual(self.tipe, result[0][4], "type does not match")
         
        def test_Update_Album_Artist(self):
            '''
            update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
            '''
            update_artist = 'ZZ Top'
            test_album = 'Test_AlbumA'
            
            self.addAlbum.update_album(test_album, update_artist)
            result = self.getInfo.get_Album_from_ArtistAlbums(test_album)
            print("update result is ", result)
            self.assertEqual(update_artist, result[0][1], "album update artist failed")
            self.assertEqual(test_album, result[0][2], 'album name is wrong')

        def test_Update_Album_Artist_genre(self):
            '''
            update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
            '''
            original_artist = 'ZZ_ZTest'
            update_artist = 'no_change'
            test_album = 'Test_AlbumA'
            update_genre = 'up_genre'
            
            self.addAlbum.update_album(test_album, update_artist,update_genre)
            result = self.getInfo.get_Album_from_ArtistAlbums(test_album)
            print("update result is ", result)
            self.assertEqual(original_artist, result[0][1], "album update artist failed")
            self.assertEqual(update_genre, result[0][3], 'genre failed')
            self.assertEqual(test_album, result[0][2], 'album name is wrong')

        def test_Update_Album_type(self):
            '''
            update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
            '''
            original_artist = 'ZZ_ZTest'
            original_genre = 'Test GenX'
            test_album = 'Test_AlbumA'
            update_type = 'Up_Type'
            
            self.addAlbum.update_album(test_album, 'no_change','no_change',update_type)
            result = self.getInfo.get_Album_from_ArtistAlbums(test_album)
            print("update result is ", result)
            self.assertEqual(original_artist, result[0][1], "album update artist failed")
            self.assertEqual(original_genre, result[0][3], 'genre failed')
            self.assertEqual(test_album, result[0][2], 'album name is wrong')
            self.assertEqual(update_type, result[0][4], 'type failed')

        def test_Delete_Album(self): 
            self.addAlbum.delete_album(self.album)
            result = self.getInfo.get_Album_from_ArtistAlbums(self.album)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")   
            
              
        """
            Test Album_Songs Table Functions
        """ 
        
        def test_Add_Song(self):
            pass
        
        def test_update_song_artist(self):
            pass

        def test_update_song_album(self):
            pass                
 
        def test_update_song_server(self):
            pass            
 
        def test_update_song_path(self):
            pass 

        def test_update_song_genre(self):
            pass   
        
        def test_update_song_type(self):
            pass
        
        def test_delete_song(self):
            pass          
              
        
                   
        """
            Test Support Functions
        """                    
        def Restore_testAlbum(self):   
            if os.uname().nodename == 'C1246895-osx.home':
                self.conn = mysql.connector.Connect(**login_info_osx)
            elif  os.uname().nodename == 'OSXAir.home.home':
                self.conn = mysql.connector.Connect(**login_info_root)

            statement = "UPDATE `Music`.artist_albums SET artist = 'ZZ_ZTest',genre = 'Test GenX',type = 'TestTape' WHERE album = 'Test_AlbumA';"
            print(statement)
            self.addAlbum.conn 
            cursor = self.conn.cursor()
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
            cursor.close()
            self.conn.close()
            
                 
if __name__ == "__main__":
    unittest.main()
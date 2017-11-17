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
#   self.albumAddUpDel.add_album(self.album,self.addArtist,self.addType,self.addGenre)

            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
            self.addArtistInfo = artist_Add_Update_Delete()
            self.albumAddUpDel = album_Add_Update_Delete()
            self.songAUD = song_Add_Update_Delete()
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
            self.addArtistInfo.dbConnectionClose()
            self.albumAddUpDel.dbConnectionClose()
            self.getInfo.dbConnectionClose()
            self.songAUD.dbConnectionClose()
         
        """
            Test Artist Table Functions
        """
            
        def test_Add_Artist(self): 
            self.addArtistInfo.add_artist(self.artistAdd , self.genreAdd)
            result = self.getInfo.get_artist_from_artistTable(self.artistAdd)
            print("Add artist result ", result)
            self.assertEqual(self.artistAdd, result[0][1], "artist name add failed")
            self.assertEqual(self.genreAdd, result[0][2], "artist genre add failed")           
            
        def testDoesArtistAlreadyExist_False(self):
            expected = "False" 
            result = self.addArtistInfo.doesArtistExist("Bill Wither")
            self.assertEqual(expected, result, "Result expected False but was True")  
            
        def testDoesArtistAlreadyExist_True_(self):
            testArtist = "Bill Withers"
            testIndex = 42
            expected = "True" 
            result = self.addArtistInfo.doesArtistExist("Bill Withers")
            self.assertEqual(expected, result, "Result expected True but was False")   
            self.addArtistInfo.add_artist(testArtist, self.addGenre)
            result = self.getInfo.get_artist_from_artistTable("Bill Withers")
            self.assertEqual(testIndex, result[0][0], "artist index not " + str(testIndex))
            self.assertEqual(testArtist, result[0][1], "artist not in data table")
            
        def test_update_date_artist_genre_update(self):
            newGenre = "Update"
            updateArtist = "Bill Withers"
            self.addArtistInfo.update_artist(updateArtist, newGenre)
            result = self.getInfo.get_artist_from_artistTable(updateArtist)
            print("Update result newGenre", result)
            self.assertEqual(newGenre, result[0][2], "genre update failed") 
         
        def test_update_date_artist_genre_rock(self): 
            '''
            This test retores the updated record
            '''
            original = 'Rock'
            updateArtist = "Bill Withers"      
            self.addArtistInfo.update_artist(updateArtist, original)
            result = self.getInfo.get_artist_from_artistTable(updateArtist)
            print("Update result Rock", result)
            self.assertEqual(original, result[0][2], "genre update failed")               
            
        def test_Delete_Artist(self): 
            self.addArtistInfo.delete_artist(self.artistAdd)
            result = self.getInfo.get_artist_from_artistTable(self.artistAdd)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")  
         
        """
            Test Artist_Albums Table Functions
        """  
        
        def test_DoesAlbumExist_True(self):
            expected = "True" 
            album = 'Heart Like A Wheel'
            result = self.albumAddUpDel.doesAlbumExist(album)
            self.assertEqual(expected, result, "Result expected True but was False")  
  
        def test_DoesAlbumExist_False(self):
            expected = "False" 
            album = "Long Long Road"
            result = self.albumAddUpDel.doesAlbumExist(album)
            self.assertEqual(expected, result, "Result expected False but was True")          

        def test_Add_Album(self):
            """
             Test Add Album to artist_albums table.
            """
            self.albumAddUpDel.add_album(self.albumAdd, self.artistAdd, self.typeAdd, self.genreAdd)
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
            
            self.albumAddUpDel.update_album(test_album, update_artist, update_genre)
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
            
            self.albumAddUpDel.update_album(test_album, 'no_change', 'no_change', update_type)
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
                      
        """
            Test Album_Songs Table Functions
        """ 
        
        def test_Add_Song(self):
            """
             insert into `Music`.album2songs (album2songs.index, album, artist,genre,path,server,song,type) 
             values (6599,'SongAlbum','SongArts','SongGenre','/path/path/','song_server','Song_Song.mp3','test_type');
             [(6599, 'song_server', '/Test/Music', 'Song_Artist', 'Test_SongAlbum', 'Song_Song.mp3', 'Song_genre', 'Song_Type')]
            """
            self.songAUD.add_song(self.addAlbum, self.addArtist, self.addGenre, self.song, self.addType, self.addPath, self.addServer)
            addSongResult = self.getInfo.get_song_by_song(self.song)
            print(addSongResult)
            self.assertEqual(self.addServer, addSongResult[0][1], "Server failed")
            self.assertEqual(self.addPath, addSongResult[0][2], "path failed")
            self.assertEqual(self.addArtist, addSongResult[0][3], "artist failed")
            self.assertEqual(self.addAlbum, addSongResult[0][4], "album failed")
            self.assertEqual(self.song, addSongResult[0][5], "song failed")
            self.assertEqual(self.addGenre, addSongResult[0][6], "genre failed")           
            self.assertEqual(self.addType, addSongResult[0][7], "album failed")
            
        def test_update_song_artist(self):
            """
            "UPDATE `Music`.album2songs SET artist = '" + artist + "' WHERE song = '" + song  + "';"
             [(6599, 'song_server', '/Test/Music', 'Song_Artist', 'Test_SongAlbum', 'Song_Song.mp3', 'Song_genre', 'Song_Type')]
            """
            self.songAUD.update_song_artist(self.artistUpdate, self.song)
            updateArtistResult = self.getInfo.get_song_by_song(self.song)
            print(updateArtistResult)
            self.assertEqual(self.artistUpdate, updateArtistResult[0][3], "update artist failed")
            
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
            self.songAUD.delete_song(self.song)
            deleteSongResult = self.getInfo.get_song_by_song(self.song)
#            print(deleteSongResult)
            expected = []
            self.assertListEqual(expected, deleteSongResult, "list is not empty")  
                   
        """
            Test Support Functions
        """                    

        def Restore_testAlbum(self):   
            if os.uname().nodename == 'C1246895-osx.home':
                conn = mysql.connector.Connect(**login_info_osx)
            elif  os.uname().nodename == 'OSXAir.home.home':
                conn = mysql.connector.Connect(**login_info_root)

            statement = "UPDATE `Music`.artist_albums SET artist = 'ZZ_ZTest',genre = 'Test GenX',type = 'TestTape' WHERE album = 'Test_AlbumA';"
            print(statement)
#            self.albumAddUpDel.conn 
            cursor = conn.cursor()
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
            cursor.close()
            conn.close()
            
                 
if __name__ == "__main__":
    unittest.main()

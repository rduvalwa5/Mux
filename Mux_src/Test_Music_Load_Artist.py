'''
'''
import unittest 
from Musicdb_info import login_info_root
from Musicdb_info import login_info_osx 
import mysql.connector
import os
import Music_Get_Functions
from  Music_Load import musicLoad_Functions, song_Add_Update_Delete, album_Add_Update_Delete, artist_Add_Update_Delete


class Test_MusicLoadArtistTable(unittest.TestCase):

        def setUp(self):
#   self.albumAddUpDel.add_album(self.album,self.addArtist,self.addType,self.addGenre)

            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
            self.addArtistInfo = artist_Add_Update_Delete()
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
            self.addArtistInfo.dbConnectionClose()
            self.getInfo.dbConnectionClose()
         
        """
            Test Artist Table Functions
        """
            
        def test_1_Add_Artist(self): 
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
            
        def test_2_update_date_artist_genre_update(self):
            newGenre = "Update"
            updateArtist = "Bill Withers"
            self.addArtistInfo.update_artist(updateArtist, newGenre)
            result = self.getInfo.get_artist_from_artistTable(updateArtist)
            print("Update result newGenre", result)
            self.assertEqual(newGenre, result[0][2], "genre update failed") 
         
        def test_3_update_date_artist_genre_rock(self): 
            '''
            This test retores the updated record
            '''
            original = 'Rock'
            updateArtist = "Bill Withers"      
            self.addArtistInfo.update_artist(updateArtist, original)
            result = self.getInfo.get_artist_from_artistTable(updateArtist)
            print("Update result Rock", result)
            self.assertEqual(original, result[0][2], "genre update failed")               
            
        def test_4_Delete_Artist(self): 
            self.addArtistInfo.delete_artist(self.artistAdd)
            result = self.getInfo.get_artist_from_artistTable(self.artistAdd)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")  

                 
if __name__ == "__main__":
    unittest.main()

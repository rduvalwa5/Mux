'''
'''
import unittest 
import Music_Get_Functions
from  Music_Load import musicLoad_Functions, song_Add_Update_Delete, album_Add_Update_Delete, artist_Add_Update_Delete

class Test_MusicLoad(unittest.TestCase):
        def setUp(self):
            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
            self.addArtistInfo = artist_Add_Update_Delete()
            self.addAlbum = album_Add_Update_Delete()
            self.arts = 'ZZ_ZTestX'
            self.genre = 'Test GenX'
            self.album = 'Test_Album1X'
            self.tipe = 'TestTape'
            self.albums = ['Test_AlbumA','Test_AlbumB','Test_AlbumC']
            
        def tearDown(self):
            self.addArtistInfo.dbConnectionClose()
            self.addAlbum.dbConnectionClose()
            self.getInfo.dbConnectionClose()
            
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
         

         
        def test_Delete_Album(self): 
            self.addAlbum.delete_album(self.album)
            result = self.getInfo.get_Album_from_ArtistAlbums(self.album)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")   
            
            
if __name__ == "__main__":
    unittest.main()
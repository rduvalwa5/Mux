'''
Created on Oct 27, 2017

@author: rduvalwa2
'''
import unittest
import Test_Results
from Music_Get_Functions import musicGet_Functions
    
class TestGetFunctions(unittest.TestCase):
    
        '''
        Test Get Max Rows
        '''
            
        def testGetMaxIndex_Artist(self):
            mux = musicGet_Functions(True)
            table = 'artist'
            expected = Test_Results.get_max_index_artist # 565
            result = mux.get_max_index(table)
            mux.dbConnectionClose()
            self.assertEqual(expected,result[0])
            
        def testGetMaxIndex_Albums(self):
            mux = musicGet_Functions(True)
            table = 'artist_albums'
            expected = Test_Results.get_max_index_albums # 978
            result = mux.get_max_index(table)
            mux.dbConnectionClose()
            self.assertEqual(expected,result[0])

        def testGetMaxIndex_Songs(self):
            mux = musicGet_Functions(True)
            table = 'album2songs'
            expected = Test_Results.get_max_index_songs #6830
            result = mux.get_max_index(table)
            mux.dbConnectionClose()
            self.assertEqual(expected,result[0])
        
        '''
        Test type counts
        '''       
        def test_type_count(self):
            mux = musicGet_Functions(True)
            for tipe in Test_Results.typeList:
                print("Type IS...", tipe[0])
                expected = tipe[1]
                result =  mux.get_type_count(tipe[0])
                print(result)
                self.assertEqual(expected, result) 
                
        '''
        Test genre counts
        '''                      
        def test_genre_count(self):
            mux = musicGet_Functions(True)
            gList = Test_Results.genreList
            for gen in gList:
                expected = gen[1]
                print("expect for genre ", gen[0])
                result = mux.get_genre_count(gen[0])
                self.assertEqual(expected,result)

        '''
        Test get counts
        '''         
        def test_get_all_songs(self):
            mux = musicGet_Functions(True)
            expected = Test_Results.songs_count  # 6831
            result = mux.get_AllSongs()
            print("All songs count is ", len(result))
            print(result[0])
            self.assertEqual(expected, len(result),"Song count is wrong")
        
        def test_get_count_Artist(self):
            mux = musicGet_Functions(True)
            table = 'Music.artist'
            criteria = ""
            expected = Test_Results.artist_count # 564
            result = mux.get_count(table, criteria)
            print("get_count artist",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
              
        def test_get_count_Artist_Albums(self):
            mux = musicGet_Functions(True)
            table = 'Music.artist_albums'
            criteria = ""
            expected = Test_Results.artist_albums_count  #954
            result = mux.get_count(table, criteria)
            print("get_count albums",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
        def test_get_count_album2Songs(self):
            mux = musicGet_Functions(True)
            table = 'Music.album2songs'
            criteria = ""
            expected = Test_Results.songs_count
            result = mux.get_count(table, criteria)
            print("get_count songs",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)    
            
        def test_get_album_cover_count(self):  
            mux = musicGet_Functions(True)
            expected = Test_Results.cover_count
            result = mux.get_album_cover_count()
            self.assertEqual(expected, result, "cover count wrong")
                    
        def test_get_all_folk_albums(self):
            expected = Test_Results.folk_albums # 576
            mux = musicGet_Functions(True)
            result = mux.get_all("`Music`.artist_albums.album", "`Music`.artist_albums","where `Music`.artist_albums.genre like 'Folk'" )
            print(len(result))
            self.assertEqual(expected, len(result))

        def test_get_all_folk_songs(self):
            expected = Test_Results.folk_songs # 576
            mux = musicGet_Functions(True)
            result = mux.get_all("`Music`.album2songs.album, `Music`.album2songs.artist", "`Music`.album2songs","where `Music`.album2songs.genre like 'folk'" )
            print(len(result))
            self.assertEqual(expected, len(result))
       
        def test_artist_album_song_exist(self):
            mux = musicGet_Functions(False)
            expected = False
            result = mux.test_artist_album_song_exist('Ten Years After', 'A Space In Time', '04 Over the Hill.m4p')
            print('Expect False ', result)
            self.assertFalse(expected, result)

        def test_artist_album_song_Notexist(self):
            mux = musicGet_Functions(True)
            expected = True
            result = mux.test_artist_album_song_exist('Ten Years After', 'A Space In Time', '09 Over the Hill.m4p')
            print('Expect True ', result)
            self.assertTrue(expected, result)
        '''
        DATABASE CRUD TEST
        '''
        '''            
        def test_Add_Song(self):
            mux = musicGet_Functions(True)
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            result = mux.add_one_song(artist, album, song)
            print("add song result is ", result)
            self.assertEqual(result,"Success" )

        def test_delete_songs(self):
            mux = musicGet_Functions(True)
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            expected = song + " deleted"
            result = mux.delete_one_song(artist, album, song)
            self.assertEqual(expected,result)            
        '''
        def test_get_Song(self):
            thisSong = 'Johnny B. Goode.mp3'
#            thisAlbum = 'The Best of Chuck Berry'
            mux = musicGet_Functions(True)
#            expected =  (946, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
            expected = Test_Results.get_song
            result = mux.get_song(thisSong)
            print("song result is ",result[0])
            self.assertEqual(expected,result[0])
                             
        def test_get_Album(self):
            mux = musicGet_Functions(True)
            album = 'A Space In Time'
            expected = Test_Results.get_album  # (664, 'Ten Years After', 'A Space In Time', 'Blues', 'Download')
            result = mux.get_album(album)
            self.assertEqual(expected,result[0])

        def test_get_all_albums(self):
            mux = musicGet_Functions(True)
            result = mux.get_all_albums()
            expected = Test_Results.artist_albums_count
            print("all albums ", result)
            print("length all albums", len(result))
            self.assertEqual(expected, len(result),"All album count wrong")

        def test_get_Artist(self):
            mux = musicGet_Functions(True)
            expected = Test_Results.get_artist   # (411, 'Ten Years After', 'Blues')
            result = mux.get_artist('Ten Years After')
            self.assertEqual(expected,result[0])
        
        def test_get_artistAlbums_from_Albums(self):
            mux = musicGet_Functions(True)
            expected =  Test_Results.get_artist_albums
 #           ((664, 'Ten Years After', 'A Space In Time', 'Blues', 'Download'), (665, 'Ten Years After', 'Recorded Live', 'Blues', 'Download'), (666, 'Ten Years After', 'Undead (Remastered) [Live]', 'Rock', 'Download'),(1064, 'Ten Years After', 'Stonedhenge (Re-Presents)', 'Rock', 'Download'))
            result = mux.get_artistAlbums_fromAlbums('Ten Years After')
            print("artistAlbums 726 ", result)
            self.assertEqual(expected, result)
        
        def test_get_album_songs(self):
            mux = musicGet_Functions(True)
            expected = Test_Results.get_artist_albums_songs
          #  (('01 One of These Days.m4p',), ('02 Here They Come.m4p',), ("03 I'd Love to Change the World.m4p",), ('04 Over the Hill.m4p',), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p",), ('06 Once There Was a Time.m4p',), ('07 Let the Sky Fall.m4p',), ('08 Hard Monkeys.m4p',), ("09 I've Been There Too.m4p",), ('10 Uncle Jam.m4p',))
            result = mux.get_album_songs('A Space In Time')
            print("artist albums ", result)
            self.assertEqual(expected, result, "song list for A Space In Time wrong" )

        def test_get_artist_songs(self):
            mux = musicGet_Functions(True)
            expected = Test_Results.get_artist_songs
            # (('01 One of These Days.m4p', 'A Space In Time'), ('02 Here They Come.m4p', 'A Space In Time'), ("03 I'd Love to Change the World.m4p", 'A Space In Time'), ('04 Over the Hill.m4p', 'A Space In Time'), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p", 'A Space In Time'), ('06 Once There Was a Time.m4p', 'A Space In Time'), ('07 Let the Sky Fall.m4p', 'A Space In Time'), ('08 Hard Monkeys.m4p', 'A Space In Time'), ("09 I've Been There Too.m4p", 'A Space In Time'), ('10 Uncle Jam.m4p', 'A Space In Time'), ('01 One of These Days Live.m4p', 'Recorded Live'), ('02 You Give Me Loving.m4p', 'Recorded Live'), ('03 Good Morning Little Schoolgirl.m4p', 'Recorded Live'), ('04 Help Me.m4p', 'Recorded Live'), ('05 Classical Thing.m4p', 'Recorded Live'), ('06 Scat Thing.m4p', 'Recorded Live'), ("07 I Can't Keep from Cryin' Sometimes.m4p", 'Recorded Live'), ("09 I Can't Keep from Cryin' (Cont'd).m4p", 'Recorded Live'), ('10 Silly Thing.m4p', 'Recorded Live'), ("11 Slow Blues In 'C'.m4p", 'Recorded Live'), ("12 I'm Going Home.m4p", 'Recorded Live'), ('13 Choo Choo Mama.m4p', 'Recorded Live'), ('01 Rock You Mama (Live).m4a', 'Undead (Remastered) [Live]'), ('02 Spoonful (Live).m4a', 'Undead (Remastered) [Live]'), ("03 I May Be Wrong, But I Won't Be Wrong Always (Live).m4a", 'Undead (Remastered) [Live]'), ('04 Summertime _ Shantung Cabbage (Live).m4a', 'Undead (Remastered) [Live]'), ('05 Spider In My Web (Live).m4a', 'Undead (Remastered) [Live]'), ("06 (At the) Woodchopper's Ball [Live].m4a", 'Undead (Remastered) [Live]'), ('07 Standing At the Crossroads (Live).m4a', 'Undead (Remastered) [Live]'), ("08 I Can't Keep from Crying Sometimes _ Extension On One Chord (Live).m4a", 'Undead (Remastered) [Live]'), ("09 I'm Going Home (Live).m4a", 'Undead (Remastered) [Live]'))
            result = mux.get_artistSongs_fromSongs('Ten Years After')
            print("artist songs", result)
            self.assertEqual(expected, result, "song list for Ten Years After wrong" )

        def test_genres(self):
            mux = musicGet_Functions(True)
            genres = mux.get_genres()
            self.assertEqual(Test_Results.genresList, genres, "genre list is wrong")

        '''                
        def test_album_insert_update_album_cover(self):  
            mux = musicGet_Functions(True)
            album = "Test_Crud_Album"
            artist = "Test_Crud_Artist"
            genre = "Test_Crud_Genre"
            tipe = "Test_Crud_Type"
            field = 'cover_name'
            value = 'Test_Crud_cover'
#            mux.set_safe_update_delete()
            mux.add_album(album, artist, genre, tipe)
            mux.update_album(album, field,value)
            field = 'cover_idx'
            idx_value = '99999'
            mux.update_album(album,field,value)
            update_result =  mux.get_album(album)
            print("Update Result.........", update_result)
            expected = ((1065, 'Test_Crud_Artist', 'Test_Crud_Album', 'Test_Crud_Genre', 'Test_Crud_Type', 'Test_Crud_cover', idx_value),)
            self.assertEqual(expected, update_result, "album update failure")
#            clean up
            mux.delete_album_cover(idx_value)

        '''
        def test_add_album(self):
            mux = musicGet_Functions(True)
            album = "Test_Crud_Album"
            artist = "Test_Crud_Artist"
            genre = "Test_Crud_Genre"
            tipe = "Test_Crud_Type"
            mux.add_album(album, artist, genre, tipe)
            result = mux.get_album(album)
            print('252   ', result)
            print('252  ',result[0][2])
            self.assertEqual(album, result[0][2], 'Test add album failed')

        def test_album_update_album_cover(self):  
            mux = musicGet_Functions(True)
            album = "Test_Crud_Album"
            field = 'cover_name'
            value = "Test_Crud_cover.jpg"
            mux.update_album(album, field,value)
            result =  mux.get_album(album)
            print(result)
            expected =  ((1084, 'Test_Crud_Artist', 'Test_Crud_Album', 'Test_Crud_Genre', 'Test_Crud_Type', 'Test_Crud_cover.jpg', None),)
            self.assertEqual(expected, result, "album update failure")
            
        def test_album_update_album_cover_idx(self):  
            mux = musicGet_Functions(True)
            album = "Test_Crud_Album"
            field = 'cover_idx'
            value = "999999"
            mux.update_album(album, field,value)
            result =  mux.get_album(album)
            print(result)
            expected =  ((1084, 'Test_Crud_Artist', 'Test_Crud_Album', 'Test_Crud_Genre', 'Test_Crud_Type', 'Test_Crud_cover.jpg', 999999),)
            self.assertEqual(expected, result, "album update failure")    
            
        def test_delete_album(self):
            mux = musicGet_Functions(True)
            album = "Test_Crud_Album"                      
            mux.delete_album(album)
            result = mux.get_album(album)
            self.assertEqual((),result, "Delete failed")

        def test_get_albumcover(self):
            mux = musicGet_Functions(True)
            albumCover = 'PatMethany_80-81.jpg'
            getCoverResult = mux.get_album_cover(albumCover)
            print("277  ", getCoverResult)
            print("278  ", getCoverResult[0][0])
            self.assertEqual(albumCover, getCoverResult[0][0], "add album cover failed")

        
        def test_add_albumcover(self):
            mux = musicGet_Functions(True)
            albumCover = "Test Cover.jpg"
            mux.add_album_cover(albumCover)
            getCoverResult = mux.get_album_cover(albumCover)
            print('285  ', getCoverResult[0][0])
            self.assertEqual(albumCover, getCoverResult[0][0], "add album cover failed")
            
        def test_delete_albumcover(self):
            albumCover = "Test Cover.jpg"
            mux = musicGet_Functions(True)
            getCoverResult = mux.get_album_cover(albumCover)
            print('292   ',getCoverResult)
            albumCoverId = getCoverResult[0][2]
            print('294  ',albumCoverId)
            mux.delete_album_cover(albumCoverId)
            expected = ()
            deleteResult = mux.get_album_cover(albumCover)
            self.assertEqual(expected, deleteResult, "delete album cover failed")
        
  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
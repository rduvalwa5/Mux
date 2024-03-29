'''
Created on Oct 27, 2017
updated 05-02-2021

@author: rduvalwa2
'''
import unittest
import Test_Results
import platform
from Music_Get_Functions import musicGet_Functions


class TestResults:
    if platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
        cover_count = 787
        songs_count = 11944
        artist_count = 585
        artist_albums_count = 1238

    elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
        cover_count = 782
        songs_count = 11935
        artist_count = 576
        artist_albums_count = 1227


class TestGetFunctions(unittest.TestCase):

        def setUp(self):
            self.mux = musicGet_Functions()
            self.album = "Crud_Album"
            self.artist = "Crud_Artist"
            self.genre = "Crud_Genre"
            self.album_type = "Crud_Type"
            self.field = 'cover_name'
            self.value = 'Crud_cover'
            self.album_index = 000
            self.song_artist = 'TestArtist_X'
            self.song_album = 'TestAlbum_X'
            self.song_song = 'TestSong.mpX'
            self.song_type = 'Download'
            self.song_genre = 'Rock'
            self.song_index = 000

        def tearDown(self):
#            self.mux.dbConnectionClose()
            unittest.TestCase.tearDown(self)

        
        '''
        Test type counts
        '''       

        def test_type_count(self):
            #   mux = musicGet_Functions(True)
            for tipe in Test_Results.typeList:
                print("Type IS...", tipe[0])
                expected = tipe[1]
                result = self.mux.get_type_count(tipe[0])
                print(result)
                self.assertEqual(expected, result) 
                
        '''
        Test genre counts
        '''                      

        def test_genre_count(self):
            #   mux = musicGet_Functions(True)
            gList = Test_Results.genreList
            for gen in gList:
                expected = gen[1]
                result = self.mux.get_genre_count(gen[0])
                print("Genre count result ", result)
                if expected != result:
                    print("expect for genre ", gen[0], expected , " actual is ", result)
                    self.assertEqual(expected, result, "Error " + gen[0])

        '''
        Test get counts
        '''         

        def test_get_all_songs(self):
            #   mux = musicGet_Functions(True)
            expected = Test_Results.songs_count  # 6831
            result = self.mux.get_AllSongs()
            print("All songs count is ", len(result))
            print(result[0])
            self.assertEqual(expected, len(result), "Song count is wrong")
        
        def test_get_count_Artist(self):
            #   mux = musicGet_Functions(True)
            table = 'Music_Test.artist'
            criteria = ""
            expected = Test_Results.artist_count  # 564
            result = self.mux.get_count(table, criteria)
            print("get_count artist", result)
#            self.mux.dbConnectionClose()
            self.assertEqual(expected, result)
              
        def test_get_count_Artist_Albums(self):
            #   mux = musicGet_Functions(True)
            table = 'Music_Test.artist_albums'
            criteria = ""
            expected = Test_Results.artist_albums_count  # 954
            result = self.mux.get_count(table, criteria)
            print("get_count albums", result)
#            self.mux.dbConnectionClose()
#            self.assertEqual(expected, result)
            
        def test_get_count_album2Songs(self):
            #   mux = musicGet_Functions(True)
            table = 'Music_Test.album2songs'
            criteria = ""
            expected = Test_Results.songs_count
            result = self.mux.get_count(table, criteria)
            print("get_count songs", result)
 #           self.mux.dbConnectionClose()
            self.assertEqual(expected, result)    
            
        def test_get_album_cover_count(self): 
            #   mux = musicGet_Functions(True)
            expected = Test_Results.cover_count
            result = self.mux.get_album_cover_count()
            self.assertEqual(expected, result, "cover count wrong")
                    
        def test_get_all_folk_albums(self):
            expected = Test_Results.folk_albums  # 576
            #   mux = musicGet_Functions(True)
            result = self.mux.get_all("`Music_Test`.artist_albums.album", "`Music_Test`.artist_albums", "where `Music_Test`.artist_albums.genre like 'Folk'")
            print(len(result))
            self.assertEqual(expected, len(result))

        def test_get_all_folk_songs(self):
            expected = Test_Results.folk_songs  # 576
            #   mux = musicGet_Functions(True)
            result = self.mux.get_all("`Music_Test`.album2songs.album, `Music_Test`.album2songs.artist", "`Music_Test`.album2songs", "where `Music_Test`.album2songs.genre like 'folk'")
            print(len(result))
            self.assertEqual(expected, len(result))
       
        def test_artist_album_song_exist(self):
            mux = musicGet_Functions()
            expected = False
            result = self.mux.test_artist_album_song_exist('Ten Years After', 'A Space In Time', '04 Over the Hill.m4p')
            print('Expect False ', result)
            self.assertFalse(expected, result)

        def test_artist_album_song_Notexist(self):
            #   mux = musicGet_Functions(True)
            expected = True
            result = self.mux.test_artist_album_song_exist('Ten Years After', 'A Space In Time', '09 Over the Hill.m4p')
            print('Expect True ', result)
            self.assertTrue(expected, result)
    
        def test_get_Song(self):
            thisSong = 'Johnny B. Goode'
            thisAlbum = 'The Best of Chuck Berry'
            #   mux = musicGet_Functions(True)
#            expected =  (946, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
            expected = ('01 Johnny B. Goode.m4a',)
            result = self.mux.get_song(thisSong)
            print("9999999999999999")
            print("song result is ", result)
            self.assertEqual(expected, result)
                       
        def test_get_Album(self):
            #   mux = musicGet_Functions(True)
            album = 'A Space In Time'
            expected = (('Ten Years After', 'A Space In Time', 'Blues Rock', 'Itunes', 'Ten Years After A SpaceIn Time.jpg', 'Download'),)
            result = self.mux.get_album(album)
            print("get album result", result)
            self.assertEqual(expected, result)

        def test_get_all_albums(self):
            #   mux = musicGet_Functions(True)
            result = self.mux.get_all_albums()
            expected = Test_Results.artist_albums_count
            print("all albums ", result)
            print("length all albums", len(result))
            self.assertEqual(expected, len(result), "All album count wrong")

        def test_get_Artist(self):
            #   mux = musicGet_Functions(True)
            expected = Test_Results.get_artist  # (411, 'Ten Years After', 'Blues')
            result = self.mux.get_artist('Ten Years After')
            self.assertEqual(expected, result[0])
        
        def test_get_artistAlbums_from_Albums(self):
            #   mux = musicGet_Functions(True)
            expected = (('Ten Years After', 'Stonedhenge (Re-Presents)', 'Blues Rock', 'Itunes', 'Ten Years After Stonehenge.jpeg', 'Download'), ('Ten Years After', 'Recorded Live', 'Blues Rock', 'Amazon', 'Ten Years After Recorded Live.jpeg', 'Download'), ('Ten Years After', 'Undead (Remastered) [Live]', 'Blues Rock', 'Itunes', 'Ten Years After Undead.jpeg', 'Download'), ('Ten Years After', 'A Space In Time', 'Blues Rock', 'Itunes', 'Ten Years After A SpaceIn Time.jpg', 'Download'))
            result = self.mux.get_artistAlbums_fromAlbums('Ten Years After')
            print("&&&&&&&&&&&&")
            print("artistAlbums 726 ", result)
            self.assertEqual(expected, result)
               
        def test_get_album_songs(self):
            #   mux = musicGet_Functions(True)
            expected = Test_Results.get_artist_albums_songs
            result = self.mux.get_album_songs('A Space In Time')
            print("&&&&&&&&&&&&")
            print("album songs ", result)
            self.assertEqual(expected, result, "song list for A Space In Time wrong")

        def test_get_artist_songs(self):
            #   mux = musicGet_Functions(True)
            expected = (('16 You Never Can Tell.m4a', 'The Anthology'), ('05 Sweet Little Sixteen.m4a', 'The Best of Chuck Berry'), ('07 Roll Over Beethoven.m4a', 'The Best of Chuck Berry'), ('04 Rock And Roll Music.m4a', 'The Best of Chuck Berry'), ("03 Reelin' and Rockin'.m4a", 'The Best of Chuck Berry'), ('10 My Ding A Ling.m4a', 'The Best of Chuck Berry'), ('06 Maybelline.m4a', 'The Best of Chuck Berry'), ('02 School Days.m4a', 'The Best of Chuck Berry'), ('09 No Particular Place To Go.m4a', 'The Best of Chuck Berry'), ('08 Brown Eyed Handsome Man.m4a', 'The Best of Chuck Berry'), ('01 Johnny B. Goode.m4a', 'The Best of Chuck Berry'))
            # (('01 One of These Days.m4p', 'A Space In Time'), ('02 Here They Come.m4p', 'A Space In Time'), ("03 I'd Love to Change the World.m4p", 'A Space In Time'), ('04 Over the Hill.m4p', 'A Space In Time'), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p", 'A Space In Time'), ('06 Once There Was a Time.m4p', 'A Space In Time'), ('07 Let the Sky Fall.m4p', 'A Space In Time'), ('08 Hard Monkeys.m4p', 'A Space In Time'), ("09 I've Been There Too.m4p", 'A Space In Time'), ('10 Uncle Jam.m4p', 'A Space In Time'), ('01 One of These Days Live.m4p', 'Recorded Live'), ('02 You Give Me Loving.m4p', 'Recorded Live'), ('03 Good Morning Little Schoolgirl.m4p', 'Recorded Live'), ('04 Help Me.m4p', 'Recorded Live'), ('05 Classical Thing.m4p', 'Recorded Live'), ('06 Scat Thing.m4p', 'Recorded Live'), ("07 I Can't Keep from Cryin' Sometimes.m4p", 'Recorded Live'), ("09 I Can't Keep from Cryin' (Cont'd).m4p", 'Recorded Live'), ('10 Silly Thing.m4p', 'Recorded Live'), ("11 Slow Blues In 'C'.m4p", 'Recorded Live'), ("12 I'm Going Home.m4p", 'Recorded Live'), ('13 Choo Choo Mama.m4p', 'Recorded Live'), ('01 Rock You Mama (Live).m4a', 'Undead (Remastered) [Live]'), ('02 Spoonful (Live).m4a', 'Undead (Remastered) [Live]'), ("03 I May Be Wrong, But I Won't Be Wrong Always (Live).m4a", 'Undead (Remastered) [Live]'), ('04 Summertime _ Shantung Cabbage (Live).m4a', 'Undead (Remastered) [Live]'), ('05 Spider In My Web (Live).m4a', 'Undead (Remastered) [Live]'), ("06 (At the) Woodchopper's Ball [Live].m4a", 'Undead (Remastered) [Live]'), ('07 Standing At the Crossroads (Live).m4a', 'Undead (Remastered) [Live]'), ("08 I Can't Keep from Crying Sometimes _ Extension On One Chord (Live).m4a", 'Undead (Remastered) [Live]'), ("09 I'm Going Home (Live).m4a", 'Undead (Remastered) [Live]'))
            result = self.mux.get_artistSongs_fromSongs('Chuck Berry')
            
            print("artist Chuck Berry songs", result)
            self.assertEqual(expected, result, "song list for Chuck Berry wrong")

        def test_genres(self):
            #   mux = musicGet_Functions(True)
            genres = self.mux.get_genres()
            print("Get Genres ", genres)
            self.assertEqual(Test_Results.genresList, genres, "genre list is wrong")

        '''
        DATABASE CRUD TEST
        Crud test album
        '''

#        def test_CRUD_album_insert_album(self): 
#            self.mux.add_album(self.album, self.artist, self.genre, self.album_type)
#            add_result = self.mux.get_album(self.album)
#            print("Add Result.........", add_result[0])
#            expected = (('Crud_Artist', 'Crud_Album', 'Crud_Genre', 'Crud_Type', None, None),)
#            print("add resutl is ", expected)
#            self.assertEqual(expected, add_result, "album crud test add failure") 
        
        def test_Add_One_Song(self):
            #   mux = musicGet_Functions(True)
            result = self.mux.add_one_song(self.song_artist, self.song_album, self.song_song, self.song_genre, self.song_type)
            print("7777777777777777")
            print("add song result is ", result) 
            self.assertEqual(result, None)

        def test_Update_Song_Artist(self):
            self.song_artist = self.song_artist + '_upDate'
            result = self.mux.update_song_artist(self.song_artist, self.song_song, self.song_album)
            print("song artist update is ", self.song_song)
            expected = self.song_song + ' updated successfully' 
            print("artist update song ", result)
            self.assertEqual(expected, result, " Song artist update failed")

        def test_Update_Song_Genre(self):
            self.song_genre = self.song_genre + '_upDate'
            result = self.mux.update_song_genre(self.song_genre, self.song_song, self.song_album)
            print("song genre update is ", self.song_genre)
            expected = self.song_song + ' updated successfully' 
            print("genre update song ", result)
            self.assertEqual(expected, result, " Song genre update failed")
        
        def test_Update_Song_Type(self):
            self.song_type = self.song_type + '_upDate'
            result = self.mux.update_song_type(self.song_type, self.song_song, self.song_album)
            print("song type update is ", self.song_type)
            expected = self.song_song + ' updated successfully' 
            print("type update song ", result)
            self.assertEqual(expected, result, " Song type update failed")
        
        def test_Update_Song_Name(self):
            pass

        '''
        def test_get_song(self):
            print(self.song_song)
            result = self.mux.get_song(self.song_song)
            print("get song is *******", result)
        
        def test_delete_song(self):
            getResult = self.mux.get_song(self.song_song)
            print("getResult  ", getResult)
            deleteIndex = getResult[0][0]
            print("deleted song index is ", str(deleteIndex))
            expected = 'delete successfull'
            print("Delete test index is ",deleteIndex )
            result = self.mux.delete_song(deleteIndex)
            print("delete song result ",result)
            self.assertEqual(expected,result)   
        '''

        def test_delete_one_song(self):
            expected = 'TestSong.mpX deleted'
            result = self.mux.delete_one_song(self.song_album, self.song_song)
            print("delete song result ", result)
            self.assertEqual(expected, result)    
     
        def test_get_albumcover(self):
            #   mux = musicGet_Functions(True)
            albumCover = 'PatMethany_80-81.jpg'
            getCoverResult = self.mux.get_album_cover(albumCover)
            print("277  ", getCoverResult)
            print("278  ", getCoverResult[0][0])
            self.assertEqual(albumCover, getCoverResult[0][1], "add album cover failed")
        
        def test_add_albumcover(self):
            #   mux = musicGet_Functions(True)
            albumCover = "Test Cover.jpg"
            album = "Test album"
            self.mux.add_album_cover(albumCover, album)
            getCoverResult = self.mux.get_album_cover(albumCover)
            print('285  ', getCoverResult[0][0])
            self.assertEqual(albumCover, getCoverResult[0][1], "add album cover failed")
            
        def test_delete_albumcover(self):
            album_cover = "Test Cover.jpg"
            print('delete cover of album ', album_cover)
            self.mux.delete_album_cover(album_cover)
            expected = ()
            deleteResult = self.mux.get_album_cover(album_cover)
            self.assertEqual(expected, deleteResult, "delete album cover failed")

  
if __name__ == "__main__":
    unittest.main()

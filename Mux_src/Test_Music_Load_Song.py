'''
'''
import unittest 

#import os, platform
#import self.conn.Error
#import MySQLdb   as connDb

#from Musicdb_info import login_info_root
#from Musicdb_info import login_info_osx 
#import mysql.connector
import os
import Music_Get_Functions
from  Music_Load import musicLoad_Functions, song_Add_Update_Delete, album_Add_Update_Delete, artist_Add_Update_Delete

class Test_MusicLoadSongTable(unittest.TestCase):
        def setUp(self):
#   self.albumAddUpDel.add_album(self.album,self.addArtist,self.addType,self.addGenre)

            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
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
            self.serverUpdate = 'Up_Song_Server'
            self.pathUpdate = '/Test/Up_Music'
            
        def tearDown(self):
            self.getInfo.dbConnectionClose()
            self.songAUD.dbConnectionClose()
         
                       
        """
            Test Album_Songs Table Functions
        """ 
        
        def test_1_Add_Song(self):
            """
             insert into `Music`.album2songs (album2songs.index, album, artist,genre,path,server,song,type) 
             values (6599,'SongAlbum','SongArts','SongGenre','/path/path/','song_server','Song_Song.mp3','test_type');
             [(6599, 'song_server', '/Test/Music', 'Song_Artist', 'Test_SongAlbum', 'Song_Song.mp3', 'Song_genre', 'Song_Type')]
            """
            self.songAUD.add_song(self.addAlbum,self.addArtist,self.addGenre,self.song,self.addType,self.addPath,self.addServer)
            addSongResult = self.getInfo.get_song_by_song(self.song)
            print(addSongResult)
            self.assertEqual(self.addServer, addSongResult[0][1], "Server failed")
            self.assertEqual(self.addPath, addSongResult[0][2], "path failed")
            self.assertEqual(self.addArtist, addSongResult[0][3], "artist failed")
            self.assertEqual(self.addAlbum, addSongResult[0][4], "album failed")
            self.assertEqual(self.song, addSongResult[0][5], "song failed")
            self.assertEqual(self.addGenre, addSongResult[0][6], "genre failed")           
            self.assertEqual(self.addType, addSongResult[0][7], "album failed")
 
            
        def test_2_update_song(self):
            """
            "UPDATE `Music`.album2songs SET artist = '" + artist + "' WHERE song = '" + song  + "';"
             [(6599, 'song_server', '/Test/Music', 'Song_Artist', 'Test_SongAlbum', 'Song_Song.mp3', 'Song_genre', 'Song_Type')]
            """
            self.songAUD.update_song_artist(self.artistUpdate, self.song)
            self.songAUD.update_song_album(self.albumUpdate, self.song)
            self.songAUD.update_song_genre(self.genreUpdate, self.song)
            self.songAUD.update_song_path(self.pathUpdate, self.song)
            self.songAUD.update_song_server(self.serverUpdate, self.song)
            self.songAUD.update_song_type(self.typeUpdate, self.song)
            Result = self.getInfo.get_song_by_song(self.song)
            
            print("song update ", Result)
            self.assertEqual(self.serverUpdate, Result[0][1], "Server failed")
            self.assertEqual(self.pathUpdate,Result[0][2], "path failed")
            self.assertEqual(self.artistUpdate, Result[0][3], "artist failed")
            self.assertEqual(self.albumUpdate, Result[0][4], "album failed")
            self.assertEqual(self.song,Result[0][5], "song failed")
            self.assertEqual(self.genreUpdate,Result[0][6], "genre failed")           
            self.assertEqual(self.typeUpdate,Result[0][7], "album failed")
 
        def test_3_delete_song(self):
            self.songAUD.delete_song(self.song)
            deleteSongResult = self.getInfo.get_song_by_song(self.song)
            print("song delete ", deleteSongResult)
            expected = []
            self.assertListEqual(expected, deleteSongResult, "list is not empty")  
                   
if __name__ == "__main__":
    unittest.main()
'''
Created on Nov 22, 2016

@author: rduvalwa2
'''
import unittest
from MusicFile import musicFile
from Music_Get_Functions import musicGet_Functions


class Test(unittest.TestCase):

        def test_get_count_albums(self):
            '''
            get_record_count
            '''
            table = "`Music`.artist_albums"
            expected = 909
            mux = musicFile()
            result = mux.get_record_count(table)
            self.assertEqual(expected,result[0])
            
        def test_get_count_songs(self):
            '''
            get_record_count
            '''
            table = "`Music`.album2songs"
            expected = 6625
            mux = musicFile()
            result = mux.get_record_count(table)
            self.assertEqual(expected,result[0])
            
        def test_get_count_artist(self):
            '''
            get_record_count
            '''
            table = "`Music`.artist"
            expected = 537
            mux = musicFile()
            result = mux.get_record_count(table)
            self.assertEqual(expected,result[0])
            
        def test_get_count_Viny_Albums(self):
            '''
            get_select_Album
            '''
            display =  "count(*)"
            constraints = "where type like 'Vinyl'"
            expected = 183
            mux = musicFile()
            result = mux.get_select_Album(display,constraints)
            self.assertEqual(expected,result[0])
 
        '''
        select artist FROM  `Music`.artist where genre like 'TexMex';
        '''
        def test_get_song(self):
            song = 'Johnny B. Goode'
            genre = 'Blues'
            muxGet = musicGet_Functions()
            result = muxGet.get_song(song)
            print(result)
 #           self.assertEqual(artist, result[0][1], "artist return wrong")
 #           self.assertEqual(genre, result[0][2], "genre wrong")
                
            
        def test_get_TexMex_Artist(self):
            '''
            get_select_Artist
            '''
            resultArtist = []
            fields =  "Music.artist.artist"
            constraints = " genre like 'TexMex'"
            mux = musicFile()
            result = mux.get_select_Artist(fields, constraints)
#            print(result)
            for artist in result:
                resultArtist.append(artist[0])
#            print(resultArtist)
            self.assertIn('Asleep At the Wheel', resultArtist, 'artist not present')
            self.assertIn('Eldorado', resultArtist, 'artist not present')
            self.assertIn( 'Freddy Fender', resultArtist, 'artist not present')
            self.assertIn('Los Lobos', resultArtist, 'artist not present')
            self.assertIn('Texas Tornados', resultArtist, 'artist not present')
            self.assertIn( 'The Mavericks', resultArtist, 'artist not present')
            self.assertIn('The Sir Douglas Quintet', resultArtist, 'artist not present')
            
 
        def test_get_album(self):
            artistName = 'Ten Years After'
            albumGenre = 'Rock'
            albumType = 'Download' 
            muxGet = musicGet_Functions()
            album = 'A space In Time'
            result = muxGet.get_album(album)
            self.assertEqual(artistName, result[0][1], 'artist name wrong')
            self.assertEqual(albumGenre, result[0][3], 'genre wrong')
            self.assertEqual(albumType, result[0][4], 'type wrong')            
#            muxGet.dbConnectionClose()
 
        def test_get_artist(self):
            '''
            [(411, 'Ten Years After', 'Blues')]
            '''
            artist = 'Ten Years After'
            genre = 'Blues'
            muxGet = musicGet_Functions()
            result = muxGet.get_artist(artist)
            print(result)
            self.assertEqual(artist, result[0][1], "artist return wrong")
            self.assertEqual(genre, result[0][2], "genre wrong")

        def test_get_song_by_id(self):
            id = 19
            item = 'song'
            muxGet = musicGet_Functions()
            result = muxGet.get_by_id(id, item)
#            print("song ", result)
            self.assertEqual(id, result[0][0], "song id not found")
            
        def test_get_album_by_id(self):
            id = 5
            item = 'album'
            muxGet = musicGet_Functions()
            result = muxGet.get_by_id(id, item)
#            print("album ",result)
            self.assertEqual(id, result[0][0], "album id not found")

        def test_get_artis_by_id(self):
            id = 4
            item = 'artist'
            muxGet = musicGet_Functions()
            result = muxGet.get_by_id(id, item)
#            print("artist ",result)
            self.assertEqual(id, result[0][0], "artist id not found")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
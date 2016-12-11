'''
Created on Nov 22, 2016

@author: rduvalwa2
'''
import unittest
from MusicFile import musicFile


class Test(unittest.TestCase):

        def test_get_count_albums(self):
            '''
            get_record_count
            '''
            table = "`Music`.artist_albums"
            expected = 901
            mux = musicFile()
            result = mux.get_record_count(table)
            self.assertEqual(expected,result[0])
            
        def test_get_count_songs(self):
            '''
            get_record_count
            '''
            table = "`Music`.album2songs"
            expected = 6593
            mux = musicFile()
            result = mux.get_record_count(table)
            self.assertEqual(expected,result[0])
            
        def test_get_count_artist(self):
            '''
            get_record_count
            '''
            table = "`Music`.artist"
            expected = 536
            mux = musicFile()
            result = mux.get_record_count(table)
            self.assertEqual(expected,result[0])
            
        def test_get_count_Viny_Albums(self):
            '''
            get_select_Album
            '''
            display =  "count(*)"
            constraints = "where type like 'Vinyl'"
            expected = 184
            mux = musicFile()
            result = mux.get_select_Album(display,constraints)
            self.assertEqual(expected,result[0])
 
        '''
        select artist FROM  `Music`.artist where genre like 'TexMex';
        '''
        def test_get_TexMex_Artist_(self):
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
            print(resultArtist)
            self.assertIn('Asleep At the Wheel', resultArtist, 'artist not present')
            self.assertIn('Eldorado', resultArtist, 'artist not present')
            self.assertIn( 'Freddy Fender', resultArtist, 'artist not present')
            self.assertIn('Los Lobos', resultArtist, 'artist not present')
            self.assertIn('Texas Tornados', resultArtist, 'artist not present')
            self.assertIn( 'The Mavericks', resultArtist, 'artist not present')
            self.assertIn('The Sir Douglas Quintet', resultArtist, 'artist not present')
 
 
 
        '''
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
    '''
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
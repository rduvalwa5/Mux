'''
Created on Nov 22, 2016

@author: rduvalwa2
'''
import unittest
from MusicFile import musicFile


class Test(unittest.TestCase):

        def test_get_select_ArtistAlbums(self):
            fields = "count(*)"
            constraints = " "
            expected = 751
            mux = musicFile()
            result = mux.get_select_Album(fields, constraints)
            self.assertEqual(expected,result[0])
 

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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
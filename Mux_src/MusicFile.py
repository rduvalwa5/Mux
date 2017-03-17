'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.

@author: rduvalwa2
'''

import os, sys
import mysql.connector
from  Musicdb_info import login_info_rd
from Musicdb_info import login_info_root
from Musicdb_info import login_info_osx 
from mysql.connector.errors import Error


class connection_db:
    def connect_music(self):
        pass


class musicFile:   
    
    def __init__(self):
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'       
    
    def get_record_count(self,table):
        statement = "select count(*) from " + table   + ";"
        if os.uname().nodename == 'C1246895-osx.home':
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            conn = mysql.connector.Connect(**login_info_root)
        
        cursor = conn.cursor()
        cursor.execute(statement)
        count = cursor.fetchone()
        conn.close()   
        return count        
    
    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
        if os.uname().nodename == 'C1246895-osx.home':
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        conn.close()   
        return maxIndex
    

    def get_select_Album(self, fields, constraints):
        if os.uname().nodename == 'C1246895-osx.home':
#            print(os.uname().nodename)
            conn = mysql.connector.Connect(**login_info_osx)
        else:
#            print(os.uname().nodename)
            conn = mysql.connector.Connect(**login_info_root)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.artist_albums " + constraints + ";" #where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
        dbCursor.close()
        conn.close()
        return row

    def get_select_Artist(self, fields, constraints):
        outPut = []
        if os.uname().nodename == 'C1246895-osx.home':
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            conn = mysql.connector.Connect(**login_info_rd)
        dbCursor = conn.cursor()
        statement = "select "+ fields + " from Music.artist " + constraints + ";" #where Albums.index = 3;"
        print(statement)
        dbCursor.execute(statement)
        rows = dbCursor.fetchall()
#        print(row)   
        dbCursor.close()     
        conn.close() 
        return rows      
    
    def get_select_ArtistAlbums(self, fields, constraints):
        if os.uname().nodename == 'C1246895-osx.home':
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            conn = mysql.connector.Connect(**login_info_root)
        dbCursor = conn.cursor()
        statement = "select " + fields + " from Music.artist_albums" + constraints + ";"
        print(statement)
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
        dbCursor.close()
        conn.close()
        return row        
    
    def select_song_by_criteria(self,statement):
        '''
        Select a song or songs by criteria.
        '''
        rows = []
        if os.uname().nodename == 'C1246895-osx.home':
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        self.statement = statement
        cursor.execute(statement)
        row = cursor.fetchone()
        while row is not None:
                rows.append(row)
                row = cursor.fetchone()
        cursor.close()
        conn.close()
        return rows

    def get_music_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index,directory))
                index = index + 1
        return artist
    
    def get_albums(self):
        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        index = 0
        artists = self.get_music_artist()
        for a in artists:
            artist = a[1]
            if os.path.isdir(base + "/" + artist):
                artist_albums = os.listdir(base + "/" + artist)
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((index,artist,album))
                        index = index + 1
        return albums

    def get_all_songs(self):
        index = 0
        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        artist = self.get_music_artist()
        for a in artist:
            if os.path.isdir(base + "/" + a[1]):
                artist_albums = os.listdir(base + "/" + a[1])
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((a,album))
                        album_songs = os.listdir(base + "/" + a[1] + "/" + album)
                        for song in album_songs:
                                songs.append((index,a[1],album,song))
                                index = index + 1
        return songs
    
    def get_all_songs_type_genre(self):
        if os.uname().nodename == 'C1246895-osx.home':
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        sync_statement = "UPDATE `Music`.album2songs t1 INNER JOIN `Music`.artist_albums t2 ON t1.album = t2.album SET t1.genre = t2.genre, t1.type = t2.type;"
        cursor.execute(sync_statement)
        commit = "commit;"
        cursor.execute(commit)    
    
    def get_songs(self,artist,album='all'):
        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        newIndex = 0
        if os.path.isdir(base + "/" + artist):
                artist_albums = os.listdir(base + "/" + artist)
                print("artist_albums: ", artist_albums)
                if album == 'all':
                    for al in artist_albums:
                        if al != '.DS_Store':
                            albums.append((artist,al))
                            album_songs = os.listdir(base + "/" + artist + "/" + al)
                            for song in album_songs:
                                    songs.append((newIndex,artist,al,song))
                elif  album != 'all':
                    for al in artist_albums:
                        if al == album:
                            if al != '.DS_Store':
                                albums.append((artist,al))
                                album_songs = os.listdir(base + "/" + artist + "/" + al)
                                for song in album_songs:
                                    songs.append((newIndex,artist,al,song))
                        
            
        return songs


    def initial_insert_into_album2songs(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        trunkate = "truncate  music.album2songs;"
        cursor.execute(trunkate)
        allSongs = self.get_all_songs()
        for song in allSongs:
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(song[0]) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + song[1] + "\",\""  + song[2] + "\",\""  + song[3] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
                cursor.execute( insertStatement)
        countStatement = "SELECT count(*) FROM music.album2songs;"        
        cursor.execute(countStatement)
        count = cursor.fetchone()
        print(count)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()

    def add_songs(self,artist,album='all'):
        '''
        This code adds song
        '''
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        maxIndex =  self.get_max_index("album2songs")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        if album == 'all': 
            songs = self.get_songs(artist)
        else:
            songs = self.get_songs(artist,album)
        print(songs)
        for song in songs:
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + song[1] + "\",\""  + song[2] + "\",\""  + song[3] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
                print(insertStatement)
                cursor.execute( insertStatement)
                newIndex = newIndex + 1
        countStatement = "SELECT count(*) FROM music.album2songs;"        
        cursor.execute(countStatement)
        count = cursor.fetchone()
        print(count)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()

    
    def delete_songs(self,artist,albumin='all',songin="all"):
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()   
        delete_songs = self.get_songs(artist,albumin)
        print("delete songs: ", delete_songs)  
        index = 0
        if albumin == 'all':
            if songin == 'all':   
                for song in delete_songs:
                        selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                        print(selectStatement)
                        cursor.execute(selectStatement)
                        row = cursor.fetchone()
                        index = row[0]  
                        print("delete index: ", index)         
                        deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                        print(deleteStatement)
                        cursor.execute(deleteStatement)
            else:
                for song in delete_songs:  
                    if song[0] == 'songin':
                        selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                        print(selectStatement)
                        cursor.execute(selectStatement)
                        row = cursor.fetchone()
                        index = row[0]           
                        deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                        print(deleteStatement)
                        cursor.execute(deleteStatement)        
        else:
            if albumin != 'all': 
                if songin == 'all':  
                    for song in delete_songs:
                        if albumin == song[2]: 
                            selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                            print(selectStatement)
                            cursor.execute(selectStatement)
                            row = cursor.fetchone()
                            index = row[0]                      
                            deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                            print(deleteStatement)
                            cursor.execute(deleteStatement)
            elif songin != 'all':
                    for song in delete_songs:
                        if albumin == song[2]:                                
                            if song[0] == 'song': 
                                selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                                print(selectStatement)
                                cursor.execute(selectStatement)
                                row = cursor.fetchone()
                                index = row[0]           
                                deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                                print(deleteStatement)
                                cursor.execute(deleteStatement)        
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()


    def initial_insert_into_artist_albums(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        trunkate = "truncate  music.artist_albums;"
        cursor.execute(trunkate)
        allAbums = self.get_albums()
        for album in allAbums:
                insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.genre,artist_albums.type)  values(" + str(album[0]) + ",\""  + album[1] + "\",\""  + album[2] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
                cursor.execute( insertStatement)
        countStatement = "SELECT count(*) FROM music.artist_albums;"        
        cursor.execute(countStatement)
        count = cursor.fetchone()
        print(count[0])
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()


    def initial_insert_into_artist(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        trunkate = "truncate  music.artist;"
        cursor.execute(trunkate)
        allArtist = self.get_music_artist()
        for artist in allArtist:
                insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(artist[0]) + ",\"" + artist[1] + "\",\""  + "rock" + "\")"
                cursor.execute( insertStatement)
        countStatement = "SELECT count(*) FROM music.artist;"        
        cursor.execute(countStatement)
        count = cursor.fetchone()
        print(count[0])
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()

 
    def add_album(self,album,artist,tipe):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        maxIndex =  self.get_max_index("artist_albums")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type)  values(" + str(newIndex) + ",\""  + artist + "\",\""  + album + "\",\""  + tipe + "\")"
        print(insertStatement)
        cursor.execute(insertStatement)
        count = cursor.fetchone()
#        print(count[0])
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()

        
#  Not done
    def delete_album(self,album):
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        index = row[0]
        print(index)
        deleteStatement = "Delete from `Music`.artist_albums where `Music`.artist_albums.index = " + str(index) + ";"       
        print(deleteStatement)
        cursor.execute(deleteStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()
        
        
    def add_artist(self,artist,genre):
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        maxIndex =  self.get_max_index("artist")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex) 
        insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(newIndex) + ",\""  + artist  + "\",\""  + genre + "\")"
        print(insertStatement)
        cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()

    def delete_artist(self,artist):
        if os.uname().nodename == 'C1246895-osx.home':
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_osx)
        else:
            self.server = os.uname().nodename
            conn = mysql.connector.Connect(**login_info_root)
        cursor = conn.cursor()
        selectStatement = "select artist.index from Music.artist where artist.artist like " + "'" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        index = row[0]
        print(index)
        deleteStatement = "Delete from `Music`.artist where `Music`.artist.index = " + str(index) + ";"       
        print(deleteStatement)
        cursor.execute(deleteStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        conn.close()

    def dbConnectionClose(self):
        self.conn.close()    
    
if __name__  == '__main__':
#    mux = musicFile()

#    albumCount = mux.get_record_count("`Music`.artist_albums")
#    songCount = mux.get_record_count("`Music`.album2songs")
#    artistCount = mux.get_record_count("`Music`.artist")
#    print("Artist: ", artistCount ," Songs: ", songCount, " Albums: ", albumCount )

#    mux.add_songs('ZZ_ZTest', 'Test_Album1')
#    mux.delete_songs('ZZ_ZTest', 'Test_Album1')
    
#    mux.add_songs('ZZ_ZTest', 'Test_Album2')
#    mux.delete_songs('ZZ_ZTest', 'Test_Album2')
    
#    mux.add_songs('ZZ_ZTest','all')
#    mux.delete_songs('ZZ_ZTest','all')
    
    
#    songs = mux.get_songs(artist, album):
        


#    fields = "Music.artist.index, Music.artist.artist "
#    criteria = " Music.artist.artist like \'Bob Dylan\'"   
#    result = mux.get_select_Artist(fields,criteria)
#    print(result)

#    for artist in artistList:
#        print(artist)

#    allAlbums = mux.get_albums()
#    for album in allAlbums:
#        print(album)

# ************
#    mux.initial_insert_into_album2songs()
#    mux.get_all_songs_type_genre()
# ************
#    mux.initial_insert_into_artist_albums()
# ************
#    mux.initial_insert_into_artist()
# ************

    '''
    Test add artist, select artist, delete artist
    '''
#    arts = "Joe Blow"
#    mux.add_artist(arts,"Rock")  
#    fields = " * "
#    criteria = "Music.artist.artist like \'Joe Blow\'"
#    print(mux.get_select_Artist(fields,criteria))
#    mux.delete_artist(arts)   
#    print(mux.get_select_Artist(fields,criteria))
    
    '''
    Test add album, select album, delete album
    '''  
#    arts = "Joe Blow"
#    album = "The Best of Joe Blow"
#    tipe = "Country"
#    mux.add_album(album,arts,tipe)
#    fields = " * "
#    criteria = " where Music.artist_albums.album like '" + album + "'"
#    result = mux.get_select_ArtistAlbums(fields,criteria)
#    print(result)
#    mux.delete_album(album)   
#    print(mux.get_select_ArtistAlbums(fields,criteria))
    
    

#    albumCount = mux.get_record_count("`Music`.artist_albums")
#    songCount = mux.get_record_count("`Music`.album2songs")
#    artistCount = mux.get_record_count("`Music`.artist")
#    print("Artist: ", artistCount ," Songs: ", songCount, " Albums: ", albumCount )
    
    
#    albumCount = mux.get_record_count("`Music`.artist_albums")
#    songCount = mux.get_record_count("`Music`.album2songs")
#    artistCount = mux.get_record_count("`Music`.artist")
#    print("Artist: ", artistCount ," Songs: ", songCount, " Albums: ", albumCount )
    

    import unittest
    class TestConnector(unittest.TestCase):

        def test_get_select_ArtistAlbums(self):
            fields = "count(*)"
            constraints = " "
            expected = 909
            mux = musicFile()
            result = mux.get_select_Album(fields, constraints)
            self.assertEqual(expected,result[0])
 

        def test_get_select_Album(self):
            fields = "count(*)"
            constraints = " "
            expected = 909
            mux = musicFile()
            result = mux.get_select_ArtistAlbums(fields, constraints)
            self.assertEqual(expected,result[0])

        def test_get_select_Artist(self):
            fields = "count(*)"
            constraints = " "
            expected = 537
            mux = musicFile()
            result = mux.get_select_Artist(fields, constraints)
            self.assertEqual(expected,result[0][0])

        def testGetMaxArtist(self):
            mux = musicFile()
            table = 'Artist'
            expected = 537
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
            
        def testGetMaxAlbums(self):
            mux = musicFile()
            table = 'artist_albums'
            expected = 909
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
 
        def testGetMaxSongs(self):
            mux = musicFile()
            table = 'album2songs'
            expected = 6624
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
 
           
        def testGetMaxAlbumSongs(self):
            mux = musicFile()
            table = 'album2songs'
            expected = 6624
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0]) 
       
        def test_get_dirs_artist(self):
            mux = musicFile()
            base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            musicArtist = mux.get_music_artist()
            self.assertIn( (409, 'The Charlie Daniels Band'), musicArtist, "Charlie Daniels Band not there")

        def test_albumList(self):
            mux = musicFile()
            alms = mux.get_albums()
            self.assertIn((802, "Tim O'Brien", 'Cornbread Nation'), alms, "Cornbread Nation not present")

        def test_songList(self):
            mux = musicFile()
            mysongs = mux.get_all_songs()
            self.assertIn((0, '18 South', 'Soulful Southern Roots Music', '01 Late Night Ramble.mp3'), mysongs, "'01 Late Night Ramble.mp3' song is missing")       
    unittest.main()    

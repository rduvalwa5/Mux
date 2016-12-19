import os
import mysql.connector, Music_Get_Functions
#from  Musicdb_info import login_info_rd
from Musicdb_info import login_info_root
from Musicdb_info import login_info_osx 
#from mysql.connector.errors import Error


class musicLoad_Functions:   
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'

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

    def get_music_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index,directory))
                index = index + 1
        return artist

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


    def initial_insert_into_artist(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
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

    def initial_insert_into_artistAlbums(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
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

    def initial_insert_into_album2songs(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
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

class musicSong_Add_Delete:       
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'      
        
    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
        cursor = self.conn.cursor()
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
    
    def get_songs(self,artist,album='all'):
        base =   self.base
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

    def add_songs(self,artist,album='all'):
        '''
        This code adds song
        '''
        cursor = self.conn.cursor()
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
    
    def delete_songs(self,artist,albumin='all',songin="all"):
        cursor = self.conn.cursor()   
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

    def dbConnectionClose(self):
        self.conn.close()

class musicAlbum_Add_Delete:       
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'      

    def dbConnectionClose(self):
        self.conn.close()

    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
        cursor = self.conn.cursor()
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
    
    def add_album(self,album,artist,tipe,gen):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        maxIndex =  self.get_max_index("artist_albums")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type,artist_albums.genre)  values(" + str(newIndex) + ",\""  + artist + "\",\""  + album + "\",\""  + tipe +  "\",\"" + gen +"\" )"
        print(insertStatement)
        cursor.execute(insertStatement)
        count = cursor.fetchone()
#        print(count[0])
        commit = "commit;"
        cursor.execute(commit)
        print("done")
#        cursor.close()
        self.conn.close()
        
#  Not done
    def delete_album(self,album):
#        if os.uname().nodename == 'C1246895-osx.home':
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_osx)
#        else:
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_root)
        cursor = self.conn.cursor()
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

        
class musicArtist_Add_Delete:       
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'     

    def dbConnectionClose(self):
        self.conn.close()

    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"

        cursor = self.conn.cursor()
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
                    
    def add_artist(self,artist,genre):
        cursor = self.conn.cursor()
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

    def delete_artist(self,artist):
        cursor = self.conn.cursor()
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
            
if __name__  == '__main__':
    import unittest
    class Test_MusicLoad(unittest.TestCase):
        def setUp(self):
            print("Test setup")
            self.getInfo = Music_Get_Functions.musicGet_Functions()
            self.addArtistInfo = musicArtist_Add_Delete()
            self.addAlbum = musicAlbum_Add_Delete()
            self.arts = 'ZZ_ZTestX'
            self.genre = 'Test GenX'
            self.album = 'Test_Album1X'
            self.tipe = 'TestTape'
            self.albums = ['Test_AlbumA','Test_AlbumB','Test_AlbumC']
            
        def tearDown(self):
            self.addArtistInfo.dbConnectionClose()
            self.addAlbum.dbConnectionClose()
            self.getInfo.close_connection()
            
        def test_Add_Artist(self): 
            self.addArtistInfo.add_artist(self.arts ,self.genre)
            result = self.getInfo.get_artist_from_artistTable(self.arts)
            self.assertEqual(self.arts,result[0][1],"artist name add failed")
            self.assertEqual(self.genre,result[0][2],"artist genre add failed")           

        def test_Delete_Artist(self): 
            self.addArtistInfo.delete_artist(self.arts)
            result = self.getInfo.get_artist_from_artistTable(self.arts)
            expected = []
            self.assertListEqual(expected, result, "list is not empty")       
            
    unittest.main()            
          

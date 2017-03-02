'''
Created on Feb 16, 2017
improve for Python 3.6
@author: rduvalwa2
'''

import os
import mysql.connector
from Musicdb_info import login_info_root
from Musicdb_info import login_info_osx 


class musicGet_Functions:   
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'  
    '''
    Get max index values from tables
    '''
    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
        try:
            cursor = self.conn.cursor()
            cursor.execute( max_index_statement)
            maxIndex = cursor.fetchone()
            cursor.close()
            self.dbConnectionClose()
            return maxIndex
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
                
    def get_count(self,table = 'music.album2songs', criteria = " "):
        statement = "select count(*) from " + table + " "  + criteria + ";"
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            count = cursor.fetchone()  
            theCount = count[0]
            cursor.close()
            self.dbConnectionClose()
            return theCount       
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
            
    def get_all(self,fields = "*",table = 'music.album2songs', criteria = " "):
        statement = "select " + fields + " from " + table + " "  + criteria + ";"
        print("get all ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result                   
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)

               
    def dbConnectionClose(self):
        self.conn.close()         
    
    '''
        Song  ********************
    '''

    def get_song(self,song):
        '''
        '''
        fields = '*'
        statement = "Select " + fields + " from music.album2songs where song like '%" + song + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result            
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)

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

    def test_artist_album_song_exist(self,artist,album,song):
        cursor = self.conn.cursor()
        statement = "select * from Music.album2songs where Music.album2songs.song like '" + song + "' and Music.album2songs.artist like '" + artist + "' and Music.album2songs.album like '" + album + "';"        
        try:
            cursor.execute(statement)
            result = cursor.fetchone()
            print(result)
            cursor.close()
            self.dbConnectionClose()
            print('Result is ',result)
            if result == None:
                return  True
            else:
                return False
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)        
    
    def add_one_song(self,artist,album,song,genre='Rock',path ='/Users/rduvalwa2/Music/iTunes/iTunes Music/Music',server='OSXAir.home',tipe='Download'):  
        cursor = self.conn.cursor()
        maxStatement = 'select max(`Music`.album2songs.index) FROM `Music`.album2songs;'
        try:
            cursor.execute(maxStatement)
            maxIndex = cursor.fetchone()[0]
            print("max is " ,maxIndex)
            newIndex = maxIndex + 1
            print("new is ", newIndex)
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
                    
        statement = "insert into `Music`.album2songs (album,artist,genre,`Music`.album2songs.index,path,server,song,type) values('" + album + "','" + artist + "','" + genre + "','" + str(newIndex) + "','" + path + "','" + server + "','" + song + "','" + tipe + "');"
        try:
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            cursor.close()
            self.dbConnectionClose()
            return "Success"
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)

    def delete_one_song(self,artist,album,song):
            cursor = self.conn.cursor()
            statement = "delete from `Music`.album2songs where song like '" + song + "' and album like '" + album + "' and artist like '" + artist + "';"
            print("delete ", statement)
            try:
                cursor.execute(statement)
                commit = "commit;"
                cursor.execute(commit)
                cursor.close()
                self.dbConnectionClose()
                return song + " deleted"  
            except mysql.connector.Error as err:
                print("Exception is ", err)
                return str(err)      

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
        result = "added " + songs 
        cursor.close()
        self.dbConnectionClose()
        return result 
    
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
        result = "deleted songs"
        cursor.close()
        self.dbConnectionClose()
        return result  

    '''
        Artist  ********************
    '''

    def get_artist(self,artist):
#       select music.artist.index, artist, genre from music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist where artist = '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result  
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)               
       
    def add_artist(self,artist,genre):
        cursor = self.conn.cursor()
        maxIndex =  self.get_max_index("artist")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex) 
        insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(newIndex) + ",\""  + artist  + "\",\""  + genre + "\")"
        print(insertStatement)
        try:
            cursor.execute(insertStatement)
            commit = "commit;"
            cursor.execute(commit)
            cursor.close()
            print("done")
            self.dbConnectionClose()
            return "Added " + artist
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
        
    def delete_artist(self,artist):
        cursor = self.conn.cursor()
        selectStatement = "select artist.index from Music.artist where artist.artist like " + "'" + artist + "';"
        print(selectStatement)
        try:
            cursor.execute(selectStatement)
            row = cursor.fetchone()
            index = row[0]
            print(index)
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
        
        deleteStatement = "Delete from `Music`.artist where `Music`.artist.index = " + str(index) + ";"       
        print(deleteStatement)
        try:
            cursor.execute(deleteStatement)
            commit = "commit;"
            cursor.execute(commit)
            cursor.close()
            self.dbConnectionClose()
            return "deleted " + artist
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err) 

    def get_artistAlbums_fromAlbums(self,artist):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where artist like '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
#            print(result)
            cursor.close()
            self.dbConnectionClose()
            return result   
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
        
    '''
        Album  ********************
    '''
            
    def get_album(self,album):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where album = '" + album + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result           
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err) 

    def add_album(self,album,artist,tipe):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        maxIndex =  self.get_max_index("artist_albums")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type)  values(" + str(newIndex) + ",\""  + artist + "\",\""  + album + "\",\""  + tipe + "\")"
        print(insertStatement)
        try:
            cursor.execute(insertStatement)
            #        count = cursor.fetchone()
            commit = "commit;"
            cursor.execute(commit)
            result = "album " + album + "added"
            cursor.close()
            self.dbConnectionClose()
            return result  
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)        

    def delete_album(self,album):
        cursor = self.conn.cursor()
        selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
        print(selectStatement)
        try:
            cursor.execute(selectStatement)
            row = cursor.fetchone()
            index = row[0]
            print(index)
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)
        deleteStatement = "Delete from `Music`.artist_albums where `Music`.artist_albums.index = " + str(index) + ";"       
        print(deleteStatement)
        try:
            cursor.execute(deleteStatement)
            commit = "commit;"
            cursor.execute(commit)
            result = "album " + album + "deleted"
            cursor.close()
            self.dbConnectionClose()
            return result  
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)


        '''
            get from table by id  **********************
        ''' 
 
    def get_by_id(self,id,itemType):
        
        if itemType == 'artist':
            table = 'Music.artist'
        elif itemType == 'song':
            table = 'Music.album2songs'
        elif itemType == 'album':
            table = 'artist_albums'
        else:
            table = 'Music.album2songs'
            
        statement = "select * from " + table + " where " + table + ".index  = "  + str(id) + ";"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            cursor.close()
            self.dbConnectionClose()
            return result
        except mysql.connector.Error as err:
            print("Exception is ", err)
            return str(err)   

         
if __name__  == '__main__':
    
    import unittest
    class TestConnector(unittest.TestCase):
        
        def test_get_count_Artist(self):
            mux = musicGet_Functions()
            table = 'Music.artist'
            criteria = ""
            expected = 537
            result = mux.get_count(table, criteria)
            print("get_count artist",result)
            self.assertEqual(expected,result)
              
        def test_get_count_Artist_Albums(self):
            mux = musicGet_Functions()
            table = 'Music.artist_albums'
            criteria = ""
            expected = 909
            result = mux.get_count(table, criteria)
            print("get_count albums",result)
            self.assertEqual(expected,result)
            
        def test_get_count_album2Songs(self):
            mux = musicGet_Functions()
            table = 'Music.album2songs'
            criteria = ""
            expected = 6625
            result = mux.get_count(table, criteria)
            print("get_count songs",result)
            self.assertEqual(expected,result)              
                    
        def test_get_all(self):
            expected = 556
            mux = musicGet_Functions()
            result = mux.get_all("`Music`.album2songs.album, `Music`.album2songs.artist", "`Music`.album2songs","where `Music`.album2songs.genre like 'folk'" )
            print(len(result))
            self.assertEqual(expected, len(result))
        
        def testGetMaxArtist(self):
            mux = musicGet_Functions()
            table = 'artist'
            expected = 537
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
            
        def testGetMaxAlbums(self):
            mux = musicGet_Functions()
            table = 'artist_albums'
            expected = 909
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])

        def testGetMaxSongs(self):
            mux = musicGet_Functions()
            table = 'album2songs'
            expected = 6624
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
        
        def test_artist_album_song_exist(self):
            mux = musicGet_Functions()
            expected = False
            result = mux.test_artist_album_song_exist('Ten Years After', 'A Space In Time', '04 Over the Hill.m4p')
            print('Expect False ', result)
            self.assertFalse(expected, result)

        def test_artist_album_song_Notexist(self):
            mux = musicGet_Functions()
            expected = True
            result = mux.test_artist_album_song_exist('Ten Years After', 'A Space In Time', '09 Over the Hill.m4p')
            print('Expecte True ', result)
            self.assertTrue(expected, result)
            
        def test_Add_Song(self):
            mux = musicGet_Functions()
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            result = mux.add_one_song(artist, album, song)
            print("add song result is ", result)
            self.assertEqual(result,"Success" )

#        def test_get_Song(self):
#            mux = musicGet_Functions()
#            expected = (6625,'OSXAir.home','/Users/rduvalwa2/Music/iTunes/iTunes Music/Music','TestArtist_X','TestAlbum_X','TestSong.mpX','Rock','Download')
#            result = mux.get_song('TestSong.mpX')
#            print(result[0])
#            self.assertEqual(expected,result[0])
     
     
        def test_delete_songs(self):
            mux = musicGet_Functions()
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            expected = song + " deleted"
            result = mux.delete_one_song(artist, album, song)
#            result = mux.get_song('TestSong.mpX')
#            print(result)
            self.assertEqual(expected,result)            
            
        def test_get_Album(self):
            mux = musicGet_Functions()
            album = 'A Space In Time'
            expected = (664, 'Ten Years After', 'A Space In Time', 'Rock', 'Download')
            result = mux.get_album(album)
            self.assertEqual(expected,result[0])

        def test_get_Artist(self):
            mux = musicGet_Functions()
            expected =  (411, 'Ten Years After', 'Blues')
            result = mux.get_artist('Ten Years After')
            self.assertEqual(expected,result[0])

        def test_get_artistAlbums_from_Albums(self):
            mux = musicGet_Functions()
            expected = [(664, 'Ten Years After', 'A Space In Time', 'Rock', 'Download'), (665, 'Ten Years After', 'Recorded Live', 'Rock', 'Download'), (666, 'Ten Years After', 'Undead (Remastered) [Live]', 'Rock', 'Download')]
            result = mux.get_artistAlbums_fromAlbums('Ten Years After')
            self.assertEqual(expected, result)
        
        

    '''
        def testGetMaxAlbums(self):
            mux = musicGet_Functions()
            table = 'artist_albums'
            expected = 868
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
 
        def testGetMaxSongs(self):
            mux = musicGet_Functions()
            table = 'album2songs'
            expected = 6569
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0])
 
           
        def testGetMaxAlbumSongs(self):
            mux = musicGet_Functions()
            table = 'album2songs'
            expected = 6569
            result = mux.get_max_index(table)
            self.assertEqual(expected,result[0]) 
       
        def test_get_dirs_artist(self):
            mux = musicGet_Functions()
            base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            musicArtist = mux.get_music_artist()
            self.assertIn( (409, 'The Charlie Daniels Band'), musicArtist, "Charlie Daniels Band not there")

        def test_albumList(self):
            mux = musicGet_Functions()
            alms = mux.get_albums()
            self.assertIn((802, "Tim O'Brien", 'Cornbread Nation'), alms, "Cornbread Nation not present")

        def test_songList(self):
            mux = musicGet_Functions()
            mysongs = mux.get_all_songs()
            self.assertIn((0, '18 South', 'Soulful Southern Roots Music', '01 Late Night Ramble.mp3'), mysongs, "'01 Late Night Ramble.mp3' song is missing")       
  '''

    unittest.main()    

    
    
    '''   
    print(os.uname().nodename)
    mux = musicGet_Functions()
    print(mux.get_song('Song For David.mp3'))
    print("All albums ",mux.get_count('music.artist_albums'))
    print("All songs ",mux.get_count('music.album2songs'))
    print("All artist ",mux.get_count('artist'))
    criteria = " where genre = 'TexMex'"
    table = 'music.artist_albums'
    print("All TexMex albums ", mux.get_count(table,criteria))
    texMexTable = 'music.album2songs'
    print("All TexMex songs ", mux.get_count(texMexTable,criteria))
    allTexMexSongs = mux.get_all("music.album2songs.song", texMexTable, criteria)
    for song in allTexMexSongs:
        print(song[0])
    criteria = " where genre = 'TexMex'"
    allTexMexAlbums = mux.get_all("distinct music.album2songs.album", texMexTable, criteria)
    for album in allTexMexAlbums:
        print("TexMex Album: ",album[0])
    
    print(mux.get_artist("Bill Withers"))
    print(mux.get_artistAlbums_fromAlbums("Bill Withers"))
    
 #   mux.close_connection()
     '''
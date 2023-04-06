'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2
'''
import pymysql
import os, platform, sys


class connection_db:

    def connect_music(self):
        pass


class musicFile: 
    
    def __init__(self):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'Macbook16.local':
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
            self.server = 'MaxBook16' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
        elif platform.uname().node == 'OSXAir.local':
            print("Host is " , 'OsxAir')
            self.conn = pymysql.connect(host='OSXAir.local', user='rduvalwa2', password='blu4jazz', db='Music_Test')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
        
        else:
            print('Node is localhost')
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
            self.server = 'localhost' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"     
      
             
    def get_record_count(self, table):
        statement = "select count(*) from " + table + ";"
        cursor = self.conn.cursor()
        cursor.execute(statement)
        count = cursor.fetchone()
        self.conn.close()   
        return count        
    
    def get_max_index(self, table):
        self.table = 'Music_Test.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table + ";"
        cursor = self.conn.cursor()
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        self.conn.close()   
        return maxIndex

    def get_select_Album(self, fields, constraints):
        dbCursor = self.conn.cursor()
        statement = "select " + fields + " from Music_Test.artist_albums " + constraints + ";"  # where Albums.index = 3;"
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
        dbCursor.close()
        self.conn.close()
        return row

    def get_select_Artist(self, fields, constraints):
        dbCursor = self.conn.cursor()
        statement = "select " + fields + " from Music_Test.artist " + constraints + ";"  # where Albums.index = 3;"
        print(statement)
        dbCursor.execute(statement)
        rows = dbCursor.fetchall()  
        dbCursor.close()     
        self.conn.close() 
        return rows      
    
    def get_select_ArtistAlbums(self, fields, constraints):
        dbCursor = self.conn.cursor()
        statement = "select " + fields + " from Music_Test.artist_albums" + constraints + ";"
        print(statement)
        dbCursor.execute(statement)
        row = dbCursor.fetchone()
        dbCursor.close()
        self.conn.close()
        return row        
    
    def select_song_by_criteria(self, statement):
        '''
        Select a song or songs by criteria.
        '''
        rows = []
        cursor = self.conn.cursor()
        self.statement = statement
        cursor.execute(statement)
        row = cursor.fetchone()
        while row is not None:
                rows.append(row)
                row = cursor.fetchone()
        cursor.close()
        self.conn.close()
        return rows
    
    '''
    Load artist
    '''

    def get_music_artist(self):
        artist = []
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                if directory!= '.DS_Store' and directory!= '.localized':
                    artist.append((directory))
        artist.sort()
        return artist
    
    def initial_insert_into_artist(self): 
        self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
        cursor = self.conn.cursor()
        cursor.execute("truncate  artist;")
        
        allArtist = self.get_music_artist()
        for artist in allArtist:
                if "\'"in artist:
#                    print("found apostrophe")
                    artist = artist.replace("'", "\\\'")
#                    print("artist", artist)
                insertStatement = "INSERT into artist  values(\"" + artist + "\"," + "\"GENRE"  + "\");"
#                print(insertStatement)
                cursor.execute(insertStatement)

        cursor.execute("commit;")
        print("done initial insert to artist")
        cursor.close()
  #      self.conn.close()
    
    '''
    End load artist
    '''
    
    '''
    load albums
    '''
    
    def get_albums(self):
        base = self.base  # "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music"
        albums = []
        artists = self.get_music_artist()
        
        for a in artists:
            artist = a
            if os.path.isdir(base + "/" + artist):
                artist_albums = os.listdir(base + "/" + artist)
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append(( artist, album))
                        
        return albums
    
    def initial_insert_into_artist_albums(self): 
        self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
        truncate = "truncate `artist_albums`;"
        cursor = self.conn.cursor()
        cursor.execute(truncate)
        albums = []
        artists = self.get_music_artist()
        for a in artists:
            artist = a
            if "\'"in artist:
#                    print("found apostrophe")
                    artist = artist.replace("'", "\\\'")
#                    print("artist", artist)
            if artist != '.DS_Store':
                artistAlbums = os.listdir("/Users/rduvalwa2/Music/Music/Media.localized/" + a) # do not remove apostrophe for directory search
                for album in artistAlbums:
                    if album != '.DS_Store':
                        albums.append(album)
                        if "\'"in album:
                                album = album.replace("'", "\\\'")
                        insertStatement = "INSERT into Music_Test.artist_albums (artist_albums.artist,artist_albums.album)  values('" + artist + "','" + album + "');" #"+ "\",\"" + album[2] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
                        cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        return albums        
    '''
    End load albums
    '''   
    '''
        Begin get songs
    '''

    def get_all_songs(self):
        print("Start get all songs")
        songs = []
        albums = self.get_albums()
#        print(albums)
        for a in albums:
            if os.path.isdir(self.base + "/" + a[0] + "/" + a[1] ):
#                        print(os.listdir(self.base + "/" + a[0] + "/" + a[1]))
                        album_songs = os.listdir(self.base + "/" + str(a[0]) + "/" + str(a[1]))
                        for song in album_songs:
                            if song != '.DS_Store':
                                if "\'"in song:
                                    song = song.replace("'", "\\\'")
 #                                  print(str(a[0]),",", str(a[1]),",", song)
                                    songs.append((str(a[0]), str(a[1]), song))
                                else:
                                    songs.append((str(a[0]), str(a[1]), song))
#                                   print(str(a[0]),",", str(a[1]),",", song)
                                
#        print("All songs returned")
#        print(songs)

        return songs
    
    def get_all_songs_type_genre(self):
        cursor = self.conn.cursor()
        sync_statement = "UPDATE album2songs t1 INNER JOIN artist_albums t2 ON t1.album = t2.album SET t1.genre = t2.genre, t1.type = t2.type;"
        cursor.execute(sync_statement)
        commit = "commit;"
        cursor.execute(commit)    
    
    def get_songs(self, artist, album='all'):
        print("artist is ", artist)
        print("Album is ", album)
        base = self.base
        albums = []
        songs = []
#        newIndex = 0
        print("path is ", self.base + "/" + artist)
        if(os.path.isdir(base + "/" + artist)):
            artist_albums = os.listdir(base + "/" + artist)
            print("artist_albums: ", artist_albums)
            if album == 'all':
                albums = os.listdir(self.base + "/" + artist)
                print("Albums are ", albums)
                for al in artist_albums:
                    print("Album is ", al)
                    if al != '.DS_Store':
                            albumSongs = os.listdir(self.base + "/" + artist + "/" + al)
                            songs.append(albumSongs)
            if album != 'all':
                songs = os.listdir(self.base + "/" + artist + "/" + album)
        return songs

    def initial_insert_into_album2songs(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        print("Start initial insert into album2songs")
        self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
        cursor = self.conn.cursor()
        trunkate = "truncate  music.album2songs;"
        cursor.execute(trunkate)
        allSongs = self.get_all_songs()
        for song in allSongs: 
                print(song)             
                insertStatement = "INSERT into album2songs (album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type,album2songs.medium)  values(\"" + str(song[0]) + "\",\"" + str(song[1]) + "\",\"" + str(song[2]) + "\",\"" + "" + "\",\"" + "" + "\",\"" + "" +"\");"
                print(insertStatement)
                cursor.execute(insertStatement)
        cursor.execute("commit")


        print("done initial insert album2songs")
        self.conn.close()

    def add_songs(self, artist, album='all'):
        '''
        This code adds song
        '''
        cursor = self.conn.cursor()
        maxIndex = self.get_max_index("album2songs")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        if album == 'all': 
            songs = self.get_songs(artist)
        else:
            songs = self.get_songs(artist, album)
        print(songs)
        for song in songs:
                insertStatement = "INSERT into album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + self.server + "\",\"" + self.base + "\",\"" + song[1] + "\",\"" + song[2] + "\",\"" + song[3] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
                print(insertStatement)
                cursor.execute(insertStatement)
                newIndex = newIndex + 1
        countStatement = "SELECT count(*) FROM music_2.album2songs;"        
        cursor.execute(countStatement)
        count = cursor.fetchone()
        print(count)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()
    


    def add_album(self, album, artist, tipe):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        maxIndex = self.get_max_index("artist_albums")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        insertStatement = "INSERT into artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type)  values(" + str(newIndex) + ",\"" + artist + "\",\"" + album + "\",\"" + tipe + "\")"
        print(insertStatement)
        cursor.execute(insertStatement)
        count = cursor.fetchone()
        print(count[0])
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()
        
#  Not done
    def delete_album(self, album):
        cursor = self.conn.cursor()
        selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        index = row[0]
        print(index)
        deleteStatement = "Delete from artist_albums where `Music`.artist_albums.index = " + str(index) + ";"       
        print(deleteStatement)
        cursor.execute(deleteStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()
        
    def add_artist(self, artist, genre):
        cursor = self.conn.cursor()
        maxIndex = self.get_max_index("artist")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex) 
        insertStatement = "INSERT into artist (artist.index, artist.artist,artist.genre)  values(" + str(newIndex) + ",\"" + artist + "\",\"" + genre + "\")"
        print(insertStatement)
        cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()

    def delete_artist(self, artist):
        cursor = self.conn.cursor()
        selectStatement = "select artist.index from artist where artist.artist like " + "'" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        index = row[0]
        print(index)
        deleteStatement = "Delete from artist where `Music`.artist.index = " + str(index) + ";"       
        print(deleteStatement)
        cursor.execute(deleteStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()

    def dbConnectionClose(self):
        self.conn.close()    

    
if __name__ == '__main__':
    mux = musicFile()
#    mux.initial_insert_into_artist()
#    mux.initial_insert_into_artist_albums()
    mux.initial_insert_into_album2songs()
#    mySongs = mux.get_all_songs()
#    for song in mySongs:
#        print(song)    
#    albums = mux.get_albums()
#    for al in albums:
#        print(str(al[0]) + "\t"  +   str(al[1]))

    

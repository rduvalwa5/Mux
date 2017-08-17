'''
Down load Python 3.6.1
Created on Feb 16, 2017
improve for Python 3.6
@author: rduvalwa2
OSXAir:bin rduvalwa2$ pip3.6 install mysqlclient
Collecting mysqlclient
  Downloading mysqlclient-1.3.10.tar.gz (82kB)
    100% |████████████████████████████████| 92kB 795kB/s 
Installing collected packages: mysqlclient
  Running setup.py install for mysqlclient ... done
Successfully installed mysqlclient-1.3.10
OSXAir:bin rduvalwa2$ 

import MySQLdb as connDb 
new process see the WindowsMusicFile.py

add Pillow ot Windows:
1) change permissions to directory where Python is so that you can read, write, modify
2) C:\Program Files\Python36-32\Scripts>pip3.6.exe install Pillow
Collecting Pillow
  Using cached Pillow-4.1.1-cp36-cp36m-win32.whl
Collecting olefile (from Pillow)
  Using cached olefile-0.44.zip
Installing collected packages: olefile, Pillow
  Running setup.py install for olefile ... done
Successfully installed Pillow-4.1.1 olefile-0.44

other wise you will see this:
error: could not create 'c:\program files\python36-32\Lib\site-packages\olefile': Access is denied
''' 
import os
import platform
import MySQLdb  # as connDb
from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx

class musicGet_Functions:   
    def __init__(self,isNotTest):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn  = MySQLdb.connect(host='OSXAir.home',user='rduval',password='blu4jazz',db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home':
            self.conn  = MySQLdb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn  = MySQLdb.connect(host=login_info_osxAir['host'],user=login_info_osxAir['user'],password=login_info_osxAir['password'],db=login_info_osxAir['db'])
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn  = MySQLdb.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn  = MySQLdb.connect(host='OSXAir.home',user='rduval',password='blu4jazz',db='Music')            
        else:
            print("Host is " , 'default')
            self.conn  = MySQLdb.connect(host='OSXAir.home',user='rduval',password='blu4jazz',db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun =  isNotTest
    '''
    Get max index values from tables
    '''
    def set_safe_update(self):
        cursor = self.conn.cursor()
        statement = 'SET SQL_SAFE_UPDATES = 0;'
        try:
            cursor.execute(statement)
            cursor.close()           
        except self.conn.Error as err:
                print("Exception is ", err)
        self.conn.close()
        
    def verify_normalized_table(self):
            cursor = self.conn.cursor()
            statement = "SELECT a.`index`, a.song, a.artist,a.album, a.path \
                     FROM `Music`.album2songs a \
                     WHERE a.`index` NOT IN (SELECT n.`song_idx` FROM `Music`.normal_song n);"
            try:
                cursor.execute(statement)
                result = cursor.fetchall()  
#                print("Result is ", result)
                cursor.close()
                return result             
            except self.conn.Error as err:
                print("Exception is ", err)
                return str(err)
            self.conn.close()
        
    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
        try:
            cursor = self.conn.cursor()
            cursor.execute( max_index_statement)
            maxIndex = cursor.fetchone()
            cursor.close()
            return maxIndex
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
                
    def get_count(self,table = 'music.album2songs', criteria = " "):
        statement = "select count(*) from " + table + " "  + criteria + ";"
        print("get count statement ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            count = cursor.fetchone()  
            print("Count is from get count ", count[0])
            cursor.close()
            return count[0]       
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_type_count(self,tipe):
        criteria = "where music.album2songs.type = '" + tipe + "'"
        result = self.get_count('music.album2songs', criteria)
        return result

    def get_genre_count(self,gen):
        criteria = "where music.album2songs.genre = '" + gen + "'"
        result = self.get_count('music.album2songs', criteria)
        return result

    def get_all_genre_count(self):
        statement = "SELECT a.genre, count(a.genre) FROM `Music`.album2songs a GROUP BY a.genre ORDER BY a.genre;"
        print("genres count statement ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            genresCount = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            print("Genres Count",genresCount)
            return genresCount                   
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_all_type_count(self):
        statement = "SELECT a.`type`, count(a.`type`) FROM `Music`.album2songs a GROUP BY a.`type` ORDER BY a.`type`;"
        print("type count statement ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            typeCount = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            print("Type Count",typeCount)
            return typeCount                   
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_genres(self):
        statement = "SELECT * FROM `Music`.genre;"
        print("genres ", statement)
        genres = []
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            genres = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            print("Genres ",genres)
            return genres                   
        except self.conn.Error.Error as err:
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
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)
               
    def dbConnectionClose(self):
        self.conn.close()         
    
    '''
        Song  ********************
    '''

    def update_song_artist(self,artist,song,album):
        statement = "update `Music`.album2songs set artist = '" + artist + "' where song like '%" + song + "' and album like '" + album + "' ;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            cursor.execute("commit;")
            cursor.close()
            self.dbConnectionClose()
            return song + "updated successfully"            
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_song(self,song,album):
        fields = '*'
        statement = "Select " + fields + " from music.album2songs where song like '%" + song + "' and album like '" + album + "' ;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result            
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_AllSongs(self):
        statement = "select a.`index`, a.artist, a.album, a.song from `Music`.album2songs a;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result            
        except self.conn.Error.Error as err:
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
        except self.conn.Error.Error as err:
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
        except self.conn.Error.Error as err:
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
        except self.conn.Error.Error as err:
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
            except self.conn.Error.Error as err:
                print("Exception is ", err)
                return str(err)      

    def add_songs_in_path(self,path,album,artist,genre,inType):
        '''
        mux = musicGet_Functions()
        myPath = "/Users/rduvalwa2/music/iTunes/iTunes Music/Music/Seals & Crofts/Seals & Crofts Greatist Hits"
        album = "Seals & Crofts/Seals & Crofts Greatist Hits"
        artist = "Seals & Crofts"
        genre = "Rock"
        inType = "CD"    
        mux.add_songs_in_path(myPath, album, artist, genre, inType)   
        '''       
        idx = self.get_max_index('album2songs')
        cursor = self.conn.cursor()
        print(idx)
        index = idx[0] + 1
        base =   path
        songs = []
#        print("base ",base)
        if os.path.isdir(base):
#            print(base)
            album_songs = os.listdir(path)
            print(album_songs)
            for song in album_songs: 
                if song != '.DS_Store':
                        print("song", song)
                        songs.append((index,song))
                        index = index + 1

            for song in songs:
#                print(song)
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(song[0]) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + artist + "\",\""  +  album + "\",\""  + song[1] + "\",\""  + genre + "\",\""  + inType + "\")"
                print(insertStatement)
                cursor.execute( insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()        

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
    
    def add_song(self,artist,album,song,genre,typ):
        '''
        This code adds song
        '''
        cursor = self.conn.cursor()
        maxIndex =  self.get_max_index("album2songs")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + artist + "\",\""  + album + "\",\""  + song + "\",\""  + genre + "\",\""  + typ + "\")"
        print(insertStatement)
        cursor.execute( insertStatement)
        countStatement = "SELECT count(*) FROM music.album2songs;"        
        cursor.execute(countStatement)
        count = cursor.fetchone()
        print(count)
        commit = "commit;"
        cursor.execute(commit)
        result = "added " + song
        cursor.close()
        self.dbConnectionClose()
        return result 
    
    
    def delete_song(self,idx):
        '''
        delete  from `Music`.album2songs where song like 'Song_Song';
        '''
        if self.notTestRun:
            statement = "delete  from `Music`.album2songs where `index` = " + str(idx) + ";"
            print(statement)
            cursor = self.conn.cursor()
            cursor.execute( statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()
    
    '''
        Artist  ********************
    '''
    def get_all_artist(self):
#       select music.artist.index, artist, genre from music.artist where artist = 'Bill Withers';
        fields = "music.artist.artist, music.artist.index"
#        fields = "*"
        statement = "select " + fields + " from music.artist;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)               


    def get_artist(self,artist):
#       select music.artist.index, artist, genre from music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist where artist like '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
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
#            self.dbConnectionClose()
            return "Added " + artist
        except self.conn.Error as err:
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
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
        deleteStatement = "Delete from `Music`.artist where `Music`.artist.index = " + str(index) + ";"       
        print(deleteStatement)
        try:
            cursor.execute(deleteStatement)
            commit = "commit;"
            cursor.execute(commit)
            cursor.close()
#            self.dbConnectionClose()
            return "deleted " + artist
        except self.conn.Error as err:
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
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
    def get_artistSongs_fromSongs(self,artist):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "music.album2songs.song, music.album2songs.album"
        statement = "select " + fields + " from music.album2songs where artist like '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            print(result)
            cursor.close()
            self.dbConnectionClose()
            return result   
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
    '''
        Album  ********************
    '''  
    def get_all_albums(self):
        fields = "artist_albums.index, artist_albums.album, artist_albums.artist"
        statement = "select " + fields + " from music.artist_albums order by artist_albums.album;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result           
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)         
            
    def get_album(self,album):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where album like '" + album + "';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            return result           
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err) 

    def get_album_songs(self,album):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
#        albumSongs = []
        fields = "music.album2songs.song"
        if album == 'all':
            statement = "select " + fields + " from music.album2songs order by `index`;"
        else:   
            statement = "select " + fields + " from music.album2songs where album = '" + album + "' order by `index`;"
        
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            cursor.close()
            self.dbConnectionClose()
            return result           
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err) 

    def get_artist_songs(self,artist):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
#        albumSongs = []
        fields = "music.album2songs.song"
        statement = "select " + fields + " from music.album2songs where artist = '" + artist + "';"
        
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            cursor.close()
            self.dbConnectionClose()
            return result           
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err) 

    def add_album(self,album,artist,genre = 'Rock' ,tipe = 'Download'):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        maxIndex =  self.get_max_index("artist_albums")
        index = maxIndex[0]
        newIndex = index + 1
        print(newIndex)
        insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.genre, artist_albums.type)  values(" + str(newIndex) + ",\""  + artist + "\",\""  + album + "\",\"" + genre + "\",\""  + tipe + "\")"
        print(insertStatement)
        try:
            cursor.execute(insertStatement)
            #        count = cursor.fetchone()
            commit = "commit;"
            cursor.execute(commit)
            result = "album " + album + "added"
            cursor.close()
#            self.dbConnectionClose()
            return result  
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)        

    def update_album(self,album,field,value):
        cursor = self.conn.cursor()
        execute = False
        print(type(value))
        if type(value) == type('str'): 
            statement = "update `Music`.`artist_albums` set " + field + " = '" + value  +"' where album like '" + album +"';"
            print(statement)
        if type(value) == type(99):
            print("INT Input........")
            statement = "update `Music`.`artist_albums` set " + field + " = " + value  +" where album like '" + album +"';"
            print(statement)
        try:
                cursor.execute(statement)
                execute = True
        except self.conn.Error as err:
                print("Exception is ", err)
                return str(err)        
        if execute:   
            commit = "commit;"
            cursor.execute(commit)
        cursor.close()

    def delete_album(self,album):
        cursor = self.conn.cursor()
        selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
        print("Delete Select .......",selectStatement)
        try:
            cursor.execute(selectStatement)
            row = cursor.fetchone()
            print("Rowwww ", row[0])
            index = row[0]
            print("Delete Album index.....",index)
        except self.conn.Error as err:
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
#            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_all_album_covers(self):
        cursor = self.conn.cursor()
        statement = "select * from `Music`.album_covers;"
        print("get cover statement ", statement)
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            return result
            cursor.close()
#            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_album_cover(self,cover):
        cursor = self.conn.cursor()
        statement = "select * from `Music`.album_covers ac where ac.album_cover like '" + cover + "';"
        print("get cover statement ", statement)
        try:
            cursor.execute(statement)
            result = cursor.fetchone()
            print(result)
            return result
            cursor.close()
#            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_album_cover_count(self):
        cursor = self.conn.cursor()
        statement = "select count(*)  from `Music`.album_covers;"
        try:
            cursor.execute(statement)
            result =cursor.fetchone()
            return result[0]
            cursor.close()
#            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
    def add_album_cover(self,cover):
        cursor = self.conn.cursor()
        statementIdx = "select max(cover_idx) from `Music`.album_covers;"
        cursor.execute(statementIdx)
        idx = cursor.fetchone()
        print("MAX ***********", idx[0])
        newIdx = idx[0] + 1   
        print("*********** New covver    ", newIdx) 
#        statement = insert into `Music`.album_covers values ('BobbyDarin_MackTheKnife.jpeg','',303,'');
        statement = "insert into `Music`.album_covers values ('" + cover + "',''," + str(newIdx) + ",'');"
        print(statement)
        cursor.execute(statement)
        cursor.execute("commit;")
        print(self.get_album_cover(cover))
        return self.get_album_cover(cover)
    
    def delete_album_cover(self,cover):
        cursor = self.conn.cursor()
        cover_result = self.get_album_cover(cover)
        coverIdx = cover_result[2]
        print("cover result delete", coverIdx)
        statement = "delete from `Music`.album_covers where cover_idx = " + str(coverIdx) + ";"
        print(statement)
        cursor.execute(statement)
        cursor.execute("commit;")




    '''
            get from table by id  **********************
    ''' 
 
    def get_by_id(self,objId,itemType):
        
        if itemType == 'artist':
            table = 'Music.artist'
        elif itemType == 'song':
            table = 'Music.album2songs'
        elif itemType == 'album':
            table = 'artist_albums'
        else:
            table = 'Music.album2songs'
            
        statement = "select * from " + table + " where " + table + ".index  = "  + str(objId) + ";"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            cursor.close()
            self.dbConnectionClose()
            return result
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)   

         
if __name__  == '__main__':
    import unittest
    import Test_Results
    
    class TestConnector(unittest.TestCase):
            
        def test_type_count(self):
            mux = musicGet_Functions(True)
            for tipe in Test_Results.typeList:
                print("Type IS...", tipe[0])
                expected = tipe[1]
                result =  mux.get_type_count(tipe[0])
                print(result)
                self.assertEqual(expected, result) 
                      
        def test_genre_count(self):
            mux = musicGet_Functions(True)
            gList = Test_Results.genreList
            for gen in gList:
                expected = gen[1]
                print("expect for genre ", gen[0])
                result = mux.get_genre_count(gen[0])
                self.assertEqual(expected,result)
                    
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
            expected = Test_Results.artist_albums_count  #932
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
            
        def test_Add_Song(self):
            mux = musicGet_Functions(True)
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            result = mux.add_one_song(artist, album, song)
            print("add song result is ", result)
            self.assertEqual(result,"Success" )

        def test_get_Song(self):
            thisSong = 'Johnny B. Goode.mp3'
            thisAlbum = 'The Best of Chuck Berry'
            mux = musicGet_Functions(True)
#            expected =  (946, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
            expected = Test_Results.get_song
            result = mux.get_song(thisSong,thisAlbum)
            print("song result is ",result[0])
            self.assertEqual(expected,result[0])
        
        def test_delete_songs(self):
            mux = musicGet_Functions(True)
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            expected = song + " deleted"
            result = mux.delete_one_song(artist, album, song)
            self.assertEqual(expected,result)            
            
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
 #           ((664, 'Ten Years After', 'A Space In Time', 'Blues', 'Download'), (665, 'Ten Years After', 'Recorded Live', 'Blues', 'Download'), (666, 'Ten Years After', 'Undead (Remastered) [Live]', 'Rock', 'Download'))
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
            value = '99999'
            mux.update_album(album,field,value)
            update_result =  mux.get_album(album)
            print("Update Result.........", update_result)
            expected = ((1058, 'Test_Crud_Artist', 'Test_Crud_Album', 'Test_Crud_Genre', 'Test_Crud_Type', 'Test_Crud_cover', 99999),)
            self.assertEqual(expected, update_result, "album update failure")

        def test_get_album_count(self):  
            mux = musicGet_Functions(True)
            expected = Test_Results.cover_count
            result = mux.get_album_cover_count()
#            print("***** album cover count is ",result)
            self.assertEqual(expected, result, "cover count wrong")
 
        def test_album_update_albumName(self):  
            mux = musicGet_Functions(True)
#            mux.set_safe_update_delete()
            album = "Test_Crud_Album"
            field = 'album'
            value = "Test_Album_Name_Crud"
            mux.update_album(album, field,value)
            result =  mux.get_album(value)
            print(result)
            expected =  ((1058, 'Test_Crud_Artist', 'Test_Album_Name_Crud', 'Test_Crud_Genre', 'Test_Crud_Type', 'Test_Crud_cover', 99999),)
            self.assertEqual(expected, result, "album update failure")
            
        def test_delete_album(self):
            mux = musicGet_Functions(True)
#            album = "Test_Crud_Album"  
#            album = "Test_Album_Name_Update" 
            album = "Test_Album_Name_Crud"                     
            mux.delete_album(album)
#            print("Get album delete.......", mux.get_album(album))
#            print("EEEEnd Crud Testttttt")
            result = mux.get_album(album)
            self.assertEqual((),result, "Delete failed")

        def test_get_albumcover(self):
            mux = musicGet_Functions(True)
            albumCover = '80-81.jpg'
            getCoverResult = mux.get_album_cover(albumCover)
            self.assertEqual(albumCover, getCoverResult[0], "add album cover failed")


        def test_add_albumcover(self):
            mux = musicGet_Functions(True)
            albumCover = "Test Cover"
            mux.add_album_cover(albumCover)
            getCoverResult = mux.get_album_cover(albumCover)
            self.assertEqual(albumCover, getCoverResult[0], "add album cover failed")
            
        def test_delete_albumcover(self):
            albumCover = "Test Cover"
            mux = musicGet_Functions(True)
            mux.delete_album_cover(albumCover)
            expected = None
            deleteResult = mux.get_album_cover(albumCover)
            self.assertEqual(expected, deleteResult, "delete album cover failed")
            
            
              

    unittest.main()    
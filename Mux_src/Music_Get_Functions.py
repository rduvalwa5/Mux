'''
Down load Python 3.6.1
Created on Feb 16, 2017

Updated April 3 2023

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
import pymysql.cursors


class musicGet_Functions:   

    def __init__(self):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'Macbook16.local':
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
            self.server = 'MaxBookPro17OSX' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized/"
        elif platform.uname().node == 'OSXAir.local':
            print("Host is " , 'OsxAir')
            self.conn = pymysql.connect(host='OSXAir.local', user='rduvalwa2', password='blu4jazz', db='Music_Test')
            self.server = 'OSXAir' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized/"
        
        else:
            print('Node is localhost')
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
            self.server = 'default' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized/"       
    '''
    Get max index values from tables
    '''

    def set_safe(self):
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
                     WHERE a.`index` NOT IN (SELECT n.`song_idx` FROM `Music_Test`.normal_song n);"
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
    '''    
Get rid of indexes    
    def get_max_index(self, table):
        self.table = '`Music_Test`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table + ";"
        print("max index statement ",max_index_statement)
        try:
            cursor = self.conn.cursor()
            cursor.execute(max_index_statement)
            maxIndex = cursor.fetchone()
            cursor.close()
            return maxIndex
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        ''' 
                       
    def get_count(self, table="'Music_Test'.album2songs", criteria =" "):
        statement = "select count(*) from " + table + " " + criteria + ";"
        print("$$$$$$$$$")
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

    def get_type_count(self, tipe):
        criteria = "where Music_Test.album2songs.type = '" + tipe + "'"
        result = self.get_count('Music_Test.album2songs', criteria)
        return result

    def get_genre_count(self, gen):
        criteria = "where Music_Test.album2songs.genre = '" + gen + "'"
        result = self.get_count('Music_Test.album2songs', criteria)
        return result

    def get_all_genre_count(self):
        statement = "SELECT a.genre, count(a.genre) FROM `Music_Test`.album2songs a GROUP BY a.genre ORDER BY a.genre;"
        print("genres count statement ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            genresCount = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            print("Genres Count", genresCount)
            return genresCount                   
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_all_type_count(self):
        statement = "SELECT a.`type`, count(a.`type`) FROM `Music_Test`.album2songs a GROUP BY a.`type` ORDER BY a.`type`;"
        print("type count statement ", statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            typeCount = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            print("Type Count", typeCount)
            return typeCount                   
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_genres(self):
        statement = "SELECT * FROM `Music_Test`.genre order by genre;"
        print("$$$$$$$$")
        print("genres ", statement)
        genres = []
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            genres = cursor.fetchall()  
            cursor.close()
            self.dbConnectionClose()
            print("$$$$$$$$")
            print("Genres ", genres)
            return genres                   
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_all(self, fields="*", table='Music_Test.album2songs', criteria=" "):
        statement = "select " + fields + " from " + table + " " + criteria + ";"
        print("%%%%%%%%%%%%%%%")
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

    def update_song_album_name(self, new_album_name, song, album):
        statement = "update `Music_Test`.album2songs set album = '" + new_album_name + "' where song like '%" + song + "' and album like '" + album + "' ;"
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
        
    def update_song_name(self, new_name, song, album):
        statement = "update `Music_Test`.album2songs set song = '" + new_name + "' where song like '%" + song + "' and album like '" + album + "' ;"
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

    def update_song_artist(self, artist, song, album):
        statement = "update `Music_Test`.album2songs set artist = '" + artist + "' where song like '%" + song + "' and album like '" + album + "' ;"
        getSongStatement = "Select * from music.album2songs where song like '%" + song + "%';"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            print("Update and Get  ", cursor.execute(getSongStatement))
            cursor.execute("commit;")
            cursor.close()
            self.dbConnectionClose()
#            return song + " updated successfully"   
            return  song + " updated successfully"       
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def update_song_genre(self, genre, song, album):
        statement = "update `Music_Test`.album2songs set genre = '" + genre + "' where song like '%" + song + "' and album like '" + album + "' ;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            cursor.execute("commit;")
            cursor.close()
            self.dbConnectionClose()
            return song + " updated successfully"            
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)
        
    def update_song_type(self, typ, song, album):
        statement = "update `Music_Test`.album2songs set type = '" + typ + "' where song like '%" + song + "' and album like '" + album + "' ;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            cursor.execute("commit;")
            cursor.close()
            self.dbConnectionClose()
            return song + " updated successfully"            
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_song(self, song):
        statement = "Select song from Music_Test.album2songs where song like '%" + song + "%' ;"
#        statement = "Select * from Music_Test.album2songs where song like '%" + song + "%';"
        print("********************************")
        print(statement)
        print("********************************")
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchone()
            print("get_song result: ", result)
            cursor.close()
            self.dbConnectionClose()
            return result            
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_AllSongs(self):
        statement = "select a.artist, a.album, a.song from `Music_Test`.album2songs a order by a.artist, a.album, a.song;"
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

    def get_songs(self, artist, album='all'):
        base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        newIndex = 0
        if os.path.isdir(base + "/" + artist):
                artist_albums = os.listdir(base + "/" + artist)
                print("artist_albums: ", artist_albums)
                if album == 'all':
                    for al in artist_albums:
                        if al != '.DS_Store':
                            albums.append((artist, al))
                            album_songs = os.listdir(base + "/" + artist + "/" + al)
                            for song in album_songs:
                                    songs.append((newIndex, artist, al, song))
                elif  album != 'all':
                    for al in artist_albums:
                        if al == album:
                            if al != '.DS_Store':
                                albums.append((artist, al))
                                album_songs = os.listdir(base + "/" + artist + "/" + al)
                                for song in album_songs:
                                    songs.append((newIndex, artist, al, song))
        return songs

    def test_artist_album_song_exist(self, artist, album, song):
        cursor = self.conn.cursor()
        statement = "select * from Music_Test.album2songs where Music_Test.album2songs.song like '" + song + "' and Music_Test.album2songs.artist like '" + artist + "' and Music_Test.album2songs.album like '" + album + "';"        
        try:
            cursor.execute(statement)
            result = cursor.fetchone()
            print(result)
            cursor.close()
            self.dbConnectionClose()
            print('Result is ', result)
            if result == None:
                return  True
            else:
                return False
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err)        
    
    def add_one_song(self, artist, album, song, genre='Rock', tipe='Download'):  
        cursor = self.conn.cursor()               
        statement = "insert into `Music_Test`.album2songs (album,artist,genre,song,type) values('" + album + "','" + artist + "','" + genre + "','" + song + "','" + tipe + "');"
        try:
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
#            getStatement = "SELECT * FROM Music_Test.album2songs where song = \"" + song + "\";"        
#            cursor.execute(getStatement)
#            thisSong = cursor.fetchone()
#            print("Added song is ", thisSong)
            cursor.close()
            self.dbConnectionClose()
 #           return "Song added " + str(thisSong)
        except self.conn.Error.Error as err: 
            print("Exception is ", err)
            return str(err)
                        
    def delete_one_song(self, album, song):
            cursor = self.conn.cursor()
            statement = "delete from `Music_Test`.album2songs where song like '" + song + "';"  # and album like '" + album + "' and artist like '" + artist + "';"
            print("delete ", statement)
            try:
                cursor.execute(statement)
                commit = "commit;"
                cursor.execute(commit)
                cursor.close()
                self.dbConnectionClose()
                return song + " deleted"  
            except self.conn.Error as err:
                print("Exception is ", err)
                return str(err)      

    def add_songs_in_path(self, path, album, artist, genre, inType, medium):
        '''
        mux = musicGet_Functions()
        myPath = "/Users/rduvalwa2/music/iTunes/iTunes Music/Music/Seals & Crofts/Seals & Crofts Greatist Hits"
        album = "Seals & Crofts/Seals & Crofts Greatist Hits"
        artist = "Seals & Crofts"
        genre = "Rock"
        inType = "CD"    
        mux.add_songs_in_path(myPath, album, artist, genre, inType)   
        ''' 
        cursor = self.conn.cursor()
        print(path) 
        print(os.path.isdir(path))     
        base = path
        songs = []
#        print("base ",base)
        if os.path.isdir(base):
#            print(base)
            album_songs = os.listdir(path)
            print(album_songs)
            for song in album_songs: 
                if song != '.DS_Store':
                        songs.append((song))
            for song in songs:
                print(song)
                insertStatement = "INSERT into Music_Test.album2songs (album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type, album2songs.medium)  values(" + "\"" + artist + "\",\"" + album + "\",\"" + song + "\",\"" + genre + "\",\"" + inType + "\",\"" + medium + "\");"
                print(insertStatement)
                cursor.execute(insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        self.conn.close()        

    def add_songs(self, artist, album='all'):
        '''
        This code adds song
        '''
        cursor = self.conn.cursor()
        if album == 'all': 
            songs = self.get_songs(artist)
        else:
            songs = self.get_songs(artist, album)
        print(songs)
        for song in songs:
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type, album2songs.medium))  values(" + "\"" + self.server + "\",\"" + self.base + "\",\"" + song[1] + "\",\"" + song[2] + "\",\"" + song[3] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
                print(insertStatement)
                cursor.execute(insertStatement)
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
    
    def add_song(self, artist, album, song, genre, typ, medium):
        '''
        This code adds song
        '''
        cursor = self.conn.cursor()
#        maxIndex = self.get_max_index("album2songs")
        insertStatement = "INSERT into Music_Test.album2songs (album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type,album2songs.medium)  values(\"" + artist + "\",\"" + album + "\",\"" + song + "\",\"" + genre + "\",\"" + typ + "\",\"" + medium +"\");"
        print("***********************")
        print(insertStatement)
        cursor.execute(insertStatement)
        getStatement = "SELECT song, album FROM Music_Test.album2songs where song = " "\"" + song +  "\";"  
        cursor.execute(getStatement)
        thisSong = cursor.fetchone()
        print("Added song is ", thisSong)
        commit = "commit;"
        cursor.execute(commit)
        result = (song, album)
        cursor.close()
        self.dbConnectionClose()
        return result 
    
    def delete_song(self, song, album):
        '''
        delete  from `Music`.album2songs where song like 'Song_Song';
        '''
        statement = "delete from `Music_Test`.album2songs where album2songs.song like '%" + song + "%' and album like '%" + album + "%';"
        print("*** Delete Song **************")
        print(statement)
        try:
            cursor = self.conn.cursor()
#            safe = "SET SQL_SAFE_UPDATES = 0;"       
#            cursor.execute(safe)

            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            cursor.close()
            return "delete successfull "
        except Exception  as e:
            print("Exception is ", e)

    '''
        Verify Table Syncs For Genre Type  ********************
    '''
    def get_sync_Album_ArtistGenre(self):
        statement = "select aa.`album`, aa.`artist`, aa.genre,  a.artist, a.genre from artist a , artist_albums aa where a.artist = aa.`artist` and aa.artist not in ('Compilations')and  a.`genre` != aa.`genre`;"
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

    def get_sync_type(self):
        statement = "select distinct aa.`album`, aa.type, ab.album ,ab.type, ab.artist from artist_albums aa , album2songs ab where aa.`album` = ab.`album`and  aa.`type` != ab.`type`;"
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

    def get_sync_genre_songsgenre(self):
        statement = "select distinct aa.`album`, aa.genre, ab.album ,ab.genre, ab.artist from artist_albums aa , album2songs ab where aa.`album` = ab.`album` and  aa.`genre` != ab.`genre`;"
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



    '''
        Artist  ********************
    '''

    def get_all_artist(self):
#       select music.artist.index, artist, genre from music.artist where artist = 'Bill Withers';
        fields = "Music_Test.artist.artist, Music_Test.artist.genre"
#        fields = "*"
        statement = "select " + fields + " from Music_Test.artist order by Music_Test.artist.artist;"
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

    def doesArtistExist(self, artist):
        cursor = self.conn.cursor()
        selectStatement = "Select  Music_Test.artist.artist from Music_Test.artist where  Music_Test.artist.artist = '" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        if aritstIndex != None:
            returnCode = 'True'
        else:
            returnCode = 'False'
        return returnCode

    def get_artist(self, artist):
        fields = "*"
        statement = "select " + fields + " from Music_Test.artist where artist like '" + artist + "';"
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
                             
    def add_artist(self, artist, genre):
        if self.doesArtistExist(artist) == 'False':
            cursor = self.conn.cursor()
            insertStatement = "INSERT into Music_Test.artist (artist.artist,artist.genre)  values("+ "\"" + artist + "\",\"" + genre + "\");"
            print(insertStatement)
            cursor.execute(insertStatement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
            cursor.close()
            return "Success " + artist
        else:
            print(artist, " already exist in data table Music.artist.")
            return "artist already exist in table"  
        
    def update_artist(self, artist, genre):
        cursor = self.conn.cursor() 
        updateStatement = "UPDATE Music_Test.artist SET GENRE = '" + genre + "' where artist like '" + artist + "';" 
        print(updateStatement)
        try:
            cursor.execute(updateStatement)
            commit = "commit;"
            cursor.execute(commit)
            cursor.close()
            print("done")
#            self.dbConnectionClose()
            return "Updated " + artist
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
    def delete_artist(self, artist):
        cursor = self.conn.cursor()
#        selectStatement = "select artist from Music_Test.artist where artist.artist like " + "'" + artist + "';"
#        print(selectStatement)
#        try:
#            cursor.execute(selectStatement)
#            row = cursor.fetchone()
#            artist = row[0]
#            print(artist)
#        except self.conn.Error as err:
#            print("Exception is ", err)
#            return str(err)
        
        deleteStatement = "Delete from `Music_Test`.artist where `Music_Test`.artist.artist = '" + artist + "';"       
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

    def get_artistAlbums_fromAlbums(self, artist):
        fields = "*"
        statement = "select " + fields + " from Music_Test.artist_albums where artist like '%" + artist + "%';"
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
        
    def get_artistSongs_fromSongs(self, artist):
        fields = "Music_Test.album2songs.song, Music_Test.album2songs.album"
        statement = "select " + fields + " from Music_Test.album2songs where artist like '" + artist + "';"
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
        fields = "artist_albums.album, artist_albums.artist"
        statement = "select " + fields + " from Music_Test.artist_albums order by artist_albums.artist, artist_albums.album;"
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
            
    def get_album(self, album):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "album"
        statement = "select * from Music_Test.artist_albums where album like '" + album + "';"
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

    def get_album_songs(self, album):
        fields = "song"
        if album == 'all':
            statement = "select " + fields + " from Music_Test.album2songs order by album, song;"
        else:   
            statement = "select " + fields + " from Music_Test.album2songs where album like '" + album + "' order by song;"
        print("$$$$$$$$$$$")
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            
            print(result) 
            cursor.close()
            self.dbConnectionClose()
            return result           
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err) 

    def get_artist_songs(self, artist):
        fields = "song"
        statement = "select " + fields + " from Music_Test.album2songs where artist like '" + artist + "';"
        print("&&&&&&&&&&&&")
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            cursor.close()
            self.dbConnectionClose()
            print("$$$$$$$$$$$")
            print(result)
            return result           
        except self.conn.Error.Error as err:
            print("Exception is ", err)
            return str(err) 

    def add_album(self, album = "Album XXX",  artist = "Artist XXXX", genre='Rock' , tipe='Download', medium = "CD"):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        insertStatement = "INSERT into Music_Test.artist_albums (artist_albums.artist,artist_albums.album,artist_albums.genre, artist_albums.type,artist_albums.medium )  values("+ "\"" + artist + "\",\"" + album + "\",\"" + genre + "\",\"" + tipe + "\",\"" + medium +"\")"
        print("album ", album )
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
        
    def update_album(self,album, field, value):
        cursor = self.conn.cursor()
        safe = "SET SQL_SAFE_UPDATES = 0;"  
        cursor.execute(safe)
        statement = "update `Music_Test`.artist_albums set artist_albums." + field + " = '" + value + "' where artist_albums.album like '" + album + "';"
        print("#########")
        print(statement)
        cursor.execute(statement)
        commit = "commit;"
        cursor.execute(commit)
        cursor.close()
        
    def delete_album_byindex(self, idx):
        cursor = self.conn.cursor()
        safe = "SET SQL_SAFE_UPDATES = 0;"  
        cursor.execute(safe)
        deleteStatement = "delete from `Music`.artist_albums where `index` = " + str(idx) + "';"  
        print('*****679   ', deleteStatement)
        try:
            cursor.execute(deleteStatement)
            commit = "commit;"
            cursor.execute(commit)
            result = "album " + idx + "deleted"
            print("741  ", result)
            cursor.close()
            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            print("Delete Album Exception is ", err)
            cursor.close()
            return err

    def delete_album_by_name(self, album_name):
        cursor = self.conn.cursor()
        safe = "SET SQL_SAFE_UPDATES = 0;"  
        cursor.execute(safe)
        deleteStatement = "delete from `Music_Test`.artist_albums where album = '" + album_name + "';"  
        print('*****Delete Album   ', deleteStatement)
        try:
            cursor.execute(deleteStatement)
            commit = "commit;"
            cursor.execute(commit)
            result = "album " + album_name + "deleted"
            print("deleted album result  ", result)
            cursor.close()
            self.dbConnectionClose()
            return result  
        except self.conn.Error as err:
            errorr = "Delete Album by Name Exception is " + err
            print(errorr)
            cursor.close()
            return errorr

    def get_all_album_covers(self):
        cursor = self.conn.cursor()
        statement = "select * from `Music_Test`.album_covers order by album_cover;"
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

    def get_album_cover(self, cover):
        cursor = self.conn.cursor()
        statement = "select * from `Music_Test`.album_covers where album_cover like '" + cover + "';"
        print("get cover statement ", statement)
        try:
            cursor.execute(statement)
            result = cursor.fetchall()
            print("#####")
            print("XXXget_album_cover result ", result)
            return result
            cursor.close()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)

    def get_album_cover_count(self):
        cursor = self.conn.cursor()
        statement = "select count(*)  from `Music_Test`.album_covers;"
        try:
            cursor.execute(statement)
            result = cursor.fetchone()
            return result[0]
            cursor.close()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
    def add_album_cover(self, cover,album):
        cursor = self.conn.cursor()
        statementIdx = "select max(idx) from `Music_Test`.album_covers;"
        cursor.execute(statementIdx)
        idx = cursor.fetchone()
        print("@@@@@@@")
        print("MAX ***********", idx)
        if idx[0] is None:
            print("idx is none")
            maxCover = 0
        else:
            print("idx is NOT none")
            maxCover = idx[0] 
        newIdx = maxCover + 1   
        print("*********** New covver    ", newIdx) 
        statement = "insert into `Music_Test`.album_covers(`idx`,`album_cover`,`album`) values (" + str(newIdx) + ",'" + cover + "','" + album + "');"
        print(statement)
        cursor.execute(statement)
        cursor.execute("commit;")
        print("Get Cover Result is ", self.get_album_cover(cover))
        return self.get_album_cover(cover)
        
    def delete_album_cover(self, album_cover):
        print("Start Delete ")
        safe = "SET SQL_SAFE_UPDATES = 0;"       
        cursor = self.conn.cursor()
        print("cover name ", album_cover)
        deleteStatement = "Delete from `Music_Test`.album_covers where album_cover like '" + album_cover + "' ;"  
        print("delete statement ", deleteStatement)      
        result = cursor.execute(deleteStatement)
        print("deleteStatement******************")
        print("Delete Result is ", result)
        cursor.execute("commit;")
        cursor.close()

    def update_album_cover(self, cover, newName):
        cursor = self.conn.cursor()
        cover_result = self.get_album_cover(cover)
        coverIdx = cover_result[0][2]
        print("cover result update", coverIdx)
        if coverIdx == None:
            return "Update Failed cover Not Found"
            exit
        if coverIdx != None:
            statement = "update `Music_Test`.album_covers set album_cover = '" + newName + "' where album_cover like '" + cover + "';"
            print(statement)
            cursor.execute(statement)
            cursor.execute("commit;")

    '''
            get from table by id  **********************
    ''' 
 
    def get_by_name(self, name, itemType):
        
#       if itemType == 'artist':
#            table = 'Music_Test.artist'
#        elif itemType == 'song':
#            table = 'Music_Test.album2songs'
#        elif itemType == 'album':
#            table = 'Music_Test.artist_albums'
#        else:
#            table = 'Music_Test.album2songs'
        
        if itemType == 'artist':
            statement = "select * from Music_Test.artist where artist like '" + name + "';"
        elif itemType == 'album':
            statement = "select * from Music_Test.artist_albums where album like '" + name + "';"
        elif itemType == 'song':
            statement = "select * from Music_Test.album2songs where song like '" + name + "';"
        else:
            print("Item tpye not found********")   
            
#        statement = "select * from " + table + " where " + table + ".index  = " + str(objId) + ";"
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
            mux = musicGet_Functions()
            for tipe in Test_Results.typeList:
                print("Type IS...", tipe[0])
                expected = tipe[1]
                result =  mux.get_type_count(tipe[0])
                print(result)
                self.assertEqual(expected, result) 
                       
        def test_genre_count(self):
            mux = musicGet_Functions()
            gList = Test_Results.genreList
            for gen in gList:
                expected = gen[1]
                print("expect for genre ", gen[0])
                result = mux.get_genre_count(gen[0])
                self.assertEqual(expected,result, gen)
                    
        def test_get_all_songs(self):
            mux = musicGet_Functions()
            expected = Test_Results.songs_count  # 6831
            result = mux.get_AllSongs()
            print("All songs count is ", len(result))
            print(result[0])
            self.assertEqual(expected, len(result),"Song count is wrong")
       
        def test_get_count_Artist(self):
            mux = musicGet_Functions()
            table = 'Music_Test.artist'
            criteria = ""
            expected = Test_Results.artist_count # 564
            result = mux.get_count(table, criteria)
            print("get_count artist",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
        def test_get_count_Artist_Albums(self):
            mux = musicGet_Functions()
            table = 'Music_Test.artist_albums'
            criteria = ""
            expected = Test_Results.artist_albums_count  #932
            result = mux.get_count(table, criteria)
            print("get_count albums",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)
            
        
        def test_get_count_album2Songs(self):
            mux = musicGet_Functions()
            table = 'Music_Test.album2songs'
            criteria = ""
            expected = Test_Results.songs_count
            result = mux.get_count(table, criteria)
            print("get_count songs",result)
            mux.dbConnectionClose()
            self.assertEqual(expected,result)              
                    
        def test_get_all_folk_albums(self):
            expected = Test_Results.folk_albums # 576
            mux = musicGet_Functions()
            result = mux.get_all("`Music_Test`.artist_albums.album", "`Music_Test`.artist_albums","where `Music_Test`.artist_albums.genre like 'Folk'" )
            print(len(result))
            self.assertEqual(expected, len(result))

        def test_get_all_folk_songs(self):
            expected = Test_Results.folk_songs # 576
            mux = musicGet_Functions()
            result = mux.get_all("`Music_Test`.album2songs.album, `Music_Test`.album2songs.artist", "`Music_Test`.album2songs","where `Music_Test`.album2songs.genre like 'folk'" )
            print(len(result))
            self.assertEqual(expected, len(result))
       
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
            print('Expect True ', result)
            self.assertTrue(expected, result)
           
        def test_crud_Add_Song(self):
            print("Song Crud Test *********************7")
            mux = musicGet_Functions()
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            mux.add_one_song(artist, album, song)
            
        def test_crud_Delete_Song(self):
            mux = musicGet_Functions()
            song = 'TestSong.mpX'    
            album = 'TestAlbum_X'        
            mux.delete_one_song(album,song)
            deletedSong = mux.get_song(song, album)
            print(deletedSong)
            self.assertFalse( deletedSong == song, msg = "End Song Crud Test")
            print("End Song Crud Test *******************8")

        def test_get_Song(self):
            thisSong = "05 Dogs Of War.mp3"
            thisAlbum = "Rock Or Bust"
            mux = musicGet_Functions()
#            expected =  (946, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
#            expected = Test_Results.get_song
            expected = mux.get_song(thisSong,thisAlbum)
            print(type(expected))
            print("get song expected is")
            print(expected)
            self.assertTrue(expected[0] == "05 Dogs Of War.mp3")
        
        def test_delete_songs(self):
            mux = musicGet_Functions()
            artist = 'TestArtist_X'
            album = 'TestAlbum_X'
            song = 'TestSong.mpX'
            expected = song + " deleted"
            result = mux.delete_one_song(album, song)
            self.assertEqual(expected,result)            
            
        def test_get_Album(self):
            mux = musicGet_Functions()
            album = 'A Space In Time'
            expected = Test_Results.get_album  # (664, 'Ten Years After', 'A Space In Time', 'Blues', 'Download')
            result = mux.get_album(album)
            print(str(result))
            
            self.assertTrue(str(result).__contains__('A Space In Time'), msg = "Tuple does not contain A Space In Time")
            
        def test_Artist_Albums(self):
            mux = musicGet_Functions()
            result = mux.get_artistAlbums_fromAlbums('AC_DC')
            expected = 4
            print("$$$$$$$")
            print("albums ", result)
            print("length all albums", len(result))
            self.assertEqual(expected, len(result),"All album count wrong")

        def test_get_Artist(self):
            mux = musicGet_Functions()
            expected = Test_Results.get_artist   # (411, 'Ten Years After', 'Blues')
            result = mux.get_artist('Ten Years After')
            self.assertEqual(expected,result[0])

       
        def test_get_album_songs(self):
            mux = musicGet_Functions()
            expected = (('01 One of These Days.m4p',), ('02 Here They Come.m4p',), ("03 I'd Love to Change the World.m4p",), ('04 Over the Hill.m4p',), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p",), ('06 Once There Was a Time.m4p',), ('07 Let the Sky Fall.m4p',), ('08 Hard Monkeys.m4p',), ("09 I've Been There Too.m4p",), ('10 Uncle Jam.m4p',))
            result = mux.get_album_songs('A Space In Time')
            print("artist albums ", result)
            self.assertEqual(expected, result, "song list for A Space In Time wrong" )

        def test_get_artist_songs(self):
            mux = musicGet_Functions()
            expected = (('01 Highway to Hell.mp3',), ('01 Rock Or Bust.mp3',), ('07 Hard Times.mp3',), ('02 Play Ball.mp3',), ('06 Got Some Rock & Roll Thunder.mp3',), ('04 Miss Adventure.mp3',), ('08 Baptism By Fire.mp3',), ('10 Sweet Candy.mp3',), ('03 Rock The Blues Away.mp3',), ('05 Dogs Of War.mp3',), ('09 Rock The House.mp3',), ('11 Emission Control.mp3',), ('07 You Shook Me All Night Long.m4a',), ('06 Back In Black.mp3',), ("01 It's a Long Way to the Top (If You Wanna Rock 'N' Roll).mp3",))
            result = mux.get_artist_songs('AC_DC')
            print("artist songs", result)
            self.assertEqual(expected, result, "song list for Ten Years After wrong" )

        def test_genres(self):
            mux = musicGet_Functions()
            genres = mux.get_genres()
            self.assertEqual(Test_Results.genresList, genres, "genre list is wrong")
                
        def test_get_album_cover__count(self):  
            mux = musicGet_Functions()
            expected = Test_Results.cover_count
            result = mux.get_album_cover_count()
#            print("***** album cover count is ",result)

        def test_get_albumcover(self):
            mux = musicGet_Functions()
            albumCover = 'Amazulu Montego Bay.jpg'
            getCoverResult = mux.get_album_cover(albumCover)
            self.assertEqual(albumCover, getCoverResult[0][1], "add album cover failed")

        def test_add_albumcover(self):
            mux = musicGet_Functions()
            albumCover = "Test Cover"
            album = "TestAlbum"
            mux.add_album_cover(albumCover,album)
            getCoverResult = mux.get_album_cover(albumCover)
            self.assertEqual(albumCover, getCoverResult[0][1], "add album cover failed")
            
        def test_delete_albumcover(self):
            albumCover = "Test Cover"
            mux = musicGet_Functions()
            mux.delete_album_cover(albumCover)
            expected = ()
            deleteResult = mux.get_album_cover(albumCover)
            print("--------")
            self.assertEqual(expected, deleteResult, "delete album cover failed")
               
    unittest.main()    


import os
import mysql.connector
from Music_Get_Functions import musicGet_Functions
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
#        print(self.conn)
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
#        print(count[0])
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()

    """
    Initial Load functions
    """
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
#        print(count[0])
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
#        print(count)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        
    def sync_song_type(self):
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs t1 INNER JOIN `Music`.artist_albums t2 ON t1.album = t2.album SET t1.type = t2.type;"
        cursor.execute(statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()       

    def sync_song_genre(self): 
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs t1 INNER JOIN `Music`.artist t2 ON t1.artist = t2.artist SET t1.genre = t2.genre;"
        cursor.execute(statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()              

class song_Add_Update_Delete:       
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
#        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'      
        
#    def get_dbConnection(self):
#        if os.uname().nodename == 'C1246895-osx.home':
#            self.conn2 = mysql.connector.Connect(**login_info_osx)
#        elif  os.uname().nodename == 'OSXAir.home.home':
#            self.conn2 = mysql.connector.Connect(**login_info_root)
#        print(self.conn)
#        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
#        self.server = 'OSXAir.home'      
#        return self.conn2
    
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
#                print("artist_albums: ", artist_albums)
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
#        print(newIndex)
        if album == 'all': 
            songs = self.get_songs(artist)
        else:
            songs = self.get_songs(artist,album)
#        print(songs)
        for song in songs:
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + song[1] + "\",\""  + song[2] + "\",\""  + song[3] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
                print(insertStatement)
                cursor.execute( insertStatement)
                newIndex = newIndex + 1
        countStatement = "SELECT count(*) FROM music.album2songs;"        
        cursor.execute(countStatement)
#        count = cursor.fetchone()
#        print(count)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()

    def add_song(self,album,artist,genre,song,type,path='"/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"',server='OSXAir.home' ):
        '''
        insert into `Music`.album2songs (album2songs.index, album, artist,genre,path,server,song,type) 
         values (6599,'SongAlbum','SongArts','SongGenre','/path/path/','song_server','test song','test_type');
        '''
        cursor = self.conn.cursor()
        maxIndex =  self.get_max_index("album2songs")
        index = maxIndex[0]
        newIndex = index + 1
        insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values("  + str(newIndex) + ",\"" + server + "\",\"" + path + "\",\""  + artist + "\",\""  + album + "\",\""  + song + "\",\""  + genre + "\",\""  + type + "\")"
        print(insertStatement)
        cursor.execute( insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
        
    def update_song_album(self, album,song):
        '''
        UPDATE `Music`.album2songs SET album = 'Test_Album' WHERE song = 'Song_Song.mp3';
        '''
#        xconn = self.get_dbConnection()
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET album = '" + album + "' WHERE song = '" + song  + "';"
        print(statement)
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()   
  #      xconn.close()
         
    def update_song_artist(self,artist,song):
        '''
        UPDATE `Music`.album2songs SET artist = 'ZZ_ZTest' WHERE song = 'Song_Song.mp3';
        '''
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET artist = '" + artist + "' WHERE song = '" + song  + "';"
        print(statement)
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()    
    
    def update_song_genre(self,genre,song):
        '''
        UPDATE `Music`.album2songs SET genre = 'Rock' WHERE song = 'Song_Song.mp3';
        '''
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET genre = '" + genre + "' WHERE song = '" + song  + "';"
        print(statement)
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()    
    
    def update_song_type(self,tipe,song):
        '''
        UPDATE `Music`.album2songs SET type = 'CD' WHERE song = 'Song_Song.mp3';
        '''
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET type = '" + tipe + "' WHERE song = '" + song  + "';"
        print(statement)
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()    
    
    def update_song_path(self,path,song):
        '''
        UPDATE `Music`.album2songs SET path = '/home.music/' WHERE song = 'Song_Song.mp3';
        '''
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET path = '" + path + "' WHERE song = '" + song  + "';"
        print(statement)
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()    

    def update_song_server(self,server, song):
        '''
        UPDATE `Music`.album2songs SET server = 'music_server' WHERE song = 'Song_Song.mp3';
        '''
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET server = '" + server + "' WHERE song = '" + song  + "';"
        print(statement)
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()   
  
    def delete_song(self,song):
        '''
        delete  from `Music`.album2songs where song like 'Song_Song';
        '''
        statement = "delete  from `Music`.album2songs where song like '" + song + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute( statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()
    
    def delete_songs(self,artist,albumin='all',songin="all"):
        cursor = self.conn.cursor()   
        delete_songs = self.get_songs(artist,albumin)
#        print("delete songs: ", delete_songs)  
        index = 0
        if albumin == 'all':
            if songin == 'all':   
                for song in delete_songs:
                        selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                        print(selectStatement)
                        cursor.execute(selectStatement)
                        row = cursor.fetchone()
                        index = row[0]  
#                        print("delete index: ", index)         
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

class album_Add_Update_Delete:       
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
#        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'      

    def dbConnectionClose(self):
        self.conn.close()

    def doesAlbumExist(self,album):
        cursor = self.conn.cursor()
        selectStatement = "Select  Music.artist_albums.index from Music.artist_albums where  Music.artist_albums.album = '" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        if aritstIndex != None:
            returnCode = 'True'
        else:
            returnCode = 'False'
        return returnCode

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
        if self.doesAlbumExist(artist) == 'False':
            cursor = self.conn.cursor()
            maxIndex =  self.get_max_index("artist_albums")
            index = maxIndex[0]
            newIndex = index + 1
#            print(newIndex)
            insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type,artist_albums.genre)  values(" + str(newIndex) + ",\""  + artist + "\",\""  + album + "\",\""  + tipe +  "\",\"" + gen +"\" )"
            print(insertStatement)
            cursor.execute(insertStatement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
            self.conn.close()
        else:
            print(album, "already exist in table.")

    def update_album(self,album, artist = 'no_change', genre = 'no_change', tipe = 'no_change'):
        '''
        genre is the only attribute that can change
        update music.artist_albums set genre = 'Rock' WHERE artist = 'Bill Withers';
        '''
        cursor = self.conn.cursor()
        if self.doesAlbumExist(album) == 'True': 
            '''
            build addition of attribute changes
            '''          
            if artist != 'no_change':
                    updateStatement = "UPDATE Music.artist_albums set artist = '" + artist + "' where album = '" + album + "';"
                    if genre != 'no_change':
                            updateStatement = "UPDATE Music.artist_albums set artist = '" + artist + "', genre = '" + genre + "' where album = '" + album + "';"
                            if tipe != 'no_change':
                                updateStatement = "UPDATE Music.artist_albums set artist = '" + artist + "', genre = '" + genre + "' ,type = '" + tipe + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and  genre != 'no_change':
                    if tipe != 'no_change':
                        updateStatement = "UPDATE Music.artist_albums set genre = '" + genre + "', type = '" + tipe + "' where album = '" + album + "';"
                    else:
                        updateStatement = "UPDATE Music.artist_albums set genre = '" + genre + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and genre == 'no_change':
                    if tipe != 'no_change':
                                updateStatement = "UPDATE Music.artist_albums set type = '" + tipe + "' where album = '" + album + "';"
                                print(updateStatement)
                                cursor.execute(updateStatement)
                                commit = "commit;"
                                cursor.execute(commit)
                    else:
                        print("no updates ", artist , genre, tipe )    
            else:
                print("no updates ", artist , genre, tipe )    
        else:
            print(artist," does not exist in data table Music.artist_albums.")            
        print("done")
        cursor.close()
            

    def delete_album(self,album):
        cursor = self.conn.cursor()
        selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        index = row[0]
#        print(index)
        deleteStatement = "Delete from `Music`.artist_albums where `Music`.artist_albums.index = " + str(index) + ";"       
        print(deleteStatement)
        cursor.execute(deleteStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()


        
class artist_Add_Update_Delete:       
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
#        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'     

    def dbConnectionClose(self):
        self.conn.close()

    def doesArtistExist(self,artist):
        cursor = self.conn.cursor()
        selectStatement = "Select  Music.artist.index from Music.artist where  Music.artist.artist = '" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        if aritstIndex != None:
            returnCode = 'True'
        else:
            returnCode = 'False'
        return returnCode

    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table   + ";"
        cursor = self.conn.cursor()
        cursor.execute( max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
                    
    def add_artist(self,artist,genre):
        if self.doesArtistExist(artist) == 'False':
            cursor = self.conn.cursor()
            maxIndex =  self.get_max_index("artist")
            index = maxIndex[0]
            newIndex = index + 1
#            print(newIndex) 
            insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(newIndex) + ",\""  + artist  + "\",\""  + genre + "\")"
            print(insertStatement)
            cursor.execute(insertStatement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
            cursor.close()
        else:
            print(artist," already exist in data table Music.artist.")

    def update_artist(self,artist, genre):
        '''
        genre is the only attribute that can change
        update music.artist set genre = 'Rock' WHERE artist = 'Bill Withers';
        '''
        cursor = self.conn.cursor()
        if self.doesArtistExist(artist) == 'True':            
            updateStatement = "UPDATE Music.artist set genre = '" + genre + "' where artist = '" + artist + "';"
            print(updateStatement)
            cursor.execute(updateStatement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")            
        else:
            print(artist," does not exist in data table Music.artist.")
        cursor.close()

    def delete_artist(self,artist):
        cursor = self.conn.cursor()
        selectStatement = "select artist.index from Music.artist where artist.artist like " + "'" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        print(row)
        index = row[0]
#        print(index)
        deleteStatement = "Delete from `Music`.artist where `Music`.artist.index = " + str(index) + ";"       
        print(deleteStatement)
        cursor.execute(deleteStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
            
if __name__  == '__main__':

#    getSongs = musicLoad_Functions()
#    getSongs.initial_insert_into_album2songs()
#    getSongs.sync_song_type()
#    getSongs.sync_song_genre()
    

#    addArtist = artist_Add_Update_Delete()
    #.initial_insert_into_artist('Sir Douglas Quintet','TexMex')
#    addArtist.add_artist('Sir Douglas Quintet','TexMex')
    
    addAlbum = album_Add_Update_Delete()
    addAlbum.add_album("Mendocino", 'Sir Douglas Quintet', 'download', 'TexMex')
    
    '''
    song = 'Song_Song.mp3'    
 
    album = 'Test_SongAlbum'
    album_up = 'Up_SongAlbum'
    artist = 'Song_Artist'
    artist_up = 'Up_Song_Artist'
    genre = 'Song_genre'
    genre_up = 'Up_Song_genre'
    
    tipe = 'Song_Type'
    tipe_up = 'Up_Song_Type'
    server = 'song_server'
    server_up = 'up_song_server'
    path = '/Test/Music'
    path_up = '/Test/Up_Music'

    Song = song_Add_Update_Delete()
    get = musicGet_Functions()
    Song.add_song(album,artist,genre,song,tipe,path,server)
    Song.update_song_album(album_up, song)
    Song.update_song_artist(artist_up, song)
    Song.update_song_genre(genre_up, song)
    Song.update_song_path(path_up, song)
    Song.update_song_server(server_up, song)
    Song.update_song_type(tipe_up, song)
    result_genre_up = get.get_song_by_song(song)
    print("genre up ", result_genre_up)
    Song.delete_song(song)
    
    update_album = album_Add_Update_Delete()
    print("update all")
    update_album.update_album('Test_AlbumA', 'upArtist', 'UpGenre', 'UpType')
    print("album does not exist")
    update_album.update_album('no album', 'upArtist', 'UpGenre', 'UpType')
    print("update artist and genre")
    update_album.update_album('Test_AlbumA', 'upArtist', 'UpGenre')
    print("update only artist")
    update_album.update_album('Test_AlbumA', 'upArtist')
    print("update no input")
    update_album.update_album('Test_AlbumA')
    print("update only genre")
    update_album.update_album('Test_AlbumA', 'no_change','UpGenre')
    print("update genre and type")
    update_album.update_album('Test_AlbumA', 'no_change','UpGenre','UpType')
    print("update type only")
    update_album.update_album('Test_AlbumA', 'no_change','no_change','UpType')
    update_album.Restore_testAlbum()
    '''
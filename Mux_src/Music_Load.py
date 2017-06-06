import os, platform
import MySQLdb   as connDb
from    Musicdb_info    import login_info_default

class musicLoad_Functions:
    def __init__(self,test = False):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
            self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')

        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
        else:
            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test
        self.genreList = ['Alternative','BlueGrass','Blues','Classic','Country','Folk','Holiday',\
                            'Jazz','Latino','Pop','Regae','Rock','RockaBilly','Soul','Talk', \
                            'TestGenre','TexMex','Traditional','World']
    
    def get_genre_album2songs(self):
        pass
        
    def get_genre_genre(self):
        pass
    
    def set_genre_genre(self,genre):
        print("Start set_genre")
        print(genre)
        cursor = self.conn.cursor()
        for gen in genre:
            statement = "insert into `Music`.genre set genre = '" + gen + "';"
            print(self.does_genre_exist(gen))
            if self.does_genre_exist(gen):
                print(gen , " already exist!")
            else:
                try:
                    print(statement)
                    cursor.execute(statement)
                    print("Success " + gen)
                    cursor.execute("commit;")
                except self.conn.Error.Error as err:
                    print("Exception is ", err)

        cursor.close()
        print("done")

    def does_genre_exist(self,genre):
        cursor = self.conn.cursor()
        statement = "select g.g_idx from `Music`.genre g where genre like '" + genre + "';"
        cursor.execute(statement)
        result = cursor.fetchone()
        if result != None:
            print(result)
            return True
        else:
            return False
            
        cursor.close()
        
        
    
    
    def get_albums(self):
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        index = 0
        artists = self.get_music_artist()
        for a in artists:
            artist = a[1]
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
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
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        artist = self.get_music_artist()
        for a in artist:
            if os.path.isdir(self.base + "/" + a[1]):
                artist_albums = os.listdir(self.base + "/" + a[1])
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((a,album))
                        album_songs = os.listdir(self.base + "/" + a[1] + "/" + album)
                        for song in album_songs:
                            if song != '.DS_Store' and song != 'side1.mp3' and song != 'side2.mp3' and song != 'side3.mp3' and song != 'side4.mp3':
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
        if self.notTestRun:
            for artist in allArtist:
                insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(artist[0]) + ",\"" + artist[1] + "\",\""  + "Rock" + "\")"
                cursor.execute( insertStatement)
            countStatement = "SELECT count(*) FROM music.artist;"        
            cursor.execute(countStatement)
            count = cursor.fetchone()
#            print(count[0])
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
        if self.notTestRun:
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
        allSongs = self.get_all_songs()
        if self.notTestRun:
            trunkate = "truncate  music.album2songs;"
            cursor.execute(trunkate)
            for song in allSongs:
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(song[0]) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + song[1] + "\",\""  + song[2] + "\",\""  + song[3] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
                print(insertStatement)
                cursor.execute( insertStatement)
            countStatement = "SELECT count(*) FROM music.album2songs;"        
            cursor.execute(countStatement)
            count = cursor.fetchone()
            print(count)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        else:
            for song in allSongs:
                insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(song[0]) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + song[1] + "\",\""  + song[2] + "\",\""  + song[3] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
#                print(insertStatement)

        cursor.close()
        
    def sync_song_type(self):
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs t1 INNER JOIN `Music`.artist_albums t2 ON t1.album = t2.album SET t1.type = t2.type;"
        if not self.notTestRun:
            print(statement)
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs t1 INNER JOIN `Music`.artist_albums t2 ON t1.album = t2.album SET t1.type = t2.type;"
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()       

    def sync_song_genre(self): 
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs t1 INNER JOIN `Music`.artist_albums t2 ON t1.album = t2.album SET t1.genre = t2.genre;"
        if not self.notTestRun:
            print(statement)
        if self.notTestRun:
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()              

class song_Add_Update_Delete():       
    def __init__(self,test = False):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
            self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')

        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
        else:
            self.conn = connDb.Connect(**login_info_default)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test 
        
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
        if self.notTestRun:
            for song in songs:
                print(song[3])
                if song[3] != ".DS_Store":
                    insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + self.server + "\",\"" + self.base + "\",\""  + song[1] + "\",\""  + song[2] + "\",\""  + song[3] + "\",\""  + "rock" + "\",\""  + "download" + "\")"
#                    print(insertStatement)
                    cursor.execute( insertStatement)
                    newIndex = newIndex + 1
            countStatement = "SELECT count(*) FROM music.album2songs;"        
            cursor.execute(countStatement)
#            count = cursor.fetchone()
#            print(count)
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
        if self.notTestRun:
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
        if self.notTestRun:
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
        statement = "UPDATE `Music`.album2songs SET artist = '" + artist + "' WHERE song like '" + song  + "';"
        print(statement)

        if self.notTestRun:
            cursor.execute( statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()    
  
    def update_songs_artists(self,songs):
        '''
        UPDATE `Music`.album2songs SET artist = 'ZZ_ZTest' WHERE song = 'Song_Song.mp3';
        '''
        artistSongs = songs  
        for item in artistSongs:
            cursor = self.conn.cursor()
            statement = "UPDATE `Music`.album2songs SET artist = '" + item[1] + "' WHERE song like '" + item[0]  + "';"
            print(statement)
            if self.notTestRun:
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
        if self.notTestRun:
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
        if self.notTestRun:
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
        if self.notTestRun:
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
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs SET server = '" + server + "' WHERE song = '" + song  + "';"
            print(statement)
            cursor.execute( statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()   
  
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
    
    def delete_songs(self,artist,albumin='all',songin="all"):
        cursor = self.conn.cursor()   
        delete_songs = self.get_songs(artist,albumin)
#        print("delete songs: ", delete_songs)  
        index = 0
        if albumin == 'all':
            if songin == 'all':   
                for song in delete_songs:
                    if self.notTestRun:
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
                        if self.notTestRun:
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
                            if self.notTestRun:
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
                                if self.notTestRun:
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
    def __init__(self,test = False):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
            self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')

        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
        else:
            self.conn = connDb.Connect(**login_info_default)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test

    def dbConnectionClose(self):
        self.conn.close()

    def doesAlbumExist(self,album):
        cursor = self.conn.cursor()
        selectStatement = "Select Music.artist_albums.index from Music.artist_albums where Music.artist_albums.album like '" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        print("aritstIndex issss ",aritstIndex )
        if aritstIndex == None:
            returnCode = 'False'
        else:
            returnCode = 'True'
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
        if self.doesAlbumExist(album) == 'False':
            cursor = self.conn.cursor()
            maxIndex =  self.get_max_index("artist_albums")
            index = maxIndex[0]
            newIndex = index + 1
#            print(newIndex)
            if self.notTestRun:
                insertStatement = "INSERT into Music.artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type,artist_albums.genre)  values(" + str(newIndex) + ",\""  + artist + "\",\""  + album + "\",\""  + tipe +  "\",\"" + gen +"\" )"
                print(insertStatement)
                cursor.execute(insertStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")
            self.conn.close()
            return "Success " + album
        else:
            print(album, "Already exist in table.")
            return "Already exist in table."

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
                if self.notTestRun:
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
                if self.notTestRun:
                    if tipe != 'no_change':
                        updateStatement = "UPDATE Music.artist_albums set genre = '" + genre + "', type = '" + tipe + "' where album = '" + album + "';"
                    else:
                        updateStatement = "UPDATE Music.artist_albums set genre = '" + genre + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and genre == 'no_change':
                if self.notTestRun:
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
        if self.notTestRun:
            selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
            print(selectStatement)
            cursor.execute(selectStatement)
            try:
                row = cursor.fetchone()
                index = row[0]
                deleteStatement = "Delete from `Music`.artist_albums where `Music`.artist_albums.index = " + str(index) + ";"       
                print(deleteStatement)
                cursor.execute(deleteStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")
                cursor.close()
                return "Success"
            except TypeError:
                print("Album not found")
                return "Album not found"


        
class artist_Add_Update_Delete:       
    def __init__(self,test = False):
        print("*************** Node Name is ",platform.uname().node)
        if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
            self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')

        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
        else:
            self.conn = connDb.Connect(**login_info_default)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test  

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
            if self.notTestRun:
                insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(newIndex) + ",\""  + artist  + "\",\""  + genre + "\")"
                print(insertStatement)
                cursor.execute(insertStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")
            cursor.close()
            return "Success " + artist
        else:
            print(artist," already exist in data table Music.artist.")
            return "artist already exist in table"
    def update_artist(self,artist, genre):
        '''
        genre is the only attribute that can change
        update music.artist set genre = 'Rock' WHERE artist = 'Bill Withers';
        '''
        cursor = self.conn.cursor()
        if self.doesArtistExist(artist) == 'True':
            if self.notTestRun:            
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
        print('deleting ',row)
        index = row
#        print(index)
        if self.notTestRun:
            deleteStatement = "Delete from `Music`.artist where `Music`.artist.index = " + str(index) + ";"       
            print(deleteStatement)
            cursor.execute(deleteStatement) 
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()

'''
Use only select statements
'''

class verify_data_tables:
        def __init__(self,test = True):
            print("*************** Node Name is ",platform.uname().node)
            if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
                self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')

            elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
                self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
                self.conn  = connDb.connect(host='OSXAir.home',user='root',password='blu4jazz',db='Music')
            else:
                self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            self.server = 'OSXAir.home' 
            self.notTestRun = test  
        
        def check_artist_table(self):
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.artist,a.genre FROM `Music`.album2songs a WHERE a.artist NOT IN (SELECT b.artist FROM Music.artist b);"
            print(selectStatement)
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    print(item)
            cursor.close()

        def check_albums_table(self):
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.album, a.artist, a.genre, a.type FROM `Music`.album2songs a WHERE a.album NOT IN (SELECT b.album FROM Music.artist_albums b);"
            print(selectStatement)
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    print(item)
            cursor.close()
            
        def check_genre_songs2albums(self):
            result = []
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.album as 'album album', a.genre as 'album genre', b.genre as 'song genre' FROM `Music`.album2songs b, Music.artist_albums a WHERE a.album = b.album and a.genre != b.genre;"
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    result.append(item)
#                    print(item)
            cursor.close()
            return result
       
        def check_Type_songs2albums(self):
            result = []
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.album as 'album album', a.type as 'album type', b.type as 'song type' FROM `Music`.album2songs b, Music.artist_albums a WHERE a.album = b.album and a.type != b.type;"
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    result.append(item)
#                    print(item)
            cursor.close()
            return result    
        

              
                
if __name__  == '__main__':
    
    runMode = "NoRun" # NoRun  # Test
    trueLoad = musicLoad_Functions(True)
#    testGen = 'Rocky'
#    output = trueLoad.does_genre_exist(testGen)
#    print(output)
#    testGen = 'Rock'
#    output = trueLoad.does_genre_exist(testGen)
#    print(output)
    genreList = ['Alternative','BlueGrass','Blues','Classic','Country','Folk','Holiday',\
                            'Jazz','Latino','Pop','Regae','Rock','RockaBilly','Soul','Talk', \
                            'TestGenre','TexMex','Traditional','World','Easy Listening']
    trueLoad.set_genre_genre(genreList)
    
    
#    if runMode == "NoRun":
#            pass
#    if runMode == "Run":
#        trueLoad = musicLoad_Functions(True)
#        trueLoad.initial_insert_into_album2songs()
#        allSongs = trueLoad.get_all_songs()
#        print('num songs is ', len(allSongs))
    
#        trueLoad.sync_song_genre()
#        trueLoad.sync_song_type()

 

#    verify = verify_data_tables()
#    verify.check_artist_table()
#    verify.check_albums_table()
#    outPutG = verify.check_genre_songs2albums()
#    print('genre outPut is', outPutG)
#    for result in outPutG:
#        print(result)
        
#    outPutT = verify.check_Type_songs2albums()
#   print('genre outPut is', outPutT)
#    for result in outPutT:
#        print(result)


#    addArtist = artist_Add_Update_Delete(True)
#    addArtist.add_artist("AA_Artist", "AA_Genre")
    

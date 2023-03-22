'''
Created on Jan 27, 2018

@author: rduvalwa2
'''
import os, platform
import MySQLdb
from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx


class derivedAlbumLoad_Functions:

    def __init__(self, test=False):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduval', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home.home':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test
        self.genreList = ['Alternative', 'BlueGrass', 'Blues', 'Classic', 'Country', 'Folk', 'Holiday', \
                            'Jazz', 'Latino', 'Pop', 'Regae', 'Rock', 'RockaBilly', 'Soul', 'Talk', \
                            'TestGenre', 'TexMex', 'Traditional', 'World']
    
    def set_genre_genre(self, genre):
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

    def does_genre_exist(self, genre):
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
 
    def get_music_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index, directory))
                index = index + 1
        return artist
 
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
                        albums.append((index, artist, album))
                        index = index + 1
        return albums
 
    """
    Initial Album Load functions
    """

    def initial_insert_into_Dervided_ArtistAlbums(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        trunkate = "truncate  music.derived_artist_albums;"
        cursor.execute(trunkate)
        allAbums = self.get_albums()
        if self.notTestRun:
            for album in allAbums:
                insertStatement = "INSERT into Music.derived_artist_albums (derived_artist_albums.index, derived_artist_albums.artist,derived_artist_albums.album,derived_artist_albums.genre,derived_artist_albums.type)  values(" + str(album[0]) + ",\"" + album[1] + "\",\"" + album[2] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
                cursor.execute(insertStatement)
            countStatement = "SELECT count(*) FROM music.artist_albums;"        
            cursor.execute(countStatement)
            count = cursor.fetchone()
#        print(count[0])
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()


class derived_album_Add_Update_Delete: 

    def __init__(self, test=False):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduvalwa2', password='blu4jazz', db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test 

    def dbConnectionClose(self):
        self.conn.close()

    def doesAlbumExist(self, album):
        cursor = self.conn.cursor()
        selectStatement = "Select Music.artist_albums.index from Music.artist_albums where Music.artist_albums.album like '" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        print("aritstIndex issss ", aritstIndex)
        if aritstIndex == None:
            returnCode = 'False'
        else:
            returnCode = 'True'
        return returnCode

    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table + ";"
        cursor = self.conn.cursor()
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
    
    def add_album(self, album, artist, tipe, gen):
        if self.doesAlbumExist(album) == 'False':
            cursor = self.conn.cursor()
            maxIndex = self.get_max_index("artist_albums")
            index = maxIndex[0]
            newIndex = index + 1
            if self.notTestRun:
                insertStatement = "INSERT into Music.derived_artist_albums (artist_albums.index, artist_albums.artist,artist_albums.album,artist_albums.type,artist_albums.genre)  values(" + str(newIndex) + ",\"" + artist + "\",\"" + album + "\",\"" + tipe + "\",\"" + gen + "\" )"
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

    def update_album(self, album, artist='no_change', genre='no_change', tipe='no_change'):
        cursor = self.conn.cursor()
        if self.doesAlbumExist(album) == 'True': 
            if artist != 'no_change':
                if self.notTestRun:
                    updateStatement = "UPDATE Music.derived_artist_albums set artist = '" + artist + "' where album = '" + album + "';"
                    if genre != 'no_change':
                            updateStatement = "UPDATE Music.derived_artist_albums set artist = '" + artist + "', genre = '" + genre + "' where album = '" + album + "';"
                            if tipe != 'no_change':
                                updateStatement = "UPDATE Music.derived_artist_albums set artist = '" + artist + "', genre = '" + genre + "' ,type = '" + tipe + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and  genre != 'no_change':
                if self.notTestRun:
                    if tipe != 'no_change':
                        updateStatement = "UPDATE Music.derived_artist_albums set genre = '" + genre + "', type = '" + tipe + "' where album = '" + album + "';"
                    else:
                        updateStatement = "UPDATE Music.derived_artist_albums set genre = '" + genre + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and genre == 'no_change':
                if self.notTestRun:
                    if tipe != 'no_change':
                                updateStatement = "UPDATE Music.derived_artist_albums set type = '" + tipe + "' where album = '" + album + "';"
                                print(updateStatement)
                                cursor.execute(updateStatement)
                                commit = "commit;"
                                cursor.execute(commit)
                    else:
                        print("no updates ", artist , genre, tipe)    
            else:
                print("no updates ", artist , genre, tipe)    
        else:
            print(artist, " does not exist in data table Music.derived_artist_albums.")            
        print("done")
        cursor.close()

    def delete_album(self, album):
        cursor = self.conn.cursor()
        if self.notTestRun:
            selectStatement = "select artist_albums.index from Music.derived_artist_albums where artist_albums.album like " + "'" + album + "';"
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

        
if __name__ == '__main__':
    
    runMode = "Run"  # NoRun  # Test
    
    trueLoad = derivedAlbumLoad_Functions(True)
    genreList = ['Alternative', 'BlueGrass', 'Blues', 'Classic', 'Country', 'Folk', 'Holiday', \
                            'Jazz', 'Latino', 'Pop', 'Regae', 'Rock', 'RockaBilly', 'Soul', 'Talk', \
                            'TestGenre', 'TexMex', 'Traditional', 'World', 'Easy Listening']
    trueLoad.initial_insert_into_Dervided_ArtistAlbums()


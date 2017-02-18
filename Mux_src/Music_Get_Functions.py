'''
Created on Feb 16, 2017

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
        
    def get_count(self,table = 'music.album2songs', criteria = " "):
        statement = "select count(*) from " + table + " "  + criteria + ";"
        cursor = self.conn.cursor()
        cursor.execute(statement)
        count = cursor.fetchone()  
        theCount = count[0]
        return theCount       
    
    def get_all(self,fields = "*",table = 'music.album2songs', criteria = " "):
        statement = "select " + fields + " from " + table + " "  + criteria + ";"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result                   

    def get_song(self,song):
        '''
        '''
        fields = '*'
        statement = "Select " + fields + "from music.album2songs where song = '" + song + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result            


    def get_artist(self,artist):
#       select music.artist.index, artist, genre from music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist where artist = '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result                 

    def get_artistAlbums_fromAlbums(self,artist):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where artist = '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result   
    
    def get_album(self,album):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where album = '" + album + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result           
 
    def get_by_id(self,id,itemType):
        
        if itemType == 'artist':
            table = 'Music.artist'
        elif itemType == 'song':
            table = 'Music.album2songs'
        elif itemType == 'album':
            table = 'artist_albums'
        else:
            talbe = 'Music.album2songs'
            
        statement = "select * from " + table + " where " + table + ".index  = "  + str(id) + ";"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()
        self.dbConnectionClose()
        return result   

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

    def add_songs(self,artist,album='all'):
        '''
        This code adds song
        '''
#        if os.uname().nodename == 'C1246895-osx.home':
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_osx)
#        else:
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_root)
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
#        if os.uname().nodename == 'C1246895-osx.home':
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_osx)
#        else:
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_root)
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
        result = "deleted " + song
        cursor.close()
        self.dbConnectionClose()
        return result  




    def add_album(self,album,artist,tipe):
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
#        if os.uname().nodename == 'C1246895-osx.home':
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_osx)
#        else:
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_root)
        cursor = self.conn.cursor()
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
        result = "album " + album + "added"
        cursor.close()
        self.dbConnectionClose()
        return result  

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
        result = "album " + album + "deleted"
        cursor.close()
        self.dbConnectionClose()
        return result  

    def add_artist(self,artist,genre):
#        if os.uname().nodename == 'C1246895-osx.home':
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_osx)
#        else:
#            self.server = os.uname().nodename
#            conn = mysql.connector.Connect(**login_info_root)
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
        self.dbConnectionClose()
        return "Added " + artist
#        conn.close()



    def delete_artist(self,artist):
 #       if os.uname().nodename == 'C1246895-osx.home':
 #           self.server = os.uname().nodename
 #           conn = mysql.connector.Connect(**login_info_osx)
 #       else:
 #           self.server = os.uname().nodename
 #           conn = mysql.connector.Connect(**login_info_root)
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
        cursor.close()
        self.dbConnectionClose()
        return "deleted " + artist
    
    def dbConnectionClose(self):
        self.conn.close()         
        
if __name__  == '__main__':
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
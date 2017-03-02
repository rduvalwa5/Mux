

'''
Created on Feb 16, 2017

@author: rduvalwa2
'''

import os
import mysql.connector
#from  Musicdb_info import login_info_rd
from Musicdb_info import login_info_root
from Musicdb_info import login_info_osx 
#from mysql.connector.errors import Error


class musicGet_Functions:   
    def __init__(self):
        if os.uname().nodename == 'C1246895-osx.home':
            self.conn = mysql.connector.Connect(**login_info_osx)
        elif  os.uname().nodename == 'OSXAir.home.home':
            self.conn = mysql.connector.Connect(**login_info_root)
#        print(self.conn)
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home'  
        
#    def close_connection(self):
#        self.conn.close() 
            
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
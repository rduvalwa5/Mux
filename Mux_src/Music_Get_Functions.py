'''
Created on Dec 10, 2016

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

    def get_artist_from_artistTable(self,artist):
#       select music.artist.index, artist, genre from music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist where artist = '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result                 

    def get_artistAlbums_from_albums(self,artist):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where artist = '" + artist + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result   
    
    def get_Album_from_ArtistAlbums(self,album):
#       select music.artist.index, artist, genre fmsom music.artist where artist = 'Bill Withers';
        fields = "*"
        statement = "select " + fields + " from music.artist_albums where album = '" + album + "';"
        print(statement)
        cursor = self.conn.cursor()
        cursor.execute(statement)
        result = cursor.fetchall()  
        return result           
    
    def dbConnectionClose(self):
        self.conn.close()         
        
if __name__  == '__main__':
    print(os.uname().nodename)
    mux = musicGet_Functions()
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
    
    print(mux.get_artist_from_artistTable("Bill Withers"))
    print(mux.get_artistAlbums_from_albums("Bill Withers"))
    
    mux.close_connection()
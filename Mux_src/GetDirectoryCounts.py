'''
Created on Dec 30, 2019

INSERT INTO counts (SERVER, artist, albums, songs) VALUES ('Test', 1, 2,3);
INSERT INTO counts (SERVER, artist, albums, songs) VALUES ('Test2',2 , 0,0);

@author: rduvalwa2
'''
import os, platform
import pymysql
from datetime import date
from _datetime import datetime
#from lib2to3.tests.data.infinite_recursion import FILE

class Get_Directory_Counts_Function:

    def __init__(self):
        
        self.server = ""
        self.artistList = []
        self.albumList = [] 
        self.songList = []
        self.albumCoverList = []
        self.artist = 0
        self.albums = 0
        self .songs = 0
        self.genre = 0
        self.covers = 0
               
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'c1246895-osx.hsd1.wa.comcast.net': #'C1246895-osx.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music/"
            self.albumCovers = "/Users/rduvalwa2/git/Mux/AlbumCovers"
            self.server = "C1246895-osx.hsd1.wa.comcast.net"
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            self.albumCovers = "/Users/rduvalwa2/eOxigen-workspace/Mux/AlbumCovers"
            self.server = "OSXAir.hsd1.wa.comcast.net"
        elif platform.uname().node == 'RandyDuvalsMBP.hsd1.wa.comcast.net':
            print("Host is " , 'RandyDuvalsMBP.hsd1.wa.comcast.net')
            self.base = "/Users/rduvalwa2/music/iTunes/iTunes Music/Music"
            self.albumCovers = "/Users/rduvalwa2/git/Mux/AlbumCovers"
            self.server = "RandyDuvalsMBP.hsd1.wa.comcast.net"
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music')            
        else:
            print("Host is not found ")
            exit

    def insertCounts_into_Db(self):
        print("Start Insert Counts into DataBase...")
#        print("Server ",self.server ,"Genre ", self.genre, " artist ", self.artist, " albums ", self.albums, " songs ", self.songs)
        cursor = self.conn.cursor()
        statement = "INSERT INTO counts (SERVER, artist, albums, songs, album_covers, genre) VALUES ('" + self.server + "'," +  str(self.artist) + "," + str(self.albums) + "," + str(self.songs) + "," + str(self.covers) + "," + str(self.genre) + ");" 
        try:
            print("Statement ", statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
        except self.conn.Error as err:
            print("Exception is ", err)
        cursor.close()
 #       return str((("server",self.server),("artist", self.artist),("albums", self.albums), ("songs", self.songs)))
        return str(datetime.now()) + "  " + "server: " + str(self.server) + " artist: " + str(self.artist) + " albums: " + str(self.albums) + " songs: " + str(self.songs) + "\n"
        
    def get_genre_count(self):
        print("Start get genre count")
        cursor = self.conn.cursor()
        statement = "select count(*) from genre;"
        print(statement)
        try:
            cursor.execute(statement)
            count = cursor.fetchone()        
            print("Success ", count[0])
            self.genre = count[0]
        except self.conn.Error as err:
                    print("Exception is ", err)
        cursor.close()
        print("done")
        
    def get_albumCover_count(self):
        albumCovers = os.listdir(self.albumCovers)
        for cover in albumCovers:
            if cover != '.DS_Store':
                self.covers = self.covers + 1
                self.albumCoverList.append(cover)
        print("Cover count is ", self.covers)
        self.albumCoverList = sorted(self.albumCoverList)

    def get_artist_count(self):
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if directory != '.DS_Store':
                if os.path.isdir(self.base + "/" + directory):
                    self.artist = self.artist + 1
                    self.artistList.append(directory)
        self.artistList = sorted(self.artistList)
 
    def get_albums_count(self):
        for a in self.artistList:
            artist = a[1]
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
                for album in artist_albums:
                    if album != '.DS_Store':
                        self.albumList.append(album)
                        self.albums = self.albums + 1
        self.albumList = sorted(self.albumList)
        
    def get_song_count(self):
        for a in self.artistList:
            artist = a
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
                for al in artist_albums:
                    if al != ".DS_Store":
                        albumSongs = os.listdir(self.base + "/" + artist + "/" + al)
                        self.songs = self.songs + len(albumSongs)             
                        for song in albumSongs:
                            self.songList.append(song)
        self.songList = sorted(self.songList)
        print("Song File ", len(self.songList))
    """ https://www.tutorialspoint.com/python/python_files_io.htm """
    def open_write_Songfile(self):
#        rsyncFile = "/Users/rduvalwa2/Public/TestRync/counts.txt"
        songFile = "AASongFile" + self.server + ".txt"
        mysong = open(songFile,'w')
        for song in self.songList:
            if song != '.DS_Store':
                mysong.write(str(song) + "\n")
        mysong.close()


    def open_write_file(self, data):
#        rsyncFile = "/Users/rduvalwa2/Public/TestRync/counts.txt"
        rsyncFile = "counts.txt"
        synFile = open(rsyncFile,'a')
        synFile.write(str(data))
        synFile.close()
  
    def open_read_file(self):
#        rsyncFile = "/Users/rduvalwa2/Public/TestRync/counts.txt"
        rsyncFile = "counts.txt"
        synFile = open(rsyncFile,'r')
        redLines = synFile.readlines()
        print("Lines READ ",redLines)
        for line in redLines:
            print("Line READ ",line)
        synFile.close()
        




if __name__ == '__main__':
    x = Get_Directory_Counts_Function()
    x.get_genre_count()
    x.get_artist_count()
    x.get_albums_count()
    x.get_song_count()
    x.get_albumCover_count()
    x.open_write_Songfile()
    data = x.insertCounts_into_Db()
#    for item in output:
#        print(item)
    x.open_write_file(data)
    x.open_read_file()

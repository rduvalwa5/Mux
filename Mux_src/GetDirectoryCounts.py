'''
Created on Dec 30, 2019

INSERT INTO counts (SERVER, artist, albums, songs) VALUES ('Test', 1, 2,3);
INSERT INTO counts (SERVER, artist, albums, songs) VALUES ('Test2',2 , 0,0);

@author: rduvalwa2
'''
import os, platform
import pymysql

class Get_Directory_Counts_Function:

    def __init__(self):
        
        self.server = ""
        self.artistList = []
        self.albumList = [] 
        self.songList = []
        self.artist = 0
        self.albums = 0
        self .songs = 0
        self.genre = 0
               
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-OSX.home': #'C1246895-osx.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music/"
            self.server = "C1246895-osx.hsd1.wa.comcast.net"
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            self.conn = pymysql.connect(host='OSXAir.hsd1.wa.comcast.net', user='rduvalwa2', password='blu4jazz', db='Music')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            self.server = "OSXAir.hsd1.wa.comcast.net"
        elif platform.uname().node == 'RandyDuvalsMBP.hsd1.wa.comcast.net':
            print("Host is " , 'RandyDuvalsMBP.hsd1.wa.comcast.net')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Media/Music"
            self.server = "RandyDuvalsMBP.hsd1.wa.comcast.net"
            self.conn = pymysql.connect(host='RandyDuvalsMBP.hsd1.wa.comcast.net', user='rduvalwa2', password='blu4jazz', db='Music')            
        else:
            print("Host is not found ")
            exit

    def insertCounts_into_Db(self):
        print("Start Insert Counts into DataBase...")
#        print("Server ",self.server ,"Genre ", self.genre, " artist ", self.artist, " albums ", self.albums, " songs ", self.songs)
        cursor = self.conn.cursor()
        statement = "INSERT INTO counts (SERVER, artist, albums, songs) VALUES ('" + self.server + "'," +  str(self.artist) + "," + str(self.albums) + "," + str(self.songs) + ");" 
        try:
            print("Statement ", statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
        except self.conn.Error as err:
            print("Exception is ", err)
        cursor.close()
        
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

    def get_artist_count(self):
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
 #               print(directory)
                self.artist = self.artist + 1
                self.artistList.append(directory)
        print(len(self.artistList))
 
    def get_albums_count(self):
        for a in self.artistList:
            artist = a[1]
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
                for album in artist_albums:
                    if album != '.DS_Store':
                        self.albumList.append(album)
                        self.albums = self.albums + 1

#        print("albums count ", self.albums)
#        print("albumList size ", len(self.albumList))

    def get_song_count(self):
        for a in self.artistList:
            artist = a
#            print(self.base + "/" + artist)
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
                for al in artist_albums:
#                        print("al is ",al)
                        albumSongs = os.listdir(self.base + "/" + artist + "/" + al)
#                        print("Al Song ", albumSongs)
                        self.songs = self.songs + len(albumSongs)
#        print("Total songs ", self.songs)                


if __name__ == '__main__':
    x = Get_Directory_Counts_Function()
    x.get_genre_count()
    x.get_artist_count()
    x.get_albums_count()
    x.get_song_count()
    x.insertCounts_into_Db()

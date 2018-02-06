'''
Created on Feb 3, 2018

@author: rduvalwa2
'''
import MySQLdb
import os, platform

class Set_Artist_Albums_Genre_Type:

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
            self.conn  = MySQLdb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test
        self.AlbumList = []
        self.genreList = ['Alternative', 'BlueGrass', 'Blues', 'Classic', 'Country', 'Folk', 'Holiday', \
                            'Jazz', 'Latino', 'Pop', 'Regae', 'Rock', 'RockaBilly', 'Soul', 'Talk', \
                            'TestGenre', 'TexMex', 'Traditional', 'World']
        
    def get_artist_genre_from_songs(self):
        statement = "select distinct artist, genre from `Music`.`album2songs`;"
        cursor = self.conn.cursor()
        cursor.execute(statement)
        self.AlbumList = cursor.fetchall()
        
    def set_genre_artist(self):
        cursor = self.conn.cursor()
        for album in self.AlbumList:
            statement = "update `derived_artist` set genre = '" + album[1] + "' where artist like \"" + album[0] + "\";"
#            statement = "update `temp_albums` set genre = '" + album[1] + "' where album like \"" + album[0] + "\";"
            print(statement)
            cursor.execute(statement)
        cursor.execute("commit;")
       
if __name__ == '__main__':
    x = Set_Artist_Albums_Genre_Type()    
    x.get_artist_genre_from_songs()
    x.set_genre_artist()
#    for item in x.AlbumList:
#        print(item[0],item[1])
    
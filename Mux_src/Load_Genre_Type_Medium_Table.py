'''
Created on Aug 1, 2022

@author: rduvalwa2
'''
import pymysql
import os, platform
from Mux_src.Mux_Parameters import *

class Load_Genre_Type_Medium_Functions:
        
    def __init__(self):
        if platform.uname().node == 'Macbook16.local':
            self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
            self.server = 'MaxBook16' 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
            self.db = 'Music_Test'
        else:
            print("Server not found")
#        print("*************** Node Name is ", platform.uname().node)
#        self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music_2')
#        self.parameters = Mux_Parameters()
#        self.base = "/Users/rduvalwa2/music/music/Media.localized/"
        self.genre = ["Alternatives","Blue Grass","Blues","Classical","Country & Folk","Folk","French Pop","Holiday","International","Jazz","Latin","New Age","Pop","R&B","R&B/Soul","Reggae","Rock","Rockbilly","Singer/Songwriter","Soul","Soundtrack","Southern Rock","TexMex"]

        self.genre = ["Alternatives","Blue Grass","Blues","Classical","Country & Folk","Folk","French Pop","Holiday","International","Jazz","Latin","New Age","Pop","R&B","R&B/Soul","Reggae","Rock","Rockbilly","Singer/Songwriter","Soul","Soundtrack","Southern Rock","TexMex"]
        self.myType = ['Amazon','Audible','CD','Internet','Itunes','Tape','Vinyl']
        self.medium = ['CD','Download','Tape','Vinyl']

    def set_genre_genre(self):
        conn = self.conn
        genre = self.genre
        print("Start set_genre")
        print(genre)
        cursor = conn.cursor()
        truncate = "truncate " + self.db + ".genre;" 
        cursor.execute(truncate)
        for gen in genre:
            statement = "insert into " + self.db + ".genre set genre = '" + gen + "';"
            print(statement)
            print(self.does_genre_exist(gen))
            if self.does_genre_exist(gen):
                print(gen , " already exist!")
            else:
                try:
                    print(statement)
                    cursor.execute(statement)
                    print("Success " + gen)
                    cursor.execute("commit;")
                except self.conn.Error as err:
                    print("Exception is ", err)
            conn.close
        print("done")

    def does_genre_exist(self, genre):
        conn = self.conn
        cursor = conn.cursor()
        statement = "select g.g_idx from "+ self.db + ".genre g where genre like '" + genre + "';"
        cursor.execute(statement)
        result = cursor.fetchone()
        if result != None:
            print(result)
            return True
        else:
            return False
            
        cursor.close()
 
    def set_medium(self):
        conn = self.conn
        medium = self.medium
        print("Start set_medium")
        print(medium)
        cursor = conn.cursor()
        truncate = "truncate " + self.db  + ".medium;" 
        cursor.execute(truncate)
        for medium in medium:
            statement = "insert into " + self.db  + ".medium set medium = '" + medium + "';"
            print(statement)
            print(self.does_medium_exist(medium))
            if self.does_genre_exist(medium):
                print(medium , " already exist!")
            else:
                try:
                    print(statement)
                    cursor.execute(statement)
                    print("Success " + medium)
                    cursor.execute("commit;")
                except self.conn.Error as err:
                    print("Exception is ", err)
            conn.close
        print("done")
        
    def does_medium_exist(self,medium):
        conn = self.conn
        cursor = conn.cursor()
        statement = "select medium from " + self.db  + ".medium  where medium like '" + medium + "';"
        cursor.execute(statement)
        result = cursor.fetchone()
        if result != None:
            print(result)
            return True
        else:
            return False
        cursor.close()
        
    def set_type(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
#        conn = self.conn
        myType = self.myType
        print("Start set_type")
        print(myType)
        cursor = self.conn.cursor()
        truncate = "truncate " + self.db  + ".type;" 
        cursor.execute(truncate)
        for typ in myType:
            statement = "insert into " + self.db  + ".type set type = '" + typ + "';"
            print(statement)
            print("does_type_exist")
            if self.does_type_exist(typ):
                print(typ , " already exist!")
            else:
                try:
                    print(statement)
                    cursor.execute(statement)
                    print("Success " + typ)
                    cursor.execute("commit;")
                except self.conn.Error as err:
                    print("Exception is ", err)
            self.conn.close
        print("done")
        
    def does_type_exist(self,typ):
        self.conn = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music_Test')
        cursor = self.conn.cursor()
        statement = "select type from " + self.db  + ".type  where type like '" + typ + "';"
        cursor.execute(statement)
        result = cursor.fetchone()
        if result != None:
            print(result)
            return True
        else:
            return False
            
        cursor.close()
        
    
        
if __name__ == '__main__':
        mux = Load_Genre_Type_Medium_Functions()
        mux.set_genre_genre()
        mux.set_medium()
        mux.set_type()

#    loadAlbums = Load_Genre_Type_Medium_Functions()
#    loadAlbums.set_genre_genre()
#    loadAlbums.set_medium()
#    loadAlbums.set_type()
#    loadAlbums.get_music_artist()
#    loadAlbums.initial_insert_into_ArtistAlbums()

#    loadAlbums.get_music_artist()
#    loadAlbums.load_Artist_Table()   



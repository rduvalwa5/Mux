'''
Created on Apr 22, 2017

@author: rduvalwa2
update `Music`.album2songs INNER JOIN  `Music`.genre
on album2songs.genre = genre.genre
set `Music`.album2songs.genre_idx = `Music`.genre.g_idx;
'''
import platform
import MySQLdb   as connDb

class Genre_Align_Index:
    def __init__(self, test=False):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-osx.home':
#            self.conn = connDb.Connect(**login_info_osx)
            self.conn = connDb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')

        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn = connDb.connect(host='OSXAir.home', user='rduvalwa2', password='blu4jazz', db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
#            self.conn = connDb.Connect(**login_info_default)
            self.conn = connDb.connect(host='OSXAir.home', user='root', password='blu4jazz', db='Music')
        else:
            self.conn = connDb.connect(host='OSXAir.home', user='rduvalwa2', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test

    def align_genre_index(self):
        statement = "update `Music`.album2songs INNER JOIN  `Music`.genre \
                     on album2songs.genre = genre.genre \
                     set `Music`.album2songs.genre_idx = `Music`.genre.g_idx;"

        cursor = self.conn.cursor()  
        try:          
            cursor.execute(statement)
            return "Genre Index Aligned Successfully"
        except self.conn.Error as err:
                print("Exception is ", err)
                return err

    def get_genre_count_by_name(self):
        cursor = self.conn.cursor()  
        statement = "select a.genre, count(a.genre) \
                        FROM `Music`.album2songs a \
                        group by a.genre \
                        order by count(a.genre) desc;"
        try:          
            cursor.execute(statement)
            resultList = cursor.fetchall()
            return resultList
        except self.conn.Error as err:
                print("Exception is ", err)
                return err                       

    def get_genre_count_by_index(self):
        cursor = self.conn.cursor()  
        statement = "select a.genre_idx, count(a.genre_idx) \
                     FROM `Music`.album2songs a \
                     group by a.genre_idx \
                     order by count(a.genre_idx) desc;"
        try:          
            cursor.execute(statement)
            resultList = cursor.fetchall()
            return resultList
        except self.conn.Error as err:
                print("Exception is ", err)
                return err    
                                       
if __name__ == '__main__':
    alignGenreIdx = Genre_Align_Index(True)
    
    alignGenreIdx.align_genre_index()

    print("\n Count by Name")    
    for item in alignGenreIdx.get_genre_count_by_name():
        print(item)
    print("\n Count by Index")
    for item in alignGenreIdx.get_genre_count_by_index():
        print(item)
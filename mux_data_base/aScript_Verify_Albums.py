'''
Created on Mar 16, 2017

@author: rduvalwa2
'''     

import os, platform
import MySQLdb   as connDb


class verify_albums:
    def __init__(self):       
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


    def verify_albums_match_rock(self,genre):
            cursor = self.conn.cursor()
            statement = "select * from `Music`.artist_albums a where a.genre = '" + genre + "' and a.album NOT IN  (select distinct b.album from `Music`.album2songs b where b.genre = '" + genre + "');"
#            statement = "select a.album from `Music`.artist_albums a where a.genre = '" + genre + "';" 
            try:
                cursor.execute(statement)
                result = cursor.fetchall()  
#                print("Result is ", result)
                cursor.close()

                return result             
            except self.conn.Error as err:
                print("Exception is ", err)
                return str(err)
            self.conn.close()
        
if __name__ == "__main__" :    
    albumVerifyRock = verify_albums()
    genreList = ['Alternative','BlueGrass','Blues','Classic','Country','Folk','Holiday',\
                            'Jazz','Latino','Pop','Regae','Rock','RockaBilly','Soul','Talk', \
                            'TestGenre','TexMex','Traditional','World']
#    print(genreList)
    for gen in genreList:
#        print(gen)
        print(gen, " " , albumVerifyRock.verify_albums_match_rock(gen))
        if len(albumVerifyRock.verify_albums_match_rock(gen)) > 0:
            for album in albumVerifyRock.verify_albums_match_rock(gen):
                print(album)
    

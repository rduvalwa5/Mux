'''
Created on Mar 16, 2017

@author: rduvalwa2
'''     

import os, platform
import MySQLdb   as connDb


class verify_artist:
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


    def verify_artist_match(self):
            cursor = self.conn.cursor()
            statement = "select b.artist, b.`index` from `Music`.artist b \
                         where b.artist NOT IN (select distinct a.artist from `Music`.album2songs a) \
                         order by b.artist asc;"
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
    verifyArtist = verify_artist()
    result = verifyArtist.verify_artist_match()
    for artist in result:
                print(artist)
    

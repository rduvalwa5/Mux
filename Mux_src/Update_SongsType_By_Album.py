'''
Created on Aug 19, 2020

@author: rduvalwa2
'''
import platform
import pymysql.cursors
from Musicdb_info import *
from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            serv = login_info_xps
        elif platform.uname().node == 'C1246895-osx.home':
            serv = login_info_osx
        elif platform.uname().node == 'OSXAir.hsd1.wa.comcast.net':
            serv = login_info_osxAir
        elif platform.uname().node == 'C1246895-WIN64-Air':
            serv = login_info_WIN64_Air
        elif platform.uname().node == 'Randalls-MBP.home':
            serv = login_info_default
        else:
            print("Host is " , 'default')
            serv = login_info_default
            
        host = serv['host']
        user = serv['user']
        password = serv['password']
        db = "music"
        conn = pymysql.connect(host=host, user=user, password=password, db=db)
        base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        server = 'OSXAir' 
      
        m = musicGet_Functions(True)
        
        statement = "select album from music.artist_albums order by artist_albums.album;"
        print(statement)
        cursor = conn.cursor()
        try:
            cursor.execute(statement)
            allAlbums = cursor.fetchall()  
            cursor.close()
        except conn.Error as err:
            print("Exception is ", err)
        print(allAlbums)
        cursor = conn.cursor()
        for al in allAlbums:
            album = list(al)
            print(album[0].strip('\''))
            thisAl = album[0].strip('\'')
            genreStatement = "select type from music.artist_albums where album like \"" + thisAl + "\";"
            print(genreStatement)
            cursor.execute(genreStatement)
            gen = cursor.fetchone()
            print(gen)
            ge = str(gen)
            g = ge.strip('(),')
            print(g)
            updateStatement = "update music.album2songs set type = " + g + " where album like '"+thisAl+"';"
            print(updateStatement)

            try:
                result = cursor.execute(updateStatement)
                print(result)
            except conn.Error as err:
                print("Exception is ", err)
        cursor.execute("commit;")
        cursor.close()


    
    
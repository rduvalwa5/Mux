import platform
import MySQLdb   as connDb


class musicLoad_Functions:
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
        
    def build_normal_song_table(self):   
        statement_get = "select distinct sng.`index`, sng.song,  art.`index`, alb.`index` \
                    from `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb \
                    where sng.album = alb.album  \
                    and sng.artist = art.artist \
                    order by sng.`index`;"
        cursor = self.conn.cursor()
        cursor.execute(statement_get)
        songs = cursor.fetchall()
        for song in songs:
#            print(song)
            insertStatement = "INSERT into Music.normal_song (song, song_idx,artist_idx, album_idx)  values( " + "\"" +  song[1] + "\"," + str(song[0]) + "," + str(song[2]) + "," + str(song[3]) + ");"
#            print(insertStatement)
            try:
                if self.notTestRun:
                    cursor.execute(insertStatement)
            except self.conn.Error as err:
                print("Insert Exception is ", song,  err)
#            return str(err)
        if self.notTestRun:
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()
                
    def truncate_normal_table(self):
        cursor = self.conn.cursor()
        trunkate = "truncate  music.normal_song;"
        cursor.execute(trunkate)

    def get_count(self,table = 'music.normal_song', criteria = " "):
        statement = "select count(*) from " + table + " "  + criteria + ";"
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            count = cursor.fetchone()  
            theCount = count[0]
            cursor.close()
#            self.dbConnectionClose()
            return theCount       
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)
        
        
if __name__ == '__main__':
    idx = musicLoad_Functions(True)
    idx.truncate_normal_table()
    idx.build_normal_song_table()
    count = idx.get_count()
    print("normal table",count)
    album2songs = idx.get_count("music.album2songs")
    print("album2song count ", album2songs)
    
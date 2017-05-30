import os, platform
import MySQLdb   as connDb


class albumCoverLoad:
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
        self.album_covers = []    
        self.base = "/Users/rduvalwa2/git/Mux/AlbumCovers"
    
    def get_album_covers(self):
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music
        print(self.base)
#        album_covers = []
        index = 0
        covers = os.listdir(self.base)
        for cover in covers:
            if cover != '.DS_Store':
                self.album_covers.append((index,cover))
                index = index + 1

    def initial_insert_into_album_covers(self): 
        cursor = self.conn.cursor()
        trunkate = "truncate   `Music`.`album_covers`;"
        cursor.execute(trunkate)
        for cover in self.album_covers:
                insertStatement = "INSERT into  `Music`.`album_covers` (cover_idx,album_cover,description,album_idx) \
                                    values(" + str(cover[0]) + ",\"" + cover[1] + "\",'' ,'');"
                print(insertStatement)
                cursor.execute( insertStatement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()

    def verify_albumCover_count(self):
        cursor = self.conn.cursor()
        statement = "select count(*) from `Music`.`album_covers`;"
        cursor.execute(statement)
        result = cursor.fetchone()
        return result[0]
             
if __name__  == '__main__':
    cov = albumCoverLoad()
    cov.get_album_covers()
    for cover in cov.album_covers:
        print(cover)
        
    cov.initial_insert_into_album_covers()
    print(cov.verify_albumCover_count())
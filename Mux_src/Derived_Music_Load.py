import os, platform
import MySQLdb
from Musicdb_info import login_info_default, login_info_osxAir, login_info_xps, login_info_WIN64_Air, login_info_osx


class derived_musicLoad_Functions:

    def __init__(self, isNotTest):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            serv = login_info_xps
        elif platform.uname().node == 'C1246895-osx.home':
            serv = login_info_osx
        elif platform.uname().node == 'OSXAir.home.home':
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
        db = serv['db']
        self.conn = MySQLdb.connect(host=host, user=user, password=password, db=db)
        
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home.home' 
        self.notTestRun = isNotTest
        
        self.countryArtistList = ["Dolly Parton","Alabama","Alison Krauss","Alison Krauss & Brad Paisley","Alison Krauss & John Waite","Alison Krauss & Union Station","Bill Monroe","Boxcar Willie","Brenda Lee","Chanel Campbell","The Charlie Daniels Band","Charlie Rich","Chet Atkins and Hank Snow","Cody Bryant and The Riders Of The Purple Sage","Colt Ford","David Allan Coe","Della Mae","Dierks Bentley","Dixie Chicks","Eilen Jewell","Eldorado","Emmylou Harris","Emmylou Harris with Herb Pedersen","Emmylou Harris with Roy Orbison","Florida Georgia Line","Foy Willing & The Riders Of The Purple Sage","Gram Parsons","Hank Williams, Jr.","Jack Ingram","James Otto","Jamey Johnson","Jerry Jeff Walker","Jessi Colter","Jessi Colter & Sunny Sweeney","Jewel","Jimmy Buffet","John Hiatt","Johnny Cash","Josh Thompson","Justin Moore","Keith Urban ","Kenny Rogers & The First Edition","Kris Kristofferson","Kris Kristofferson & Patty Griffin","Linda Ronstadt","Lori McKenna","Mark O'Connor","The Marshall Tucker Band","Marty Robbins","The Mavericks","Michael Martin Murphey","Montgomery Gentry","New Riders of the Purple Sage","Nitty Gritty Dirt Band","Olivia Newton-John","Pat Green","Patsy Cline","Polecat","Prairie Flyer","Randy Houser","Redbird","Robert Plant & Alison Krauss","Shooter Jennings","Stray Birds","The Texas Tornados","Texas Tornados","Trace Adkins","Uncle Earl","Van Morrison","Waylon and Willie","Waylon Jennings","Waylon Jennings & The Waylors","Waylon Jennings & Willie Nelson","Willie Nelson and Leon Russel","Wyatt McCubbin","Zac Brown Band"]
        self.popArtistList = ["Yo-Yo Ma","Sarah McLachlan","Reflejo de Luna","Nat _King_ Cole","Celtic Christmas","Bing Crosby","Armik","Tony Bennett","Ottmar Liebert%","Noam Chomsky","Philip Selway","Padraig MacMathuna","Ottmar Liebert_Luna Negra","Ottmar Liebert","Mannheim Steamroller","Loreena McKennitt","Julio Iglesias","ADELE","The Airborne Toxic Event","Alexander","Arcade Fire","Art Garfunkel","The Coats","Cold War Kids","Dean Martin","Death Cab for Cutie","Del Shannon","Diego Garcia","Frank Sinatra","Frank Sinatra & Dean Martin","Frank Sinatra & Sammy Davis Jr.","Frank Sinatra, Dean Martin & Sammy Davis Jr.","Generationals","George Baker & George Baker Selection","Harry Nilsson","Iron & Wine","Jackson Browne","Jeremy Camp","Jesse Thomas","Jose Feliciano","Judy Collins","Junip","k.d. lang and the Siss Boom Bang","Leo Sayer","Lesley Gore","The Mamas & The Papas","Nashville Teens","Neil Diamond","Neil Sedaka","Norah Jones","Parts & Labor","Paul Simon","Percy Sledge","Peter Bjorn and John","Playing for Change","Rita Coolidge","S. Carey","Sammy Davis Jr.","Sammy Davis Jr. & Dean Martin","Sarah Jarosz","Say Hi","The Shadows","Telekinesis","The Tokens","Tom Jones","Tom Jones, Johnnie Spence & Orchestra","We Are Augustines","Wrabel","Wye Oak"]
        self.jazzArtistList = ["Walt Weiskopf Nonet","Pat Metheny Trio","Alex Hargreaves","Branford Marsalis","Brecker Brothers","Buddy Tate","Chick Corea","Darius Brubeck","Dave Brubeck Quartet",'%Dave Brubeck%' ,"Devin Duval","Duke Ellington","Eddie Lockjaw Davis","Fats Waller","Gary Burton, Steve Swallow, Roy Haynes, Tiger Okoshi","Grant Green","Hank Jones","Herbie Hancock","Ian Hunter","Jaco Pastorius","Jaco Pastorius With Herbie Hancock","The Jazz Crusaders","Jerry Gonzalez & The Fort Apache Band","Jimmy Witherspoon","Joe Henderson","John Coltrane","John Coltrane & Johnny Hartman","John Scofield","Keith Jarrett","Les McCann","Less McCann and Eddie Harris","Lester Young","Madeleine Peyroux","Mary Pastorius","Mass Mental","Michael Brecker","Miles Davis","Miles Davis Quintet","Miles Davis Sextet_Sonny Rollins","Miles Davis_Sonny Rollins","Oscar Peterson","The Overton Berry Trio","Pat Martino","Pat Metheny","Pat Metheny Group","The Quintet","Rodrigo Y Gabriela","Sonny Rollins","Sonny Stitt","Stanley Turrentine","Tech N9ne","The Jazz Crusaders","Thelonious Monk","Thelonious Monk Quartet With John Coltrane","Tony Burgos & His Swing Shift Orchestra","Various Artists","Walt Weiskopf","Weather Report"]
        self.bluegrassArtistList = ["The Chieftains","Crooked Still","Infamous Stringdusters","Mountain Heart","Sarah Jarosz","Tim O'Brien","Uncle Earl","Walela"]
        self.folkArtistList = ["The Kingston Trio","Peter Paul and Mary","Pete Segear Arlo Guthrie","Arlo Guthrie","Barry McGuire","Bee Gees","Bob Dylan","Cat Stevens","Gordon Lightfoot","The Handsome Family","Harry Belafonte","Joan Baez","John Fahey","John Fahey & His Orchestra","John Prine","Joni Mitchell","Josh Rouse","Judy Collins","Kingston Trio","Leo Kottke","Mark Lanegan","Pete Seeger & Arlo Guthrie","Peter, Paul & Mary","Richie Havens","Rodriguez","Steve Goodman","The Wailin' Jennys"]
        self.bluesArtistList = ["Alvin Lee & Ten Years Later","Mavis Staples","Alvin Lee","Alvin Lee & Richard Newman","Alvin Lee, Richard Newman & Tim Hinkley","Billy Holliday","Blues Artists","Bob Forrest","The Box Tops","Boz Scaggs","Clarence Gatermouth Brown","Cream","Eric Clapton","Eric Clapton & B.B. King","Gregg Allman","Hot Tuna","Jimmy Witherspoon","Joe Louis Walker","John Lee Hooker","John Mayall","John Mayall & The Bluesbreakers","Johnny Winter","Muddy Waters","North Mississippi Allstars","The Paul Butterfield Blues Band","R.L. Burnside","Richie Havens","Savoy Brown","Stevie Ray Vaughan","Stevie Ray Vaughan & Double Trouble","Ten Years After","War","Wynton Marsalis & Eric Clapton","The Yardbirds","18 South"]
        self.classicalArtistList = ["Andre Kostelanetz and his orchestra",'Charles Dutoit%','Alfred Hause%','Angele Dubeau%',"Antonio Vivaldi","Branford Marsalis","Branford Marsalis & Orpheus Chamber Orchestra","Dvorak","A Fielder Boston Pops","Mark O'Connor","Oliver Kane","Ravel","Richard Wagner","Wagner"]
        self.TexMex = ['Asleep At the Wheel','Santana','Los Lobos','Freddy Fender','Texas Tornados','The Mavericks','Eldorado','Sir Douglas Quintet']
        self.RockABilly = ['Buddy Holly','Carl Perkins','Jerry Lee Lewis','Bill Haley & His Comets','Dale Hawkins','Billy Lee Riley']
        self.Soul = ['Marvin Gaye','Mavis Staples','Roberta Flack & Donny Hathaway','Aretha Franklin','Roberta Flack']
        self.Regae = ['Desmond Dekker','Bob Marley & The Wailers','Freddie Notes & the Rudies','Bob Marley']

    
    def get_genre_album2songs(self):
        pass
        
    def get_genre_genre(self):
        pass
    
    def set_genre_genre(self, genre):
        print("Start set_genre")
        print(genre)
        cursor = self.conn.cursor()
        for gen in genre:
            statement = "insert into `Music`.genre set genre = '" + gen + "';"
            print(self.does_genre_exist(gen))
            if self.does_genre_exist(gen):
                print(gen , " already exist!")
            else:
                try:
                    print(statement)
                    cursor.execute(statement)
                    print("Success " + gen)
                    cursor.execute("commit;")
                except self.conn.Error.Error as err:
                    print("Exception is ", err)

        cursor.close()
        print("done")

    def does_genre_exist(self, genre):
        cursor = self.conn.cursor()
        statement = "select g.g_idx from `Music`.genre g where genre like '" + genre + "';"
        cursor.execute(statement)
        result = cursor.fetchone()
        if result != None:
            print(result)
            return True
        else:
            return False
            
        cursor.close()
    
    def get_albums(self):
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        index = 0
        artists = self.get_music_artist()
        for a in artists:
            artist = a[1]
            if os.path.isdir(self.base + "/" + artist):
                artist_albums = os.listdir(self.base + "/" + artist)
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((index, artist, album))
                        index = index + 1
        return albums

    def get_music_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index, directory))
                index = index + 1
        return artist

    def get_all_songs(self):
        index = 0
#        base =   "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        albums = []
        songs = []
        artist = self.get_music_artist()
        for a in artist:
            if os.path.isdir(self.base + "/" + a[1]):
                artist_albums = os.listdir(self.base + "/" + a[1])
                for album in artist_albums:
                    if album != '.DS_Store':
                        albums.append((a, album))
                        album_songs = os.listdir(self.base + "/" + a[1] + "/" + album)
                        for song in album_songs:
                            if song != '.DS_Store' and song != 'side1.mp3' and song != 'side2.mp3' and song != 'side3.mp3' and song != 'side4.mp3':
                                songs.append((index, a[1], album, song))
                                index = index + 1
        return songs

    def initial_insert_into_artist(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        trunkate = "truncate  music.derived_artist;"
        cursor.execute(trunkate)
        allArtist = self.get_music_artist()
        if self.notTestRun:
            for artist in allArtist:
                insertStatement = "INSERT into Music.derived_artist (derived_artist.index, derived_artist.artist,derived_artist.genre)  values(" + str(artist[0]) + ",\"" + artist[1] + "\",\"" + "Rock" + "\")"
                cursor.execute(insertStatement)
            countStatement = "SELECT count(*) FROM music.derived_artist;"        
            cursor.execute(countStatement)
            count = cursor.fetchone()
#            print(count[0])
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()

    """
    Initial Load functions
    """

    def initial_insert_into_artistAlbums(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        trunkate = "truncate  music.derived_artist_albums;"
        cursor.execute(trunkate)
        allAbums = self.get_albums()
        if self.notTestRun:
            for album in allAbums:
                insertStatement = "INSERT into Music.derived_artist_albums (derived_artist_albums.index, derived_artist_albums.artist,derived_artist_albums.album,derived_artist_albums.genre,derived_artist_albums.type)  values(" + str(album[0]) + ",\"" + album[1] + "\",\"" + album[2] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
                cursor.execute(insertStatement)
            countStatement = "SELECT count(*) FROM music.derived_artist_albums;"        
            cursor.execute(countStatement)
            count = cursor.fetchone()
#        print(count[0])
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()

    def initial_insert_into_album2songs(self): 
        '''
        This code recurses thru the "base" path and captures the artist, album and song
        '''
        cursor = self.conn.cursor()
        allSongs = self.get_all_songs()
        if self.notTestRun:
            trunkate = "truncate  music.derived_album2songs;"
            cursor.execute(trunkate)
            for song in allSongs:
                insertStatement = "INSERT into Music.derived_album2songs (derived_album2songs.index, derived_album2songs.server,derived_album2songs.path,derived_album2songs.artist,derived_album2songs.album,derived_album2songs.song,derived_album2songs.genre,derived_album2songs.type)  values(" + str(song[0]) + ",\"" + self.server + "\",\"" + self.base + "\",\"" + song[1] + "\",\"" + song[2] + "\",\"" + song[3] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
                print(insertStatement)
                cursor.execute(insertStatement)
            countStatement = "SELECT count(*) FROM music.derived_album2songs;"        
            cursor.execute(countStatement)
            count = cursor.fetchone()
            print(count)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        else:
            for song in allSongs:
                insertStatement = "INSERT into Music.derived_album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(song[0]) + ",\"" + self.server + "\",\"" + self.base + "\",\"" + song[1] + "\",\"" + song[2] + "\",\"" + song[3] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
#                print(insertStatement)

        cursor.close()
        
    def sync_song_type(self):
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.derived_album2songs t1 INNER JOIN `Music`.derived_artist_albums t2 ON t1.album = t2.album SET t1.type = t2.type;"
        if not self.notTestRun:
            print(statement)
        if self.notTestRun:
            statement = "UPDATE `Music`.derived_album2songs t1 INNER JOIN `Music`.derived_artist_albums t2 ON t1.album = t2.album SET t1.type = t2.type;"
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()       

    def sync_song_genre(self): 
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.derived_album2songs t1 INNER JOIN `Music`.derived_artist_albums t2 ON t1.album = t2.album SET t1.genre = t2.genre;"
        if not self.notTestRun:
            print(statement)
        if self.notTestRun:
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()              

class song_Add_Update_Delete():       

    def __init__(self, test=False):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home':
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test 
        
    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table + ";"
        cursor = self.conn.cursor()
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
    
    def get_songs(self, artist, album='all'):
        base = self.base
        albums = []
        songs = []
        newIndex = 0
        if os.path.isdir(base + "/" + artist):
                artist_albums = os.listdir(base + "/" + artist)
#                print("artist_albums: ", artist_albums)
                if album == 'all':
                    for al in artist_albums:
                        if al != '.DS_Store':
                            albums.append((artist, al))
                            album_songs = os.listdir(base + "/" + artist + "/" + al)
                            for song in album_songs:
                                    songs.append((newIndex, artist, al, song))
                elif  album != 'all':
                    for al in artist_albums:
                        if al == album:
                            if al != '.DS_Store':
                                albums.append((artist, al))
                                album_songs = os.listdir(base + "/" + artist + "/" + al)
                                for song in album_songs:
                                    songs.append((newIndex, artist, al, song))
                return songs

    def add_songs(self, artist, album='all'):
        cursor = self.conn.cursor()
        maxIndex = self.get_max_index("album2songs")
        index = maxIndex[0]
        newIndex = index + 1
#        print(newIndex)
        if album == 'all': 
            songs = self.get_songs(artist)
        else:
            songs = self.get_songs(artist, album)
#        print(songs)
        if self.notTestRun:
            for song in songs:
                print(song[3])
                if song[3] != ".DS_Store":
                    insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + self.server + "\",\"" + self.base + "\",\"" + song[1] + "\",\"" + song[2] + "\",\"" + song[3] + "\",\"" + "rock" + "\",\"" + "download" + "\")"
#                    print(insertStatement)
                    cursor.execute(insertStatement)
                    newIndex = newIndex + 1
            countStatement = "SELECT count(*) FROM music.album2songs;"        
            cursor.execute(countStatement)
#            count = cursor.fetchone()
#            print(count)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()

    def add_song(self, album, artist, genre, song, type, path='/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', server='OSXAir.home'):
 
        cursor = self.conn.cursor()
        maxIndex = self.get_max_index("album2songs")
        index = maxIndex[0]
        newIndex = index + 1
        insertStatement = "INSERT into Music.album2songs (album2songs.index, album2songs.server,album2songs.path,album2songs.artist,album2songs.album,album2songs.song,album2songs.genre,album2songs.type)  values(" + str(newIndex) + ",\"" + server + "\",\"" + path + "\",\"" + artist + "\",\"" + album + "\",\"" + song + "\",\"" + genre + "\",\"" + type + "\")"
        print(insertStatement)
        if self.notTestRun:
            cursor.execute(insertStatement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()
        return newIndex
        
    def update_song_album(self, album, song):

        cursor = self.conn.cursor()
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs SET album = '" + album + "' WHERE song = '" + song + "';"
            print(statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()   
  #      xconn.close()
         
    def update_song_artist(self, artist, song):
        cursor = self.conn.cursor()
        statement = "UPDATE `Music`.album2songs SET artist = '" + artist + "' WHERE song like '" + song + "';"
        print(statement)

        if self.notTestRun:
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()    
  
    def update_songs_artists(self, songs):

        artistSongs = songs  
        for item in artistSongs:
            cursor = self.conn.cursor()
            statement = "UPDATE `Music`.album2songs SET artist = '" + item[1] + "' WHERE song like '" + item[0] + "';"
            print(statement)
            if self.notTestRun:
                cursor.execute(statement)
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()      
    
    def update_song_genre(self, genre, song):

        cursor = self.conn.cursor()
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs SET genre = '" + genre + "' WHERE song = '" + song + "';"
            print(statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()    
    
    def update_song_type(self, tipe, song):

        cursor = self.conn.cursor()
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs SET type = '" + tipe + "' WHERE song = '" + song + "';"
            print(statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()    
    
    def update_song_path(self, path, song):
 
        cursor = self.conn.cursor()
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs SET path = '" + path + "' WHERE song = '" + song + "';"
            print(statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()    

    def update_song_server(self, server, song):

        cursor = self.conn.cursor()
        if self.notTestRun:
            statement = "UPDATE `Music`.album2songs SET server = '" + server + "' WHERE song = '" + song + "';"
            print(statement)
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()   
  
    def delete_song(self, idx):

        if self.notTestRun:
            statement = "delete  from `Music`.album2songs where `index` = " + str(idx) + ";"
            print(statement)
            cursor = self.conn.cursor()
            cursor.execute(statement)
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()
    
    def delete_songs(self, artist, albumin='all', songin="all"):
        cursor = self.conn.cursor()   
        delete_songs = self.get_songs(artist, albumin)
#        print("delete songs: ", delete_songs)  
        index = 0
        if albumin == 'all':
            if songin == 'all':   
                for song in delete_songs:
                    if self.notTestRun:
                        selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                        print(selectStatement)
                        cursor.execute(selectStatement)
                        row = cursor.fetchone()
                        index = row[0]  
#                        print("delete index: ", index)         
                        deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                        print(deleteStatement)
                        cursor.execute(deleteStatement)
            else:
                for song in delete_songs:  
                    if song[0] == 'songin':
                        if self.notTestRun:
                            selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                            print(selectStatement)
                            cursor.execute(selectStatement)
                            row = cursor.fetchone()
                            index = row[0]           
                            deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                            print(deleteStatement)
                            cursor.execute(deleteStatement)        
        else:
            if albumin != 'all': 
                if songin == 'all':  
                    for song in delete_songs:
                        if albumin == song[2]: 
                            if self.notTestRun:
                                selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                                print(selectStatement)
                                cursor.execute(selectStatement)
                                row = cursor.fetchone()
                                index = row[0]                      
                                deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                                print(deleteStatement)
                                cursor.execute(deleteStatement)
            elif songin != 'all':
                    for song in delete_songs:
                        if albumin == song[2]:                                
                            if song[0] == 'song': 
                                if self.notTestRun:
                                    selectStatement = "select album2songs.index from Music.album2songs where album2songs.song like " + "'" + song[3] + "';"
                                    print(selectStatement)
                                    cursor.execute(selectStatement)
                                    row = cursor.fetchone()
                                    index = row[0]           
                                    deleteStatement = "Delete from `Music`.album2songs where `Music`.album2songs.index = " + str(index) + ";"  
                                    print(deleteStatement)
                                    cursor.execute(deleteStatement)        
        commit = "commit;"
        cursor.execute(commit)
        print("done")
        cursor.close()

    def dbConnectionClose(self):
        self.conn.close()


class album_Add_Update_Delete:       
    def __init__(self, test=False):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
            self.conn  = MySQLdb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test 

    def dbConnectionClose(self):
        self.conn.close()
        
    def doesAlbumExist(self, album):
        cursor = self.conn.cursor()
        selectStatement = "Select Music.artist_albums.index from Music.artist_albums where Music.artist_albums.album like '" + album + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        print("aritstIndex issss ", aritstIndex)
        if aritstIndex == None:
            returnCode = 'False'
        else:
            returnCode = 'True'
        return returnCode

    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table + ";"
        cursor = self.conn.cursor()
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
    
    def add_album(self, album, artist, tipe, gen):
        if self.doesAlbumExist(album) == 'False':
            cursor = self.conn.cursor()
            maxIndex = self.get_max_index("artist_albums")
            index = maxIndex[0]
            newIndex = index + 1
            if self.notTestRun:
                insertStatement = "INSERT into `Music`.`artist_albums` (`artist_albums`.index, `artist_albums`.artist,`artist_albums`.album,`artist_albums`.type,`artist_albums`.genre)  values(" + str(newIndex) + ",\"" + artist + "\",\"" + album + "\",\"" + tipe + "\",\"" + gen + "\" )"
                print(insertStatement)
                cursor.execute(insertStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")
            self.conn.close()
            return "Success " + album
        else:
            print(album, "Already exist in table.")
            return "Already exist in table."

    def update_album(self, album, artist='no_change', genre='no_change', tipe='no_change'):
        cursor = self.conn.cursor()
        if self.doesAlbumExist(album) == 'True': 
            if artist != 'no_change':
                if self.notTestRun:
                    updateStatement = "UPDATE Music.artist_albums set artist = '" + artist + "' where album = '" + album + "';"
                    if genre != 'no_change':
                            updateStatement = "UPDATE Music.artist_albums set artist = '" + artist + "', genre = '" + genre + "' where album = '" + album + "';"
                            if tipe != 'no_change':
                                updateStatement = "UPDATE Music.artist_albums set artist = '" + artist + "', genre = '" + genre + "' ,type = '" + tipe + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and  genre != 'no_change':
                if self.notTestRun:
                    if tipe != 'no_change':
                        updateStatement = "UPDATE Music.artist_albums set genre = '" + genre + "', type = '" + tipe + "' where album = '" + album + "';"
                    else:
                        updateStatement = "UPDATE Music.artist_albums set genre = '" + genre + "' where album = '" + album + "';"
                    print(updateStatement)
                    cursor.execute(updateStatement)
                    commit = "commit;"
                    cursor.execute(commit)
            elif artist == 'no_change' and genre == 'no_change':
                if self.notTestRun:
                    if tipe != 'no_change':
                                updateStatement = "UPDATE Music.artist_albums set type = '" + tipe + "' where album = '" + album + "';"
                                print(updateStatement)
                                cursor.execute(updateStatement)
                                commit = "commit;"
                                cursor.execute(commit)
                    else:
                        print("no updates ", artist , genre, tipe)    
            else:
                print("no updates ", artist , genre, tipe)    
        else:
            print(artist, " does not exist in data table Music.artist_albums.")            
        print("done")
        cursor.close()

    def delete_album(self, album):
        cursor = self.conn.cursor()
        if self.notTestRun:
            selectStatement = "select artist_albums.index from Music.artist_albums where artist_albums.album like " + "'" + album + "';"
            print(selectStatement)
            cursor.execute(selectStatement)
            try:
                row = cursor.fetchone()
                index = row[0]
                deleteStatement = "Delete from `Music`.artist_albums where `Music`.artist_albums.index = " + str(index) + ";"       
                print(deleteStatement)
                cursor.execute(deleteStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")
                cursor.close()
                return "Success"
            except TypeError:
                print("Album not found")
                return "Album not found"

class artist_Add_Update_Delete:       

    def __init__(self, test=False):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'C1246895-XPS':
            self.conn = MySQLdb.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
        elif platform.uname().node == 'C1246895-osx.home.home':
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
        elif platform.uname().node == 'OSXAir.home.home':
#            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
        elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
            self.conn = MySQLdb.connect(login_info_WIN64_Air)
        elif platform.uname().node == 'Randalls-MBP.home':
            print("Host is " , 'Randalls-MBP.home')
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')            
        else:
            print("Host is " , 'default')
            self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')
        self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
        self.server = 'OSXAir.home' 
        self.notTestRun = test  

    def dbConnectionClose(self):
        self.conn.close()

    def doesArtistExist(self, artist):
        cursor = self.conn.cursor()
        selectStatement = "Select  Music.artist.index from Music.artist where  Music.artist.artist = '" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        aritstIndex = cursor.fetchone()
        if aritstIndex != None:
            returnCode = 'True'
        else:
            returnCode = 'False'
        return returnCode

    def get_max_index(self, table):
        self.table = '`Music`.' + table
        self.tableIndex = table + "." + 'Index'
        max_index_statement = "select max(" + self.tableIndex + ") from " + self.table + ";"
        cursor = self.conn.cursor()
        cursor.execute(max_index_statement)
        maxIndex = cursor.fetchone()
        return maxIndex
                    
    def add_artist(self, artist, genre):
        if self.doesArtistExist(artist) == 'False':
            cursor = self.conn.cursor()
            maxIndex = self.get_max_index("artist")
            index = maxIndex[0]
            newIndex = index + 1
            if self.notTestRun:
                insertStatement = "INSERT into Music.artist (artist.index, artist.artist,artist.genre)  values(" + str(newIndex) + ",\"" + artist + "\",\"" + genre + "\")"
                print(insertStatement)
                cursor.execute(insertStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")
            cursor.close()
            return "Success " + artist
        else:
            print(artist, " already exist in data table Music.artist.")
            return "artist already exist in table"

    def update_artist(self, artist, genre):

        cursor = self.conn.cursor()
        if self.doesArtistExist(artist) == 'True':
            if self.notTestRun:            
                updateStatement = "UPDATE Music.artist set genre = '" + genre + "' where artist = '" + artist + "';"
                print(updateStatement)
                cursor.execute(updateStatement)
                commit = "commit;"
                cursor.execute(commit)
                print("done")            
        else:
            print(artist, " does not exist in data table Music.artist.")
        cursor.close()

    def delete_artist(self, artist):
        cursor = self.conn.cursor()
        selectStatement = "select artist.index from Music.artist where artist.artist like " + "'" + artist + "';"
        print(selectStatement)
        cursor.execute(selectStatement)
        row = cursor.fetchone()
        print("Row is ", row)
        index = row[0]
        print(index)
        if self.notTestRun:
            deleteStatement = "Delete from `Music`.artist where `Music`.artist.index = " + str(index) + ";"       
            print(deleteStatement)
            cursor.execute(deleteStatement) 
            commit = "commit;"
            cursor.execute(commit)
            print("done")
        cursor.close()


class verify_data_tables:

        def __init__(self, test=True):
            if platform.uname().node == 'C1246895-XPS':
                self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')
#            self.conn  = c.connect(login_info_xps)
            elif platform.uname().node == 'C1246895-osx.home':
                self.conn = MySQLdb.connect(host='OSXAir.home', user='rduvalwa2', password='blu4jazz', db='Music')
#            self.conn  = MySQLdb.connect(login_info_osx)
            elif platform.uname().node == 'OSXAir.home.home':
#            self.conn  = connDb.connect(host='OSXAir.home',user='rduvalwa2',password='blu4jazz',db='Music')
                self.conn = MySQLdb.connect(host=login_info_osxAir['host'], user=login_info_osxAir['user'], password=login_info_osxAir['password'], db=login_info_osxAir['db'])
            elif platform.uname().node == 'C1246895-WIN64-Air':
        #    self.conn  = connDb.connect(host='OSXAir.home.home',user='rduvalwa2',password='blu4jazz',db='Music')
                self.conn = MySQLdb.connect(login_info_WIN64_Air)
            elif platform.uname().node == 'Randalls-MBP.home':
                print("Host is " , 'Randalls-MBP.home')
                self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')            
            else:
                print("Host is " , 'default')
                self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')
            self.base = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music"
            self.server = 'OSXAir.home' 
            self.notTestRun = test  
        
        def check_artist_table(self):
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.artist,a.genre FROM `Music`.album2songs a WHERE a.artist NOT IN (SELECT b.artist FROM Music.artist b);"
            print(selectStatement)
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    print(item)
            cursor.close()

        def check_albums_table(self):
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.album, a.artist, a.genre, a.type FROM `Music`.album2songs a WHERE a.album NOT IN (SELECT b.album FROM Music.artist_albums b);"
            print(selectStatement)
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    print(item)
            cursor.close()
            
        def check_genre_songs2albums(self):
            result = []
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.album as 'album album', a.genre as 'album genre', b.genre as 'song genre' FROM `Music`.album2songs b, Music.artist_albums a WHERE a.album = b.album and a.genre != b.genre;"
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    result.append(item)
#                    print(item)
            cursor.close()
            return result
       
        def check_Type_songs2albums(self):
            result = []
            cursor = self.conn.cursor()
            selectStatement = "SELECT DISTINCT a.album as 'album album', a.type as 'album type', b.type as 'song type' FROM `Music`.album2songs b, Music.artist_albums a WHERE a.album = b.album and a.type != b.type;"
            if self.notTestRun:
                cursor.execute(selectStatement)
                rows = cursor.fetchall()
                for item in rows:
                    result.append(item)
#                    print(item)
            cursor.close()
            return result    
        
if __name__ == '__main__':
    pass
'''
    runMode = "Run"  # NoRun  # Test
    
    trueLoad = musicLoad_Functions(True)
    genreList = ['Alternative','BlueGrass','Blues','Classic','Country','Folk','Holiday',\
                            'Jazz','Latino','Pop','Regae','Rock','RockaBilly','Soul','Talk', \
                            'TestGenre','TexMex','Traditional','World','Easy Listening']
    trueLoad.set_genre_genre(genreList)

    if runMode == "NoRun":
            pass
    if runMode == "Run":
        trueLoad = musicLoad_Functions(True)
        trueLoad.initial_insert_into_album2songs()
        allSongs = trueLoad.get_all_songs()
        print('num songs is ', len(allSongs))
    
        trueLoad.sync_song_genre()
        trueLoad.sync_song_type()
        '''
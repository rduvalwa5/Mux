'''
Feb 5 2021
@author: rduvalwa2
'''
import os, platform
import pymysql
from Musicdb_info import *


class Verify_musicAritst:

    def __init__(self):
        print("*************** Node Name is ", platform.uname().node)
        self.Node = os.uname().nodename
        if platform.uname().node == 'OSXAir.local':
            self.conn = pymysql.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
        elif platform.uname().node == 'Macbook16.loca':
            print("Host is " , 'Macbook16.loca')
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music') 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
        else:
            print("Host is " , 'default')
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music') 
            self.base = "/Users/rduvalwa2/Music/Music/Media.localized"
            
            print(self.Node)

        host = self.Node
        user = 'rduvalwa2'
        password = 'blu4jazz'
        db = 'music'
        
        countryArtistList = ["Dolly Parton", "Alabama", "Alison Krauss", "Alison Krauss & Brad Paisley", "Alison Krauss & John Waite", "Alison Krauss & Union Station", "Asleep At the Wheel", "Bill Monroe", "Boxcar Willie", "Brenda Lee", "Chanel Campbell", "The Charlie Daniels Band", "Charlie Rich", "Chet Atkins and Hank Snow", "Cody Bryant and The Riders Of The Purple Sage", "Colt Ford", "David Allan Coe", "Della Mae", "Dierks Bentley", "Dixie Chicks", "Eilen Jewell", "Eldorado", "Emmylou Harris", "Emmylou Harris with Herb Pedersen", "Emmylou Harris with Roy Orbison", "Florida Georgia Line", "Foy Willing & The Riders Of The Purple Sage", "Gram Parsons", "Hank Williams, Jr.", "Jack Ingram", "James Otto", "Jamey Johnson", "Jerry Jeff Walker", "Jessi Colter", "Jessi Colter & Sunny Sweeney", "Jewel", "Jimmy Buffet", "John Hiatt", "Johnny Cash", "Josh Thompson", "Justin Moore", "Keith Urban ", "Kenny Rogers & The First Edition", "Kris Kristofferson", "Kris Kristofferson & Patty Griffin", "Linda Ronstadt", "Lori McKenna", "Mark O'Connor", "The Marshall Tucker Band", "Marty Robbins", "The Mavericks", "Michael Martin Murphey", "Montgomery Gentry", "New Riders of the Purple Sage", "Nitty Gritty Dirt Band", "Olivia Newton-John", "Pat Green", "Patsy Cline", "Polecat", "Prairie Flyer", "Randy Houser", "Redbird", "Robert Plant & Alison Krauss", "Shooter Jennings", "Stray Birds", "The Texas Tornados", "Texas Tornados", "Trace Adkins", "Uncle Earl", "Van Morrison", "Waylon and Willie", "Waylon Jennings", "Waylon Jennings & The Waylors", "Waylon Jennings & Willie Nelson", "Willie Nelson and Leon Russel", "Wyatt McCubbin", "Zac Brown Band"]
        popArtistList = ["Yo-Yo Ma", "Sarah McLachlan", "Reflejo de Luna", "Nat _King_ Cole", "Celtic Christmas", "Bing Crosby", "Armik", "Tony Bennett", "Ottmar Liebert%", "Noam Chomsky", "Philip Selway", "Padraig MacMathuna", "Ottmar Liebert_Luna Negra", "Ottmar Liebert", "Mannheim Steamroller", "Loreena McKennitt", "Julio Iglesias", "ADELE", "The Airborne Toxic Event", "Alexander", "Arcade Fire", "Art Garfunkel", "The Coats", "Cold War Kids", "Dean Martin", "Death Cab for Cutie", "Del Shannon", "Diego Garcia", "Frank Sinatra", "Frank Sinatra & Dean Martin", "Frank Sinatra & Sammy Davis Jr.", "Frank Sinatra, Dean Martin & Sammy Davis Jr.", "Generationals", "George Baker & George Baker Selection", "Harry Nilsson", "Iron & Wine", "Jackson Browne", "Jeremy Camp", "Jesse Thomas", "Jose Feliciano", "Judy Collins", "Junip", "k.d. lang and the Siss Boom Bang", "Leo Sayer", "Lesley Gore", "The Mamas & The Papas", "Nashville Teens", "Neil Diamond", "Neil Sedaka", "Norah Jones", "Parts & Labor", "Paul Simon", "Percy Sledge", "Peter Bjorn and John", "Playing for Change", "Rita Coolidge", "S. Carey", "Sammy Davis Jr.", "Sammy Davis Jr. & Dean Martin", "Sarah Jarosz", "Say Hi", "The Shadows", "Telekinesis", "The Tokens", "Tom Jones", "Tom Jones, Johnnie Spence & Orchestra", "We Are Augustines", "Wrabel", "Wye Oak"]
        jazzArtistList = ["Walt Weiskopf Nonet", "Pat Metheny Trio", "Alex Hargreaves", "Branford Marsalis", "Brecker Brothers", "Buddy Tate", "Chick Corea", "Darius Brubeck", "Dave Brubeck Quartet", '%Dave Brubeck%' , "Devin Duval", "Duke Ellington", "Eddie Lockjaw Davis", "Fats Waller", "Gary Burton, Steve Swallow, Roy Haynes, Tiger Okoshi", "Grant Green", "Hank Jones", "Herbie Hancock", "Ian Hunter", "Jaco Pastorius", "Jaco Pastorius With Herbie Hancock", "The Jazz Crusaders", "Jerry Gonzalez & The Fort Apache Band", "Jimmy Witherspoon", "Joe Henderson", "John Coltrane", "John Coltrane & Johnny Hartman", "John Scofield", "Keith Jarrett", "Les McCann", "Less McCann and Eddie Harris", "Lester Young", "Madeleine Peyroux", "Mary Pastorius", "Mass Mental", "Michael Brecker", "Miles Davis", "Miles Davis Quintet", "Miles Davis Sextet_Sonny Rollins", "Miles Davis_Sonny Rollins", "Oscar Peterson", "The Overton Berry Trio", "Pat Martino", "Pat Metheny", "Pat Metheny Group", "The Quintet", "Rodrigo Y Gabriela", "Sonny Rollins", "Sonny Stitt", "Stanley Turrentine", "Tech N9ne", "The Jazz Crusaders", "Thelonious Monk", "Thelonious Monk Quartet With John Coltrane", "Tony Burgos & His Swing Shift Orchestra", "Various Artists", "Walt Weiskopf", "Weather Report"]
        bluegrassArtistList = ["The Chieftains", "Crooked Still", "Infamous Stringdusters", "Mountain Heart", "Sarah Jarosz", "Tim O'Brien", "Uncle Earl", "Walela"]
        folkArtistList = ["The Kingston Trio", "Peter Paul and Mary", "Pete Segear Arlo Guthrie", "Arlo Guthrie", "Barry McGuire", "Bee Gees", "Bob Dylan", "Cat Stevens", "Gordon Lightfoot", "The Handsome Family", "Harry Belafonte", "Joan Baez", "John Fahey", "John Fahey & His Orchestra", "John Prine", "Joni Mitchell", "Josh Rouse", "Judy Collins", "Kingston Trio", "Leo Kottke", "Mark Lanegan", "Pete Seeger & Arlo Guthrie", "Peter, Paul & Mary", "Richie Havens", "Rodriguez", "Steve Goodman", "The Wailin' Jennys"]
        bluesArtistList = ["Alvin Lee & Ten Years Later", "Mavis Staples", "Alvin Lee", "Alvin Lee & Richard Newman", "Alvin Lee, Richard Newman & Tim Hinkley", "Billy Holliday", "Blues Artists", "Bob Forrest", "The Box Tops", "Boz Scaggs", "Clarence Gatermouth Brown", "Cream", "Eric Clapton", "Eric Clapton & B.B. King", "Gregg Allman", "Hot Tuna", "Jimmy Witherspoon", "Joe Louis Walker", "John Lee Hooker", "John Mayall", "John Mayall & The Bluesbreakers", "Johnny Winter", "Muddy Waters", "North Mississippi Allstars", "The Paul Butterfield Blues Band", "R.L. Burnside", "Richie Havens", "Savoy Brown", "Stevie Ray Vaughan", "Stevie Ray Vaughan & Double Trouble", "Ten Years After", "War", "Wynton Marsalis & Eric Clapton", "The Yardbirds", "18 South"]
        classicalArtistList = ["Andre Kostelanetz and his orchestra", 'Charles Dutoit%', 'Alfred Hause%', 'Angele Dubeau%', "Antonio Vivaldi", "Branford Marsalis", "Branford Marsalis & Orpheus Chamber Orchestra", "Dvorak", "A Fielder Boston Pops", "Mark O'Connor", "Oliver Kane", "Ravel", "Richard Wagner", "Wagner"]
    
    def get_music_artist_Dir(self):
        artistDir = []
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artistDir.append((directory))
        artistDir.sort()
        return artistDir

    def get_all_artist_DB(self):
        statement = "select artist from music.artist order by music.artist.artist;"
        print(statement)
        cursor = self.conn.cursor()
        try:
            cursor.execute(statement)
            result = cursor.fetchall()  
            cursor.close()
            self.conn.close()
            return result  
        except self.conn.Error as err:
            print("Exception is ", err)
            return str(err)               
    
    def print_artist_List(self):
        myartist = self.get_music_artist_Dir()
#        sortedArtist = myartist.sort()
#        print(sortedArtist)
        for artist in myartist:
            print(artist)

    def verify_music_artist(self):
        artist = []
        index = 0
        musicDirs = os.listdir(self.base)
        for directory in musicDirs:
            if os.path.isdir(self.base + "/" + directory):
                artist.append((index, directory))
                index = index + 1
        return artist

        
if __name__ == '__main__':
    x = Verify_musicAritst()
    dirArtist = x.get_music_artist_Dir()
    dirArtist.sort()
    dbArtist = x.get_all_artist_DB()
    
    newDbArtist = []
    for xx in dbArtist:
        newDbArtist.append(xx[0])
    
    print("dir Length ", len(dirArtist))
    print("db Lenth ", len(dbArtist))
        
    ArtistNotInDataBase = []
    for cc in newDbArtist:
        if cc not in dirArtist:
            ArtistNotInDataBase.append(cc)
    print(ArtistNotInDataBase)
            
    print("Artist is in the data base but not in the directories")
    
    ArtistNotInDirectory = []
    for cc in dirArtist:
        if cc not in newDbArtist:
            ArtistNotInDirectory.append(cc)
    print(ArtistNotInDirectory)
            
    print("Artist is in the directories but not in the Data Base")

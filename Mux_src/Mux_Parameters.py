'''
Created on Dec 20, 2020

@author: rduvalwa2
'''

import os, platform
import pymysql
from  Musicdb_info import login_info_osxAir
from Musicdb_info import login_info_default
from Musicdb_info import login_info_Macbook16


class Mux_Parameters:
    
    def __init__(self):
        print("*************** Node Name is ", platform.uname().node)
        if platform.uname().node == 'OSXAir.local':
            self.conn = pymysql.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
        elif platform.uname().node == 'Macbook16.loca':
            print("Host is " , 'Macbook16.loca')
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music') 
#            self.cover_base = "/Users/rduvalwa2/Documents/GitHub/Mux/AlbumCovers"
        else:
            print("Host is " , 'default')
            self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music') 
    
            self.Node = os.uname().nodename
            print(self.Node)
            
            self.countryArtistList = ['Alabama', 'Alison Krauss', 'Alison Krauss & Union Station', 'Bill Monroe', 'Bob Dylan', 'Boxcar Willie', 'Brenda Lee', 'Charlie Rich', 'Chet Atkins and Hank Snow', 'Cody Bryant and The Riders Of The Purple Sage', 'Compilations', 'Della Mae', 'Dierks Bentley', 'Dixie Chicks', 'Dolly Parton, Linda Ronstadt & Emmylou Harris', 'Eilen Jewell', 'Emmylou Harris', 'Emmylou Harris & Rodney Crowell', 'Eric Church', 'Florida Georgia Line', 'Foy Willing & The Riders Of The Purple Sage', 'Hank Williams', 'Jerry Jeff Walker', 'Jewel', 'Jimmy Buffet', 'Jo Dee Messina', 'John Denver', 'Johnny Cash', 'Kenny Rogers', 'Kris Kristofferson', 'Linda Ronstadt', 'Linda Ronstadt & Emmylou Harris', 'Lonestar', 'Lori McKenna', 'Marty Robbins', 'Michael Martin Murphey', 'Old Crow Medicine Show', 'Olivia Newton-John', 'Pat Benatar', 'Patsy Cline', 'Polecat', 'Prairie Flyer', 'Redbird', 'Rita Coolidge', 'Robert Plant & Alison Krauss', 'Stray Birds', 'The Charlie Daniels Band', 'Waylon and Willie', 'Waylon Jennings', 'Waylon Jennings & The Waylors', 'Waylon Jennings & Willie Nelson', 'Willie Nelson and Leon Russel']
            self.popArtistList = ['Arcade Fire', 'Beady Eye', 'Billy J. Kramer', 'Bing Crosby', 'Blondie', 'Bobby Darin', 'Bobby Rydell', 'Boz Scaggs', 'Bread', 'Carole King', 'Celtic Christmas', 'City and Colour', 'Cold War Kids', 'Compilations', 'Crispian St. Peters', 'Death Cab for Cutie', 'Del Shannon', 'Dionne Warwick', 'Dusty Springfield', 'Elton John', 'Elton John & Leon Russell', 'Frank Sinatra', 'Freddie & The Dreamers', 'Generationals', 'George Baker', 'Gerry & The Pacemakers', 'Jackson Browne', 'John Fahey', 'Johnny Mathis', 'Jose Feliciano', 'Junip', 'k.d. lang and the Siss Boom Bang', 'Leo Sayer', 'Lesley Gore', 'Little Eva', 'Loreena McKennitt', 'Manfred Mann', 'Marianne Faithfull', 'Nat King Cole', 'Neil Diamond', 'Neil Sedaka', 'Padraig MacMathuna', 'Parts & Labor', 'Paul McCartney', 'Paul Simon', 'Percy Sledge', 'Peter Bjorn and John', 'Petula Clark', 'Playing for Change', 'Roy Orbison', 'Sarah McLachlan', 'Say Hi', 'Sonny & Cher', 'Sting', 'Telekinesis', 'The Airborne Toxic Event', 'The Box Tops', 'The Diamonds', 'The Drifters', 'The Everly Brothers', 'The Honeycombs', 'The Lettermen', 'The Mamas & The Papas', 'The Merseybeats', 'The Monkees', 'The Shangri-Las', 'The Swinging Blue Jeans', 'The Tokens', 'Tom Jones', 'Tony Bennett', 'Wrabel', 'Wye Oak', 'Yo-Yo Ma']
            self.jazzArtistList = ['Alex Hargreaves', 'Andy Narell', 'Branford Marsalis', 'Brecker Brothers', 'Cal Tjader', 'Charlie Parker', 'Chick Corea', 'Compilations', 'Darius Brubeck', 'Dave Brubeck', 'Dave Brubeck Quartet', 'Delirium Blues Project', 'Devin Duval', 'Fats Waller', 'Gary Burton, Steve Swallow, Roy Haynes, Tiger Okoshi', 'Herbie Hancock', 'Jaco Pastorius', 'Joe Henderson', 'John Coltrane', 'John Coltrane & Johnny Hartman', 'John Scofield', 'Keith Jarrett', 'Kenny Burrell & John Coltrane', 'Les McCann', 'Less McCann and Eddie Harris', 'Lester Young', 'Lester Young With The Oscar Peterson Trio', 'Madeleine Peyroux', 'Marsalis-Branford', 'Michael Brecker', 'Miles Davis', 'Miles Davis John Coltrane', 'Miles Davis Quintet', 'Miles Davis Sextet', 'Oscar Peterson', 'Pat Metheny', 'Pat Metheny Group', 'Pat Metheny Trio', 'Sonny Rollins', 'Stan Getz', 'Stanley Turrentine', 'The Cal Tjader Quintet', 'The Jazz Crusaders', 'The Overton Berry Trio', 'The Quintet', 'Thelonious Monk', 'Thelonious Monk Quartet With John Coltrane', 'Tony Burgos & His Swing Shift Orchestra', 'Walt Weiskopf Nonet', 'Weather Report']
            
            self.bluegrassArtistList = ['Crooked Still', 'Infamous Stringdusters', 'Mountain Heart', 'Sarah Jarosz', 'The Chieftains', 'Tim O''Brien', 'Uncle Earl', 'Various Bluegrass Artists', 'Walela']
 
            self.folkArtistList = ['Arlo Guthrie', 'Barry McGuire', 'Bee Gees', 'Bob Dylan', 'Gillian Welch', 'Gordon Lightfoot', 'Harry Belafonte', 'Joan Baez', 'John Prine', 'Joni Mitchell', 'Judy Collins', 'Leo Kottke', 'Leonard Cohen', 'Mark Lanegan', 'Monsters Of Folk', 'Pete Seeger & Arlo Guthrie', 'Peter, Paul & Mary', 'Steve Goodman', 'The Handsome Family', 'The Kingston Trio', 'The Wailin'' Jennys']

            self.frenchPopArtistList = ['Edith Piaf', 'Jacques Brel', 'Leo Ferre']
            
            self.HolidayArtistList = ['Bing Crosby', 'Celtic Christmas', 'The Chieftains', 'Elvis Presley', 'Emmylou Harris', 'Joan Baez', 'Johnny Mathis', 'Jose Feliciano', 'Loreena McKennitt', 'Nat "King" Cole', 'Sarah McLachlan', 'Tony Bennett', 'Yo-Yo Ma']
            
            self.SoundtrackAlbumList = ['Hair', 'La Bamba (Original Motion Picture Soundtrack)', 'Man Of La Mancha', 'The Departed: Music From The Motion Picture', 'Easy Rider (Soundtrack from the Motion Picture) [Deluxe Edition]', 'I''m Not There', 'Masked & Anonymous', 'Tommy']
            
            self.RBSoulArtistList = ['Al Green', 'Aloe Blacc', 'Aretha Franklin', 'Average White Band', 'Ben E. King', 'Bill Withers', 'Booker T. & The M.G.''s', 'Booker T. Jones', 'The Brothers Johnson', 'The Chi-Lites', 'The Coasters', 'Dionne Warwick', 'Earth, Wind & Fire', 'The Four Tops', 'Gladys Knight & The Pips', 'Ike and Tina Turner', 'Isaac Hayes', 'The Isley Brothers', 'James Brown', 'Laura Nyro', 'Marvin Gaye', 'Mavis Staples', 'Otis Redding', 'Roberta Flack', 'Roberta Flack & Donny Hathaway', 'The Spinners', 'The Supremes', 'Teddy Pendergrass', 'The Temptations', 'Tower of Power']
  
            self.RockABillyArtistList = ['Billy Lee Riley', 'Carl Perkins', 'Dale Hawkins', 'Jerry Lee Lewis']
            
            self.ReggaeArtistList = ['Agent Sasco (Assassin)', 'Amazula', 'Bob Marley', 'Desmond Dekker', 'Freddie Notes & The Rudies']
            
            self.bluesArtistList = ['18 South', 'Alvin Lee', 'Alvin Lee & Co.', 'Alvin Lee & Company', 'Alvin Lee & Mylon LeFevre ', 'Alvin Lee & Richard Newman', 'Alvin Lee & Ten Years Later', 'Andy Fairweather Low W/ Eric Clapton', 'B.B. King ', 'Billie Holiday', 'Billy Holliday', 'Blake Mills & Derek Trucks', 'Bob Forrest', "Booker T. With Steve Cropper, Keb' Mo', Blake Mills, Matt \"Guitar\" Murphy & Albert Lee", 'Buddy Guy with Junior Wells', 'Buddy Guy, Robert Randolph & Quinn Sullivan', 'Canned Heat', 'Charles Brown', 'Clarence Gatermouth Brown', 'Compilations', 'Cream', 'Doyle Bramhall II & Citizen Cope', 'Doyle Bramhall II & Gary Clark Jr.', 'Earl Klugh', 'Eric Clapton', 'Eric Clapton & B.B. King', 'Eric Clapton & Steve Winwood', 'Eric Clapton & Vince Gill', 'Eric Clapton With Keith Richards', 'Gary Clark Jr.', 'Gregg Allman', 'Gregg Allman, Warren Haynes & Derek Trucks', 'Hot Tuna', 'Jeff Beck', 'Jimmie Vaughan', 'Jimmy Witherspoon', 'Joe Louis Walker', 'John Lee Hooker', 'John Mayall', 'John Mayall & The Bluesbreakers', 'John Mayall & The Bluesbreakers & Eric Clapton', 'John Mayer', 'John Mayer & Keith Urban', 'John Mayer With Doyle Bramhall II', 'Johnny Winter', 'Kurt Rosenwinkel', "Lightnin' Hopkins", 'Los Lobos', 'Muddy Waters', 'North Mississippi Allstars', 'Pinetop Perkins', 'R.L. Burnside', 'Ray Charles', 'Richie Havens', 'Robert Cray Band', 'Savoy Brown', 'Sonny Landreth & Derek Trucks', 'Stevie Ray Vaughan', 'Stevie Ray Vaughan & Double Trouble', "Taj Mahal & Keb' Mo'", 'Ten Years After', 'The Allman Brothers Band & Eric Clapton', 'The Doors', 'The Paul Butterfield Blues Band', 'The Yardbirds', 'Vince Gill / Albert Lee', 'Wynton Marsalis & Eric Clapton']
            self.classicalArtistList = ['A Fielder Boston Pops', 'Alfred Hause And His Vienna Waltz Country Ballroom Orchestra', 'Andre Kostelanetz and his orchestra', 'Angele Dubeau & La Pieta', 'Antonio Vivaldi', 'Branford Marsalis & Orpheus Chamber Orchestra', 'Charles Dutoit, Kyung Wha Chung & Philharmonia Orchestra', 'Compilations', 'Dvorak', 'Julio Iglesias', 'London Philharmonic Orchestra & David Parry', 'Oliver Kane', 'Ravel', 'Reflejo de Luna', 'Richard Wagner', 'Stanley Kubrick', 'Stravinsky', 'Tchaikovsky', 'Various Artist', 'Wagner']
            self.TexMexArtistList = ['A Sleep At the Wheel', 'Doug Sahm', 'Eldorado', 'Freddy Fender', 'Santana', 'Sir Douglas Quintet', 'Texas Tornados', 'The Mavericks', 'Calexico']
        
            self.RockArtistList = ['38 Special', 'Ace Frehley', 'AC_DC', 'Aerosmith', 'Alice Cooper', 'Alligator Stew', 'America', 'Average White Band', 'Bachman-Turner Overdrive', 'Bad Company', 'Badfinger', 'Bee Gees', 'Ben Harper', 'Big Brother & the Holding Company_Janis Joplin', 'Bill Perry', 'Billy Joel', 'BJ Thomas', 'Black Sabbath', 'Blackfoot', 'Blind Faith', 'Blood Sweat & Tears', 'Blue Cheer', 'Blue Oyster Cult', 'Blue Swede', 'Blues Image', 'Bob Seger', 'Bon Jovi', 'Booker T. Jones', 'Boston', 'Brewer & Shipley', 'Bruce Springsteen', 'Bruce Springsteen & The E Street Band', 'Buffalo Springfield', '', 'Cat Stevens', 'Chad & Jeremy', 'Cheap Trick', 'Chicago', 'Chris Robinson Brotherhood', 'Chuck Berry', 'Citizen Cope', 'Classics IV', 'Commander Cody & His Lost Planet Airmen', 'Compilations', 'Creedence Clearwater Revival', 'Crosby, Stills, Nash & Young', 'Dave Dee, Dozy, Beaky, Mick & Tich', 'Dave Edmunds', 'Dave Mason', 'Dave Matthews Band', 'David Allan Coe', 'David Bowie', 'David Bromberg Band', 'Deep Purple', 'Dick Dale & His Del-Tones', 'Dire Straits', 'Don McLean', 'Donovan', 'Doobie Brothers', 'Dr. John', 'Drive-By Truckers', 'Dropkick Murphys', 'Duran Duran', 'Eagles', 'Eddie Vedder', 'Edgar Winter', 'Electric Light Orchestra', 'Elvin Bishop', 'Elvis Costello', 'Elvis Presley', 'Emerson, Lake & Palmer', 'Faces', 'Fleet Foxes', 'Fleetwood Mac', 'Foghat', 'Foreigner', 'Gary Lewis & The Playboys', 'Gary Puckett & The Union Gap', 'Genesis', 'George Harrison', 'Gerry Rafferty', 'Golden Earring', 'Grand Funk Railroad', 'Grateful Dead', 'Guns N'' Roses', 'Harry Nilsson', 'Heart', 'Herman''s Hermits', 'Huey Lewis & The News', 'Humble Pie', 'Ian Anderson', 'Iggy & The Stooges', 'Iron & Wine', 'Iron Butterfly', 'Iron Butterfly & Vanilla Fudge', 'J. J. Cale With Leon Russell', 'J.J. Cale', 'J.J. Cale & Eric Clapton', 'James Gang', 'Jan & Dean', 'Janis Joplin', 'Jason Isbell & The 400 Unit', 'Jeff Beck', 'Jefferson Airplane', 'Jerry Garcia Band', 'Jethro Tull', 'Jim Croce', 'Jimi Hendrix', 'Joe Cocker', 'Joe Walsh', 'John Fogerty', 'John Lennon', 'John Mellencamp', 'Johnny Nash', 'Johnny Rivers', 'Journey', 'Kansas', 'Keith Richards', 'Keith Urban', 'Kenny Rogers & The First Edition', 'Kiss', 'Led Zeppelin', 'Lenny Kravitz', 'Linkin Park', 'Little Dragon', 'Little Feat', 'Little Richard', 'Little River Band', 'Lloyd Price', 'Loggins And Messina', 'Los Bravos', 'Los Lobos', 'Lou Reed', 'Lovin Spoonful', 'Lynyrd Skynyrd', 'Mark Knopfler', 'Mark Knopfler & Emmylou Harris', 'Mark Knopfler_Emmylou Harris', 'Mark Lindsey, Paul Revere & The Raiders', 'Mason Williams', 'Meat Loaf', 'Men At Work', 'Metallica', 'Mitch Ryder & The Detroit Wheels', 'Motley Crue', 'Motorhead', 'Mungo Jerry', 'Nancy Sinatra', 'Nancy Sinatra And Lee Hazlewood', 'Nashville Teens', 'Neil Young', 'Neil Young & Crazy Horse', 'Neko Case', 'New Riders of the Purple Sage', 'Nirvana', 'Nitty Gritty Dirt Band', 'Patti Smith', 'Paul McCartney & Wings', 'Pete Segear Arlo Guthrie', 'Pete Townshend & Ronnie Lane', 'Peter & Gordon', 'Pink Floyd', 'Poco', 'Prince', 'Procol Harum', 'Queen', 'Queenryche', 'R.E.M.', 'Radiohead', 'Ram Jam', 'REO Speedwagon', 'Ricketic', 'Ringo Starr', 'Ritchie Valens', 'Robert Plant', 'Rod Stewart', 'Rodriguez', 'Rush', 'Sam the Sham & The Pharaohs', 'Santo And Johnny', 'Seals & Crofts', 'Simon & Garfunkel', 'Small Faces', 'Spanky & Our Gang', 'Stealers Wheel', 'Steely Dan', 'Steppenwolf', 'Steve Miller Band', 'Sting & The Police', 'Strawberry Alarm Clock', 'Stray Cats', 'Styx', 'Supertramp', 'T. Rex', 'Texas Tornados', 'The 5.6.7.8''s', 'The Allman Brothers Band', 'The Amazing Rhythm Aces', 'The American Breed', 'The Animals', 'The Association', 'The B-52''s', 'The Band', 'The Beach Boys', 'The Beatles', 'The Beau Brummels', 'The Box Tops', 'The Buckinghams', 'The Byrds', 'The Cars', 'The Castaways', 'The Centurions', 'The Dave Clark Five', 'The Dickey Betts Band', 'The Doobie Brothers', 'The Electric Prunes', 'The Five Americans', 'The Gentrys', 'The Georgia Satellites', 'The Grass Roots', 'The Guess Who', 'The Hillbilly Moon Explosion', 'The Hollies', 'The Human Beinz', 'The Kingsmen', 'The Kinks', 'The Knack', 'The Left Banke', 'The Marketts', 'The Marshall Tucker Band', 'The Moody Blues', 'The Outlaws', 'The Outsiders', 'The Ozark Mountain Daredevils', 'The Pointer Sisters', 'The Police', 'The Righteous Brothers', 'The Rolling Stones', 'The Searchers', 'The Seeds', 'The Shadows', 'The Sonics', 'The Soundtrack Studio Stars', 'The Spencer Davis Group', 'The Stooges', 'The Surfaris', 'The Sweet', 'The Traveling Wilburys', 'The Tremeloes', 'The Troggs', 'The Turtles', 'The Ventures', 'The Who', 'The Who At Filllmore East 1968', 'The Young Rascals', 'The Youngbloods', 'The Zombies', 'Them', 'Thin Lizzy', 'Three Dog Night', 'Tina Turner', 'Tom Petty & The Heartbreakers', 'Tommy James & The Shondells', 'Toto', 'Traffic', 'Traveling Wilburys', 'Triumph', 'U2', 'Union Gap', 'Van Morrison', 'Various artists', 'War', 'Wayne Fontana & The Mindbenders', 'White Lion', 'Wilbert Harrison', 'Yes', 'ZZ Top', '_ & The Mysterians']  

    def get_conn(self):
            Node = os.uname().nodename
            print("In base", Node)
            if platform.uname().node == 'OSXAir.local':
                self.conn = pymysql.connect(host='OSXAir.home.home', user='rduvalwa2', password='blu4jazz', db='Music')
            elif platform.uname().node == 'Macbook16.loca':
                self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music') 
            else:
                print("Host is " , 'default')
                self.conn = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music') 
                
            return self.conn
    
    def get_Rock_Artist(self):
        return self.RockArtistList
    
    def get_Pop_Artist(self):
        return self.popArtistList
    
    def get_Jazz_Artist(self):
        return self.jazzArtistList
    
    def get_RockABilly_Artist(self):
        return self.RockABillyArtistList
    
    def get_FrenchPop_Artist(self):
        return self.frenchPopArtistList
    
    def get_Folk_Artist(self):
        return self.folkArtistList
    
    def get_BlueGrass_Artist(self):
        return self.bluegrassArtistList
    
    def get_Reggae_Artist(self):
        return self.ReggaeArtistList
    
    def get_RnBSoul_Artist(self):
        return self.RBSoulArtistList
    
    def get_Blues_Artist(self):
        return self.bluesArtistList
    
    def get_Classical_Artist(self):
        return self.classicalArtistList
    
    def get_Country_Artist(self):
        return self.countryArtistList 
    
    def get_TexMex_Artist(self):
        return self.TexMexArtistList

    def get_soundTrack_Albums(self):
        return self.SoundtrackAlbumList
    
    def get_Node(self): 
            Node = os.uname().nodename
#            print(Node)
            return(Node)
     
    def get_base(self): 
            Node = os.uname().nodename
            print("In base", Node)
            if Node == "OSXAir.local":
                base = "/Users/rduvalwa2/Music/Music/Media.localized/"
                return(base)
            if Node == "Macbook16.local":
                base = "/Users/rduvalwa2/Music/Music/Media.localized/"
                return(base)
            
    def get_CoverBase(self):
            Node = os.uname().nodename
            print("In base", Node)
            if Node == "OSXAir.local":
                coverbase = "/Users/rduvalwa2/Music/AlbumCovers" 
                return(coverbase)
            if Node == "Macbook16.local":
                coverbase = "/Users/rduvalwa2/Music/AlbumCovers" 
                return(coverbase)
    
    def get_genreList(self): 
            genreList = ['Blue Grass', 'Blues', 'Classical', 'Country', 'Folk', 'French Pop', 'Holiday', 'Jazz', 'Pop', 'R&B/Soul', 'Reggae', 'Rock', 'RockaBilly', 'Soundtrack', 'TexMex']
            return(genreList)
     
    def get_MediumList(self): 
            mediumList = ['CD', 'Download', 'Itunes', 'Tape', 'Test Type', 'Vinyl']
            return(mediumList)

    def get_TypeList(self): 
            typeList = ['Amazon', 'CD', 'Download', 'Itunes', 'Tape', 'Test Song TYpe', 'Vinyl']
            return(typeList)

    
if __name__ == '__main__':
     
        param = Mux_Parameters()
        print(param.get_genreList())
        print(param.get_Node())
        print("Base ", param.get_base())
        print("Coverbase ", param.get_CoverBase())
        print("Genre list ", param.get_genreList())
        print("Medium List ", param.get_MediumList())
        print("Type List ", param.get_TypeList())
        print("conn ", param.get_conn())
        
        conn = param.get_conn()
 #       statement = "select count(*) from" + "\'genre\' " + ";"  
        statement = "select count(*) from Music.genre;"        
        
        print(statement)     
        cursor = conn.cursor()
        cursor.execute(statement)
        count = cursor.fetchone()
        cursor.close()   
        print(count)      
     
        statement = "select * from Music.genre;"           
        print(statement)     
        cursor = conn.cursor()
        cursor.execute(statement)
        genres = cursor.fetchall()
        cursor.close()   
        print(genres) 
        
        print("rock artist ", param.get_Rock_Artist())     
        print("SoundTrack Albums ", param.get_soundTrack_Albums())

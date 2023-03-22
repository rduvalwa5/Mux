'''
Created on Mar 16, 2017

@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__": 
    mux = musicGet_Functions()
    print(mux.get_count('artist', ''))
#    artistsList = [("Seals & Crofts","Rock"),("Herb Alpert & The Tijuana Brass","Alternative"),("Joni Mitchell","Rock")]
#    artistsList = [("Kenny Rogers & The First Edition","Rock")] #,("Herb Alpert & The Tijuana Brass","Alternative"),("Joni Mitchell","Rock")]
#    artistsList = [('Angele Dubeau & La Pieta', 'Classic'),('Compilations', 'Mix'),('Dave Dee, Dozy, Beaky, Mick & Tich', 'Rock'),('Dick Dale & His Del-Tones', 'Rock'),('George Baker', 'Pop'),('John Fogerty', 'Rock'),('Jose Feliciano', 'Pop'),('Padraig MacMathuna', 'Alternative'),("The 5.6.7.8's", 'Rock'),('The Centurions', 'Rock'),('The Soundtrack Studio Stars', 'Rock'),('ZZ_ZTest', 'Rock')]
    artistsList = [("Blondie", "Rock"), ("Edgar Winter", "Rock")]
    for artist in artistsList:
        mux.add_artist(artist[0], artist[1])
    print(mux.get_count('artist', ''))

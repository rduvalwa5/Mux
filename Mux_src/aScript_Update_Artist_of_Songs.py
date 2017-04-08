'''
Created on Mar 16, 2017

@author: rduvalwa2
[("01 My Back Pages.mp3","Magokoro Brothers"),\
("02 Gotta Serve Somebody.mp3","Shirley Caesar"),\
("03 Down In The Flood (New Version).mp3","Bob Dylan"),\
("04 It's All Over Now, Baby Blue.mp3","Grateful Dead"),\
("05 Most Of The Time.mp3","Sophie Zelmani"), \
("06 On A Night Like This.mp3","Los Lobos"), \
("07 Diamond Joe.mp3","Bob Dylan"), \
("08 Come Una Pietra Scalciata (Like A Rolling Stone).mp3","Articolo"), \
("09 One More Cup Of Coffee.mp3","Sertab"), \
("10 Non Dirle Che Non E' Cosi' (If You See Her, Say Hello).mp3","Francesco De Gregori"), \
("11 Dixie.mp3","Bob Dylan"), \
("12 Senor (Tales Of Yankee Power).mp3","Jerry Garcia"), \
("13 Cold Irons Bound (New Version).mp3","Bob Dylan"), \
("14 City Of Gold.mp3","The Dixie Hummingbirds")]


'''

from Music_Load import song_Add_Update_Delete

        
if __name__ == "__main__" :
    
    song_artist = [("01 Wild Thing (Re-Recorded).m4a","The Troggs"), \
                   ("02 Kicks (Re-Recorded).m4a","Paul Revere & The Raiders"), \
                    ("03 Shakin\\' All Over (feat. Chad Allan) [Re-Recorded].m4a","The Guess Who"), \
                    ("04 Time Won\\'t Let Me (Re-Recorded).m4a","The Outsiders"), \
                    ("05 Liar, Liar.m4a","The Castaways"), \
                    ("06 Bend Me, Shape Me (Re-Recorded).m4a","The American Breed"), \
                    ("07 Lady Willpower (Re-Recorded).m4a","Gary Puckett & The Union Gap"), \
                    ("08 Wooly Bully (Re-Recorded).m4a","Sam the Sham & The Pharaohs"), \
                    ("09 Western Union (Re-Recorded).m4a","The Five Americans"), \
                    ("10 Laugh, Laugh (Re-Recorded).m4a","The Beau Brummels"), \
                    ("11 Keep On Dancing (Re-Recorded).m4a","The Gentrys"), \
                    ("12 The Letter (Re-Recorded).m4a","The Box Tops"), \
                    ("13 Midnight Confessions (Re-Recorded).m4a","The Grass Roots"), \
                    ("14 Spooky (feat. Dennis Yost) [Re-Recorded].m4a","Classics IV"), \
                    ("15 Windy (Re-Recorded).m4a","The Association"), \
                    ("16 This Diamond Ring (Re-Recorded).m4a","Gary Lewis & The Playboys"), \
                    ("17 Tobacco Road (Re-Recorded).m4a","Nashville Teens"), \
                    ("18 Silence Is Golden (Re-Recorded).m4a","The Tremeloes"), \
                    ("19 Out of Limits (Re-Recorded).m4a","The Marketts"), \
                    ("20 Kind of a Drag (Re-Recorded).m4a","The Buckinghams")]
     
    
    mux = song_Add_Update_Delete(True)
    print(song_artist )
    mux.update_songs_artists(song_artist)

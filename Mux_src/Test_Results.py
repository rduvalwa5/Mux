'''
Created on Apr 25, 2017

@author: rduvalwa2
'''

cover_count = 435
songs_count = 8298
artist_count = 574
artist_albums_count = 956
folk_songs = 614
folk_albums = 45
get_max_index_artist = 604
get_max_index_albums = 1084
get_max_index_songs = 8332
get_song = (1134, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
get_album = (664, 'Ten Years After', 'A Space In Time', 'Blues', 'Download',None,None)
get_artist = (411, 'Ten Years After', 'Blues')
# 1064
get_artist_albums = ((664, 'Ten Years After', 'A Space In Time', 'Blues', 'Download',None, None), (665, 'Ten Years After', 'Recorded Live', 'Blues', 'Download',None, None), (666, 'Ten Years After', 'Undead (Remastered) [Live]', 'Rock', 'Download',None, None),(1064, 'Ten Years After', 'Stonedhenge (Re-Presents)', 'Rock', 'Download',None, None))
get_artist_albums_songs = (('01 One of These Days.m4p',), ('02 Here They Come.m4p',), ("03 I'd Love to Change the World.m4p",), ('04 Over the Hill.m4p',), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p",), ('06 Once There Was a Time.m4p',), ('07 Let the Sky Fall.m4p',), ('08 Hard Monkeys.m4p',), ("09 I've Been There Too.m4p",), ('10 Uncle Jam.m4p',))

get_artist_songs = (('01 One of These Days.m4p', 'A Space In Time'), ('02 Here They Come.m4p', 'A Space In Time'), ("03 I'd Love to Change the World.m4p", 'A Space In Time'), ('04 Over the Hill.m4p', 'A Space In Time'), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p", 'A Space In Time'), ('06 Once There Was a Time.m4p', 'A Space In Time'), ('07 Let the Sky Fall.m4p', 'A Space In Time'), ('08 Hard Monkeys.m4p', 'A Space In Time'), ("09 I've Been There Too.m4p", 'A Space In Time'), ('10 Uncle Jam.m4p', 'A Space In Time'), ('01 One of These Days Live.m4p', 'Recorded Live'), ('02 You Give Me Loving.m4p', 'Recorded Live'), ('03 Good Morning Little Schoolgirl.m4p', 'Recorded Live'), ('04 Help Me.m4p', 'Recorded Live'), ('05 Classical Thing.m4p', 'Recorded Live'), ('06 Scat Thing.m4p', 'Recorded Live'), ("07 I Can't Keep from Cryin' Sometimes.m4p", 'Recorded Live'), ("09 I Can't Keep from Cryin' (Cont'd).m4p", 'Recorded Live'), ('10 Silly Thing.m4p', 'Recorded Live'), ("11 Slow Blues In 'C'.m4p", 'Recorded Live'), ("12 I'm Going Home.m4p", 'Recorded Live'), ('13 Choo Choo Mama.m4p', 'Recorded Live'), ('01 Rock You Mama (Live).m4a', 'Undead (Remastered) [Live]'), ('02 Spoonful (Live).m4a', 'Undead (Remastered) [Live]'), ("03 I May Be Wrong, But I Won't Be Wrong Always (Live).m4a", 'Undead (Remastered) [Live]'), ('04 Summertime _ Shantung Cabbage (Live).m4a', 'Undead (Remastered) [Live]'), ('05 Spider In My Web (Live).m4a', 'Undead (Remastered) [Live]'), ("06 (At the) Woodchopper's Ball [Live].m4a", 'Undead (Remastered) [Live]'), ('07 Standing At the Crossroads (Live).m4a', 'Undead (Remastered) [Live]'), ("08 I Can't Keep from Crying Sometimes _ Extension On One Chord (Live).m4a", 'Undead (Remastered) [Live]'), ("09 I'm Going Home (Live).m4a", 'Undead (Remastered) [Live]'), ('01 Going To Try (Mono).m4a', 'Stonedhenge (Re-Presents)'), ("02 I Can't Live Without Lydia (Mono).m4a", 'Stonedhenge (Re-Presents)'), ('03 Woman Trouble (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('04 Skoobly-Oobly-Doobob (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('05 Hear Me Calling (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('06 A Sad Song (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('07 Three Blind Mice (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('08 No Title (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('09 Faro (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('10 Speed Kills (Mono).m4a', 'Stonedhenge (Re-Presents)'), ('11 Going To Try.m4a', 'Stonedhenge (Re-Presents)'), ("12 I Can't Live Without Lydia.m4a", 'Stonedhenge (Re-Presents)'), ('13 Woman Trouble.m4a', 'Stonedhenge (Re-Presents)'), ('14 Skoobly-Oobly-Doobob.m4a', 'Stonedhenge (Re-Presents)'), ('15 Hear Me Calling.m4a', 'Stonedhenge (Re-Presents)'), ('16 A Sad Song.m4a', 'Stonedhenge (Re-Presents)'), ('17 Three Blind Mice.m4a', 'Stonedhenge (Re-Presents)'), ('18 No Title.m4a', 'Stonedhenge (Re-Presents)'), ('19 Faro.m4a', 'Stonedhenge (Re-Presents)'), ('2-01 Hear Me Calling (Mono _ Single Version).m4a', 'Stonedhenge (Re-Presents)'), ('2-02 Woman Trouble (US Version).m4a', 'Stonedhenge (Re-Presents)'), ('2-03 Boogie On.m4a', 'Stonedhenge (Re-Presents)'), ('2-04 Rock Your Mama (Live At  BBC _Top Gear_ Session, London _ 1968).m4a', 'Stonedhenge (Re-Presents)'), ('2-05 Portable People (Live At  BBC _Top Gear_ Session, London _ 1968).m4a', 'Stonedhenge (Re-Presents)'), ("2-06 I Ain't Seen No Whisky (Live At  BBC _Top Gear_ Session, London _ 1968).m4a", 'Stonedhenge (Re-Presents)'), ('20 Speed Kills.m4a', 'Stonedhenge (Re-Presents)'), ('The Hobbit (Live in Frankfurt)', 'Recorded Live'))
                   
genreList = [('Alternative',3),('BlueGrass',157),('Blues',483),('Classical',43),('Country',909), \
            ('Easy Listening',28),('Folk',614),('Holiday',97),('Jazz',774),('Latino',1),('Pop',518),('Regae',22), \
            ('Rock',4376),('RockaBilly',32),('Soul',44),('Talk',1),('TestGenre',3),('TexMex',154), \
            ('Traditional',23),('World',15)]
typeList = [('CD',3337),('Download',3172),('Tape',24),('TestType',3),('Vinyl',1762)]
genresList = (('Rock', 1), ('Alternative', 7), ('BlueGrass', 8), ('Blues', 9), ('Classical', 10), ('Country', 11), ('Folk', 12), ('Holiday', 13), ('Jazz', 14), ('Latino', 15), ('Pop', 16), ('Regae', 17), ('RockaBilly', 18), ('Soul', 19), ('Talk', 20), ('TestGenre', 21), ('TexMex', 22), ('Traditional', 23), ('World', 24), ('NewGenre', 25), ('Easy Listening', 26),('Classic', 27))


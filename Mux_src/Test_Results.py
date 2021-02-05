'''
Created on Apr 25, 2017

@author: rduvalwa2

Alternative    11
BlueGrass    179
Blues    803
Classical    65
Country    1137
Easy Listening    28
Folk    696
Jazz    955
Pop    739
R&B    427
Regae    23
Rock    6437
RockaBilly    32
Soul    25
Sound Track    2
Talk    1
TestGenre    3
TexMex    218
'''

cover_count = 1253
songs_count = 11914
artist_count = 592
artist_albums_count = 1262
folk_songs = 684
folk_albums = 62
get_max_index_artist = 594
get_max_index_albums = 1303
get_max_index_songs = 12158
#get_song = (1134, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
get_song = ((2389, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Grateful Dead', 'The Grateful Dead (Skull & Roses)', '09 Johnny B. Goode.mp3', 'Rock', 'Download', 1), (4044, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1))
get_album = ((261, 'Ten Years After', 'A Space In Time', 'Blues', 'Download', 'Ten Years After A SpaceIn Time.jpg', 1464))
get_artist = (95, 'Ten Years After', 'Blues')
get_artist_albums = ((258, 'Ten Years After', 'Stonedhenge (Re-Presents)', 'Blues', 'Download', 'Ten Years After Stonehenge.jpeg', 1466), (259, 'Ten Years After', 'Recorded Live', 'Blues', 'Download', 'Ten Years After Recorded Live.jpeg', 1467), (260, 'Ten Years After', 'Undead (Remastered) [Live]', 'Blues', 'Download', 'Ten Years After Undead.jpeg', 1465), (261, 'Ten Years After', 'A Space In Time', 'Blues', 'Download', 'Ten Years After A SpaceIn Time.jpg', 1464), (359, 'Alvin Lee & Ten Years After', 'In Flight', 'rock', 'Download', 'Alvin Lee In Flight.jpg', 1468))
get_artist_albums_songs = (("03 I'd Love to Change the World.m4p",), ('02 Here They Come.m4p',), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p",), ('01 One of These Days.m4p',), ('10 Uncle Jam.m4p',), ('04 Over the Hill.m4p',), ('07 Let the Sky Fall.m4p',), ("09 I've Been There Too.m4p",), ('06 Once There Was a Time.m4p',), ('08 Hard Monkeys.m4p',))

get_artist_songs = (('08 Johnny B. Goode.mp3', 'The Best of Chuck Berry'), ('02 Roll Over Beethoven.mp3', 'The Best of Chuck Berry'), ('10 Sweet Little Sixteen.mp3', 'The Best of Chuck Berry'), ('09 Brown Eyed Handsome Man.mp3', 'The Best of Chuck Berry'), ('07 Maybelline.mp3', 'The Best of Chuck Berry'), ('03 Rock And Roll Music.mp3', 'The Best of Chuck Berry'), ('05 No Particular Place To Go.mp3', 'The Best of Chuck Berry'), ('06 My Ding A Ling.mp3', 'The Best of Chuck Berry'), ('01 School Days.mp3', 'The Best of Chuck Berry'), ("04 Reelin' and Rockin'.mp3", 'The Best of Chuck Berry')) 
genreList = [('Rock', 6411), ('Alternative', 11), ('BlueGrass', 179), ('Blues', 803), ('Country', 1153), ('Folk', 684), ('Holiday', 0), ('Jazz', 921), ('Latino', 1), ('Pop', 663), ('Regae', 23), ('RockaBilly', 32), ('Soul', 25), ('Talk', 1), ('TestGenre', 3), ('TexMex', 228), ('Traditional', 0), ('World', 0), ('NewGenre', 0), ('Easy Listening', 28), ('Classical', 115), ('R&B', 467), ('French Pop', 78),('Audio Book',81),('Audiobooks',2),('Sound Track',2),('Soundtrack',2),('Reggae',1)]
typeList = [('CD', 6267), ('Download', 3610), ('Tape',101), ('TestType', 3), ('Vinyl', 1933)]
genresList = (('Rock', 1), ('Alternative', 2), ('BlueGrass', 3), ('Blues', 4), ('Classical', 5), ('Country', 6), ('Folk', 7), ('Holiday', 8), ('Jazz', 9), ('Latino', 10), ('Pop', 11), ('Regae', 12), ('RockaBilly', 13), ('Soul', 14), ('Talk', 15), ('TestGenre', 16), ('TexMex', 17), ('Traditional', 18), ('World', 19), ('NewGenre', 20), ('Easy Listening', 21), ('Classic', 22), ('R&B', 23), ('French Pop', 24))

'''
Rock    1
Alternative    2
BlueGrass    3
Blues    4
Classical    5
Country    6
Folk    7
Holiday    8
Jazz    9
Latino    10
Pop    11
Regae    12
RockaBilly    13
Soul    14
Talk    15
TestGenre    16
TexMex    17
Traditional    18
World    19
NewGenre    20
Easy Listening    21
Classic    22
R&B    23
French Pop    24


Rock    6447
Country    1153
Jazz    968
Blues    803
Pop    663
Folk    696
R&B    467
TexMex    228
BlueGrass    179
Classical    115
Audio Book    81
French Pop    78
RockaBilly    32
Easy Listening    28
Soul    25
Regae    23
Alternative    11
TestGenre    3
Audiobooks    2
Sound Track    2
Soundtrack    2
Reggae    1
Talk    1
Latino    1




'''
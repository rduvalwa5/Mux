'''
Created on Apr 25, 2017

@author: rduvalwa2

BlueGrass    179
Blues    785
Classical    59
Country    939
Easy Listening    28
Folk    677
Jazz    787
Pop    646
Regae    23
Rock    4880
RockaBilly    32
Soul    198
Talk    1
TestGenre    3
TexMex    202

'''

cover_count = 543
songs_count = 9439
artist_count = 496
artist_albums_count = 1006
folk_songs = 677
folk_albums = 51
get_max_index_artist = 496
get_max_index_albums = 1007
get_max_index_songs = 9442
#get_song = (1134, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1)
get_song = ((2389, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Grateful Dead', 'The Grateful Dead (Skull & Roses)', '09 Johnny B. Goode.mp3', 'Rock', 'Download', 1), (4044, 'OSXAir.home', '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music', 'Chuck Berry', 'The Best of Chuck Berry', '08 Johnny B. Goode.mp3', 'Rock', 'Vinyl', 1))
get_album = (188, 'Ten Years After', 'A Space In Time', 'Blues', 'Download', None, None)
get_artist = (95, 'Ten Years After', 'Blues')
get_artist_albums = ((185, 'Ten Years After', 'Stonedhenge (Re-Presents)', 'Blues', 'Download', None, None), (186, 'Ten Years After', 'Recorded Live', 'Blues', 'Download', None, None), (187, 'Ten Years After', 'Undead (Remastered) [Live]', 'Blues', 'Download', None, None), (188, 'Ten Years After', 'A Space In Time', 'Blues', 'Download', None, None))
get_artist_albums_songs = (("03 I'd Love to Change the World.m4p",), ('02 Here They Come.m4p',), ("05 Baby Won't You Let Me Rock 'N' Roll You.m4p",), ('01 One of These Days.m4p',), ('10 Uncle Jam.m4p',), ('04 Over the Hill.m4p',), ('07 Let the Sky Fall.m4p',), ("09 I've Been There Too.m4p",), ('06 Once There Was a Time.m4p',), ('08 Hard Monkeys.m4p',))

get_artist_songs = (('08 Johnny B. Goode.mp3', 'The Best of Chuck Berry'), ('02 Roll Over Beethoven.mp3', 'The Best of Chuck Berry'), ('10 Sweet Little Sixteen.mp3', 'The Best of Chuck Berry'), ('09 Brown Eyed Handsome Man.mp3', 'The Best of Chuck Berry'), ('07 Maybelline.mp3', 'The Best of Chuck Berry'), ('03 Rock And Roll Music.mp3', 'The Best of Chuck Berry'), ('05 No Particular Place To Go.mp3', 'The Best of Chuck Berry'), ('06 My Ding A Ling.mp3', 'The Best of Chuck Berry'), ('01 School Days.mp3', 'The Best of Chuck Berry'), ("04 Reelin' and Rockin'.mp3", 'The Best of Chuck Berry')) 
genreList = [('Alternative', 0), ('BlueGrass', 179), ('Blues', 785), ('Classical', 59), ('Country', 939), \
            ('Easy Listening', 28), ('Folk', 677), ('Holiday', 0), ('Jazz', 787), ('Latino', 0), ('Pop', 646), ('Regae', 23), \
            ('Rock', 4880), ('RockaBilly', 32), ('Soul', 198), ('Talk', 1), ('TestGenre', 3), ('TexMex', 202), \
            ('Traditional', 0), ('World', 0)]
typeList = [('CD', 4199), ('Download', 3392), ('Tape', 24), ('TestType', 3), ('Vinyl', 1821)]
genresList = (('Rock', 1), ('Alternative', 7), ('BlueGrass', 8), ('Blues', 9), ('Classical', 10), ('Country', 11), ('Folk', 12), ('Holiday', 13), ('Jazz', 14), ('Latino', 15), ('Pop', 16), ('Regae', 17), ('RockaBilly', 18), ('Soul', 19), ('Talk', 20), ('TestGenre', 21), ('TexMex', 22), ('Traditional', 23), ('World', 24), ('NewGenre', 25), ('Easy Listening', 26), ('Classic', 27))


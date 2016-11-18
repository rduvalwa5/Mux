select * from Music.songs;

select Music.songs.genre, count(Music.songs.genre) from Music.songs
group by Music.songs.genre
order by Music.songs.genre desc;
/*
Tex Mex		69
Soul		43
Rocka Billy	45
Rock		3839
Regae		22
Pop			340
Jazz		697
Holiday		122
Folk		328
Country		661
Classic		30
Book		1
Blues		289
Blue Grass	92
*/

select Music.songs.artist, count(Music.songs.artist) from Music.songs
group by Music.songs.artist
order by count(Music.songs.artist) desc;

select Music.songs.type, count(Music.songs.type) from Music.songs
group by Music.songs.type
order by count(Music.songs.type) desc;

/*
Load	3230
CD	1680
Vinyl	1649
Tape	19
*/
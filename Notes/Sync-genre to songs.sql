/*  change Type and medium data values   Nov 9 2021*/ 


select * from music_2.artist where genre = 'TexMex' order by artist;

 -- ['A Sleep At the Wheel','Calexico','Doug Sahm','Eldorado','Freddy Fender','Santana','Sir Douglas Quintet','Texas Tornados','The Mavericks']
 
 select distinct artist from music_2.album2songs where genre = 'TexMex' order by artist;
 
select * from music_2.artist where genre = 'Reggae' order by artist;
  
-- ['Agent Sasco (Assassin)','Amazula','Bob Marley','Bob Marley & The Wailers','Desmond Dekker','Freddie Notes & The Rudies']

update music_2.artist set genre = 'Reggae' where artist like 'Agent Sasco (Assassin)';

select * from music.artist where artist like 'Agent Sasco (Assassin)';

select distinct artist, genre from music.album2songs where genre = 'Reggae' order by artist;


select * from music.artist where artist like 'Adele';

select * from music.artist_albums where artist like 'AC%';

select * from music.album2songs where artist like 'Al Green';

update music.album2songs set Medium = 'CD' where type = 'CD';

select distinct genre from music.album2songs order by genre;

use music

UPDATE album2songs
        INNER JOIN
    artist ON album2songs.artist = artist.artist
SET 
    album2songs.genre = artist.genre;


select distinct genre from music.album2songs order by genre;

delete from music.album2songs where genre like 'Test%';


update music.album2songs set genre = 'R&B/Soul' where genre = 'Soul';
update music.album2songs set genre = 'R&B/Soul' where genre = 'R&B';
update music.album2songs set genre = 'Pop' where genre = 'New Age';

-- Music 2
update music_2.album2songs set genre = 'R&B/Soul' where genre = 'Soul';
update music_2.album2songs set genre = 'R&B/Soul' where genre = 'R&B';
update music_2.album2songs set genre = 'Pop' where genre = 'New Age';


select distinct genre from music_2.album2songs order by genre;

UPDATE artist_albums
        INNER JOIN
    artist ON artist_albums.artist = artist.artist
SET 
    artist_albums.genre = artist.genre;
    
select * from music.genre order by genre;
/*
Blue Grass	1
Blues	2
Classical	3
Country	4
Folk	5
French Pop	6
Holiday	7
Jazz	8
Pop	9
R&B/Soul	10
Reggae	11
Rock	12
RockaBilly	13
Soundtrack	14
TexMex	15
*/


delete from music_2.album2songs where genre like 'Test%';

INSERT INTO music_2.genre (genre)
SELECT distinct genre FROM music_2.album2songs order by genre;

delete from music_2.album2songs where genre like 'Test%';

select * from music_2.genre order by genre;
/*
Audio Book	1
Blue Grass	2
Blues	3
Classical	4
Country	5
Folk	6
French Pop	7
Jazz	8
Pop	9
R&B/Soul	10
Reggae	11
Rock	12
RockaBilly	13
Talk	14
TexMex	15
*/

INSERT INTO music.genre (genre)
SELECT distinct genre FROM music.album2songs order by genre;


select * from music.genre order by genre;

/*
Audio Book	1
Blue Grass	2
Blues	3
Classical	4
Country	5
Folk	6
French Pop	7
Jazz	8
Pop	9
R&B/Soul	10
Reggae	11
Rock	12
RockaBilly	13
Talk	14
TexMex	15
*/

-- Nov 9 2021 --------------------------------------

INSERT INTO music.type (type)
SELECT distinct type FROM music.album2songs order by type;


select count(*) from music.album2songs where music.album2songs.type = 'Vinyl';

select * from music.album2songs where music.album2songs.type = 'Itunes';

select * from music.album2songs where music.album2songs.type = 'CD';

select genre, count(genre) from music.album2songs group by genre order by genre;

select distinct type from music.album2songs order by type;

INSERT INTO music_2.type (type)
SELECT distinct type FROM music.album2songs order by type;

INSERT INTO music_2.medium (medium)
SELECT distinct medium FROM music.album2songs order by medium;

select distinct medium FROM music_2.album2songs order by medium;

update music_2.album2songs set medium = 'Download' where medium = 'Downloasd';

select * from music.album2songs where genre = 'Talk';

commit;

select * FROM music.album2songs where type like 'Tape';

select * FROM music.album2songs where medium is NULL;

-----------------------
select count(*) from music.album2songs where music.album2songs.type = 'Vinyl';

select * from music.album2songs where music.album2songs.type = 'Itunes';

select * from music.album2songs where music.album2songs.type = 'CD';

select genre, count(genre) from music.album2songs group by genre order by genre;

select distinct type from music.album2songs order by type;

INSERT INTO music_2.type (type)
SELECT distinct type FROM music.album2songs order by type;

INSERT INTO music_2.medium (medium)
SELECT distinct medium FROM music.album2songs order by medium;

select distinct medium FROM music_2.album2songs order by medium;

update music_2.album2songs set medium = 'Download' where medium = 'Downloasd';

select * from music.album2songs where genre = 'Talk';

commit;

select * FROM music.album2songs where type like 'Tape';

select * FROM music.album2songs where medium is NULL;

select * FROM music.album2songs where artist like '%Foy%';

select * FROM music.album2songs where type like 'itunes';

select * from music.album2songs where album like 'Easy Rider (Soundtrack from the Motion Picture) [Deluxe Edition]';

--------------------------------------------
Album cover

select count(*) from music.artist_albums where cover_name is null;  -- 1054

select count(*) from music.artist_albums where cover_name is not null; -- 335

select * from music.artist_albums where cover_name is null;

select * from music.artist_albums where album like '%Christmas%';

select * from music.artist_albums where artist like '%Blondie%';

select * from music.album2songs where artist like '%Lost%Dogs%';

select * from music.artist_albums where `index` = 1420;

select * from music.album_covers where album_cover like '%Rocks%';

select * from music.album_covers where album_cover like '%Blondie%';


select * from music.album_covers where cover_idx = 1427;

delete from music.album_covers where cover_idx = 1426;

delete from music.artist_albums where `index` = 1426;

select * from music.artist_albums aa, music.album_covers ac
where aa.album in (select ac.album from album_covers);

select * from music.artist_albums where album like '%Hollywood Bowl%';

select * from album2songs where album like '%Hollywood Bowl%';

select * from album2songs where artist like '%Beatles%' order by album;

select cover_idx, album_cover from music.album_covers where album_cover like '%Chicago%';

select * from music.album_covers where album_cover like '%Aladdin%Sane%';


select * from music.artist_albums where artist like '%Chicago%';

select * from music.artist_albums where album like '%Joan Baez (The Classic Debut Album..Plus!)%';

select * from music.artist_albums where cover_name is null;

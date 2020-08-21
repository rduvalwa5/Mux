select * from album2songs where album2songs.`artist` like '%REO%' order by album ,song;

select * from artist where artist like '%REO%';

select * from artist_albums where artist like '%REO%';

delete from artist_albums where `index` = 1230;

select * from `album2songs` where artist like 'Judy Collins' order by album, song;

delete from album2songs where album = 'The Road To Escondido';

delete from `artist_albums` where album = 'The Road To Escondido';

/* table counts */
SELECT count(*) FROM `Music`.artist; -- 576

SELECT count(*) FROM `Music`.artist_albums; -- 1229

SELECT count(*) FROM `Music`.`album2songs`; -- 11933

SELECT count(*) FROM `Music`.`album_covers`;  -- 782

SELECT count(song)
  FROM music.`album2songs`
 WHERE `artist` LIKE 'Compilations'; -- 393

/* create table */

CREATE TABLE Counts (server VARCHAR(50), artist int, albums int, songs int, Input_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

/* create User and data base */

CREATE USER 'rduvalwa2'@'localhost' IDENTIFIED BY 'blu4jazz';

GRANT ALL PRIVILEGES ON * . * TO 'rduvalwa2'@'localhost';

GRANT ALL PRIVILEGES ON * . * TO 'rduval'@'localhost';

/* album cover */

update artist_albums set type = 'Download' where type = 'download';

select * from artist_albums a where a.`cover_name` is null order by `artist`;

select count(*) from artist_albums a where a.`cover_name` is null;

select* from album_covers where `album_cover` = 'JudyCollins_Bothsides.jpg';


select count(*) from music.album2songs where music.album2songs.genre = 'Alternative';


select (select count(*) from artist_albums) - (select count(*) from artist_albums a where `cover_name` is null) as Difference;

select * from album_covers ac wbere ac.`album_cover` like 'iTunesImages.jpg';

select * from artist_albums a where a.`cover_name` is null and a.`type` like 'Vinyl' order by a.`artist` desc; 

select count(*) from artist_albums a where a.`cover_name` is null and a.`type` like 'Vinyl' order by a.`artist` desc;

select count(*) from artist_albums a where a.`cover_name` is null order by a.`artist` desc; 

select * from artist_albums a where a.`cover_name` like 'iTunesImages.jpg' order by `artist` desc;

select * from artist_albums a where a.artist like '%Doobie%'; 

select * from artist_albums a where a.`album` like '%Greatest%';

update `artist_albums` set `cover_name` = 'iTunesImages.jpg' where `cover_idx` = 631;

update `artist_albums` set  `cover_idx` = 631  where `cover_name` = 'iTunesImages.jpg';

update artist_albums set `cover_name` = 'iTunesImages.jpg' where type = 'Download' and cover_name is null;

select * from artist_albums where type = 'Download';

select * from `artist_albums`  where `cover_idx` = 631 order by `artist`;

select * from `artist_albums` where `artist` like "%Beatles%";

/* old  */

SELECT *
  FROM `Music`.artist a;

SELECT *
  FROM `Music`.album2songs a
 WHERE a.song LIKE "%Bogart%";

UPDATE `Music`.album2songs a
   SET a.artist = "The Fraternity of Man"
 WHERE a.song LIKE "%Bogart%";



  SELECT a.genre, count(a.genre)
    FROM `Music`.album2songs a
GROUP BY a.genre
ORDER BY a.genre;

  SELECT a.genre, count(a.genre)
    FROM `Music`.artist a
GROUP BY a.genre;

SELECT *
  FROM `Music`.artist_albums a
 WHERE a.album LIKE 'Chicago Live In Japan [Disc 1]';

SELECT *
  FROM `Music`.artist_albums a
 WHERE a.index > 930;

DELETE FROM `Music`.artist_albums
      WHERE artist_albums.index > 936;

SELECT count(*) FROM `Music`.album2songs;

  SELECT album2songs.genre, count(album2songs.genre)
    FROM `Music`.album2songs
GROUP BY album2songs.genre
ORDER BY album2songs.genre;

  SELECT album2songs.type, count(album2songs.type)
    FROM `Music`.album2songs
GROUP BY album2songs.type
ORDER BY album2songs.type;


-- 543	Compilations		Mix

SELECT *
  FROM music.album2songs
 WHERE music.album2songs.artist LIKE 'Compilations';

-- Music	Compilations	20th Century Rocks_ 60's Rock Bands - Wild Thing (Re-Recorded Versions)
-- The Music Inside_ A Collaboration Dedicated To Waylon Jennings, Volume II
-- The Music Inside - A Collaboration Dedicated to Waylon Jennings, Vol. 1
-- The Departed
-- The Cream Of Clapton
-- The Anthology
-- Strawberry Letter 23_ The Very Best of the Brothers Johnson
-- Singin' With Emmylou Volume 1 (P) 2000
-- Masked & Anonymous
-- Mambo Bounce
-- I'm Not There [Disc 2]
-- I'm Not There [Disc 1]
-- Gypsy Soul_ New Flamenco
-- Easy Rider (Soundtrack from the Motion Picture) [Deluxe Edition]
-- Delta Lady_ The Rita Coolidge Anthology [Disc 2]
-- Delta Lady _ The Anthology
-- 50's Rock
-- 4 John Paul George Ringo - EP
-- 20th Century Rocks_ 60's Rock Bands - Wild Thing (Re-Recorded Versions)

UPDATE `Music`.album2songs
   SET album2songs.genre = 'Alternative'
 WHERE album2songs.album LIKE "Gypsy Soul_ New Flamenco";

SELECT *
  FROM `Music`.album2songs
 WHERE album2songs.album LIKE "Gypsy Soul_ New Flamenco";

SELECT *
  FROM `Music`.album2songs a
 WHERE a.album LIKE 'Anthology%';

UPDATE `Music`.album2songs
   SET artist = 'The Handsome Family'
 WHERE album LIKE
          'Down to the Promised Land - Five Years of Bloodshot Records';

/*  check aainst tables */

SELECT DISTINCT a.album,
                a.artist,
                a.genre,
                a.type
  FROM `Music`.album2songs a
 WHERE a.album NOT IN (SELECT b.album
                         FROM Music.artist_albums b);


SELECT DISTINCT a.album,
                a.artist,
                a.genre,
                a.type
  FROM `Music`.album2songs a
 WHERE a.artist NOT IN (SELECT b.artist
                          FROM Music.artist b);

SELECT DISTINCT
       a.album AS 'album album',
       a.genre AS 'album genre',
       b.genre AS 'song genre'
  FROM `Music`.album2songs b, Music.artist_albums a
 WHERE a.album = b.album AND a.genre != b.genre;

UPDATE Music.artist_albums
   SET Music.artist_albums.genre = 'TestGenre'
 WHERE Music.artist_albums.album LIKE "Test_Album2";

UPDATE `Music`.album2songs
   SET `Music`.album2songs.genre = 'TestG'
 WHERE Music.album2songs.album LIKE "Test_Album2";

SELECT *
  FROM Music.artist_albums
 WHERE Music.artist_albums.album LIKE "The Immediate Years (Disc Two)";


SELECT DISTINCT
       a.album AS 'album album',
       a.type  AS 'album type',
       b.type  AS 'song type'
  FROM `Music`.album2songs b, Music.artist_albums a
 WHERE a.album = b.album AND a.type != b.type;

UPDATE Music.artist_albums
   SET Music.artist_albums.type = 'TestType'
 WHERE Music.artist_albums.album LIKE "Test_Album2";

UPDATE `Music`.album2songs
   SET `Music`.album2songs.type = 'Test'
 WHERE Music.album2songs.album LIKE "Test_Album1";

SELECT *
  FROM Music.artist_albums
 WHERE Music.artist_albums.album LIKE "The Immediate Years (Disc Two)";



SELECT *
  FROM `Music`.artist a
 WHERE artist LIKE 'Chicago';

COMMIT;

SELECT *
  FROM `Music`.artist a
 WHERE artist LIKE 'R.E.M.';

SELECT *
  FROM `Music`.album2songs a
 WHERE artist LIKE 'R.E.M_';

/*
Asleep At the Wheel Remembers the Alamo
Down to the Promised Land - Five Years of Bloodshot Records
In the Air
Greatest Hits
Tres Hombres
*/

SELECT *
  FROM `Music`.album2songs a
 WHERE a.album LIKE 'Greatest Hits';

SELECT DISTINCT a.artist
  FROM `Music`.album2songs a
 WHERE a.artist NOT IN (SELECT b.artist
                          FROM Music.artist b);



SELECT *
  FROM `Music`.album2songs b
 WHERE b.artist LIKE 'Compilations';

DELETE FROM `Music`.album2songs
      WHERE artist LIKE 'R.E.M.' AND album2songs.index < 6815;

UPDATE `Music`.album2songs
   SET artist = 'R.E.M.'
 WHERE artist LIKE 'R.E.M_';

SELECT *
  FROM `Music`.artist a
 WHERE artist LIKE 'Chicago';

UPDATE `Music`.artist
   SET artist = 'Chicago'
 WHERE artist LIKE 'R.E.M';

SELECT artist.*
  FROM Music.artist
 WHERE artist.index > 537;

SELECT DISTINCT a.album, a.genre
  FROM album2songs a
 WHERE a.artist LIKE 'Joni%';

SELECT *
  FROM music.artist_albums b
 WHERE b.index > 908;

DELETE FROM music.artist_albums
      WHERE artist_albums.index > 909;

SELECT *
  FROM music.album2songs a
 WHERE a.artist LIKE
          'Andrea Zonn; Dirk Powell; John Herrmann; Ronnie McCoury; Tim O\'Brien';

SELECT *
  FROM music.album2songs a
 WHERE a.artist LIKE 'Tim O\'Brien';

UPDATE music.album2songs a
   SET artist = 'Tim O\'Brien'
 WHERE a.artist LIKE 'Tim O\'Bien';

SELECT *
  FROM `Music`.artist a
 WHERE a.artist LIKE 'Tim O\'Bien';


SELECT *
  FROM Music.album2songs
 WHERE artist LIKE 'R.E.M.';

UPDATE Music.album2songs
   SET Music.album2songs.genre = 'TexMex'
 WHERE artist LIKE 'Los Lobos';

DELETE FROM Music.album2songs
      WHERE artist LIKE 'R.E.M.';

SELECT *
  FROM Music.artist
 WHERE artist LIKE 'Los Lobos';

SELECT *
  FROM Music.artist_albums
 WHERE artist LIKE '%Jo De%';
 
SELECT *
  FROM Music.album2songs
 WHERE artist LIKE '%Weather Report%'
 order by album , song; 
 

SELECT *
  FROM Music.artist_albums
 WHERE artist LIKE '';

UPDATE Music.album2songs
   SET Music.album2songs.type = 'Download'
 WHERE Music.album2songs.album IN
          ('Oh My Heart - Single', 'In Time - The Best of R.E.M. 1988-2003');


DELETE FROM Music.artist_albums
      WHERE artist_albums.index IN (924)
      

select Music.album2songs.song from Music.album2songs where album2songs.type = 'tape';

select count(*) from Music.Artist;

select * from Music.Artist where artist like "Compilations";

select DISTINCT album from Music.`album2songs` where genre = "Classical" order by album;



/* query to identify type and genre across tables */

select distinct album, artist,  genre, `type`  from NextMusic.`album2songs` order by artist;

select artist_albums.album, artist.artist,  artist_albums.genre, artist.genre
from NextMusic.artist, NextMusic.artist_albums 
where artist_albums.artist = artist.artist
and  artist_albums.genre != artist.genre
order by artist_albums.album, artist_albums.artist;

update artist_albums set genre = 'Country' where album like "50's Rock";

update artist_albums set genre = 'Country' where artist like "Lynyrd Skynyrd";

update artist_albums set genre = 'Folk' where album like "Both Sides Now - The Very Best Of [Disc 2]";

update artist_albums set genre = 'R&B' where artist like "Gladys Knight & The Pips";

select * from artist_albums  where album like "Alabama Greatest Hits";

update artist_albums set artist = 'Judy Collins' where album like "Both Sides Now - The Very Best Of [Disc 2]";

update artist set genre = 'Pop' where artist like 'Santo And Johnny';

update artist_albums set genre = 'Audio Book' where genre like "Audiobooks";

select * from artist where artist like 'Lynyrd Skynyrd';

select * from artist_albums where artist like 'Donovan';

select * from artist_albums;

update artist_albums set album = 'Who Hits' where artist like 'The Who' and album like 'Hits';

INSERT INTO NextMusic.`artist_albums` VALUES (1238, 'Lynyrd Skynyrd', 'Pronounced Leh-nerd Skin-nerd',"Country","CD"," ",0);

delete from NextMusic.`artist_albums` where `index` = 1238;

select  distinct album2songs.`album`, artist_albums.`album`, album2songs.genre, artist_albums.genre, album2songs.artist
from NextMusic.album2songs, NextMusic.artist_albums 
where artist_albums.album = album2songs.`album`
and  artist_albums.genre != album2songs.genre
-- and  album2songs.artist  = 'Gladys Knight & The Pips'
--  and  artist_albums.artist = 'Gladys Knight & The Pips'
order by album2songs.`album`;

select * from album2songs where artist like 'Donovan';

update album2songs set album2songs.genre = "Unknown" where album2songs.album like "IBMA Blue Grass Sample";

update album2songs set genre = "Pop" where album2songs.artist like "Neil Diamond";

update album2songs set artist = "Judy Collins" where album2songs.album like "IBMA Blue Grass Sample";

select * from album2songs where album like 'Donovan';

update album2songs set album = 'Who Hits' where album = 'Hits' and artist = 'The Who';

insert into artsit_albums set album = 'The Supremes Gold [Disc 1]' where album = 'Gold [Disc 1]' and artist = 'The Supremes';


select  distinct album2songs.`album`, artist_albums.`album`, album2songs.type, artist_albums.type, album2songs.artist
from NextMusic.album2songs, NextMusic.artist_albums 
where artist_albums.album = album2songs.`album`
and  artist_albums.type != album2songs.type
-- and  album2songs.artist  = 'Gladys Knight & The Pips'
--  and  artist_albums.artist = 'Gladys Knight & The Pips'
order by album2songs.`album`;


update album2songs set album2songs.type = "CD" where album2songs.album like "The Best of Blondie";

update artist_albums set type = 'CD' where album like '_Heroes_';

select * from music.artist_albums where album like '_Heroes_';

update music.artist_albums set type = 'CD' where album like '_Heroes_';

update music.artist_albums set genre = 'Rock' where album like '_Heroes_';

select * from nextmusic.album2songs  where album like '_Heroes_';

select * from music.album2songs  where album like '_Heroes_';

select * from music.album2songs  where album like '_Heroes_';

update music.album2songs set genre = 'update artist_albums set type = 'CD' where album like "The Best of Blondie";' where album like '_Heroes_';

update nextmusic.album2songs set tupe = 'Download' where album like '_Heroes_';

update nextmusic.album2songs set type = 'Download' where album like '_Heroes_';


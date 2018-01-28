
SET SQL_SAFE_UPDATES = 0;

select count(*) from `Music`.artist;  -- 574 569
select count(*) from music.artist_albums; -- 963
select count(*) from `Music`.album2songs; -- 8373 8062
select count(*) from `Music`.album_covers;  -- 435  473

/* database management */
/*
mysqldump --databases --user=rduval --password  Music > Music_export_into_db.sql

mysql -u username -p database_name < file.sql
if you don't you need to create the relevant database(empty) in MySQL, for that first log on to the MySQL console by running the following command in terminal or in cmd

mysql -u userName -p;
and when prompted provide the password.

Next create a database and use it

mysql>create database yourDatabaseName;
mysql>use yourDatabaseName;

*/

/*  Jan 28 2018 ------------------------------------------------      */

CREATE TABLE `derived_album2songs` (
  `index` bigint(5) NOT NULL,
  `server` varchar(50) DEFAULT NULL,
  `path` varchar(100) NOT NULL,
  `artist` varchar(100) NOT NULL,
  `album` varchar(200) NOT NULL,
  `song` varchar(200) NOT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `genre_idx` bigint(5) unsigned DEFAULT '1',
  PRIMARY KEY (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


commit;


INSERT derived_album2songs
SELECT * FROM album2songs;

select * from music.`album2songs` where `album2songs`.`artist` like 'Eric Clapton';

delete from music.`album2songs` where `album2songs`.`album` like 'Live Back To Macon, GA [Disc 1]';

/* 11-13-2017 ------------------------------------------------      */
update `Music`.artist_albums set artist_albums.cover_name = 'Crud_cover' where artist_albums.index = 1085;

select * from `Music`.artist_albums where cover_name is NULL;

select * from `Music`.artist_albums where `index` = 1085;

select * from `Music`.album2songs a2s where a2s.`song` like '%Test%';

Select * from music.album2songs where song like '%TestSong.mpX' ;

delete from `Music`.album2songs where song = 'TestSong.mpX';

delete from `Music`.album2songs where song like 'TestSong.mpX' and album like 'TestAlbum_X' and artist like 'TestArtist_X_upDate';

delete  from `Music`.album2songs where `index` = 8333;

commit;

select * from `Music`.artist_albums where album = 'Crud_Album';

delete from `Music`.artist_albums where album = 'Crud_Album';

/* 08-31-2017 */

select * from `Music`.artist_albums x;

/* Fixing tests */

select * from music.artist_albums where album like 'Test_Crud_Album';


select * from music.artist_albums;

delete from `Music`.artist_albums where album like 'Test_Crud_Album';
Delete from `Music`.artist_albums where `Music`.artist_albums.album like 'Test_Crud_Album';
delete from `Music`.artist_albums where `Music`.artist_albums.album like 'Test_Crud_Album';

select * from `Music`.album_covers ac where ac.album_cover like '%80%';

/* artist work */

select * from `Music`.album2songs a where a.artist like '%Creedence Clearwater Revival%';


select * from `Music`.artist_albums where `Music`.artist_albums.artist like '%Mysterians';

select * from `Music`.artist where `Music`.artist.artist like '%Test%';

select count(*) from `Music`.artist_albums;  -- 945
select * from `Music`.artist_albums;

delete from `Music`.artist_albums where album like '%Test_Crud_Album';


select count(*) from `Music`.artist;  -- 569
select count(*) from music.artist_albums;
select count(*) from `Music`.album2songs; -- 8062
select count(*) from `Music`.album_covers;  -- 473
select * from `Music`.album_covers;
select * from `Music`.album_covers  where cover_idx > 479; 
delete from `Music`.album_covers where cover_idx > 480; -- in (478,479,481);


delete from `Music`.artist where `Music`.artist.artist like '_ & The Mysterians';

update `Music`.album2songs set `Music`.album2songs.artist = '? & The Mysterians' where `Music`.album2songs.artist like '_ & The Mysterians';
select * from `Music`.album2songs where `Music`.album2songs.artist like '? & The Mysterians';

/*  issue delete album covers */

select * from `Music`.album_covers ac where ac.album_cover like 'animals original hits.jpg';

delete from `Music`.album_covers where cover_idx = 480 ;

delete from `Music`.album_covers where cover_idx in (480,481,482,483,484,485,486);

update `Music`.album_covers set album_cover = 'JoanBaez_First 10 Years.jpg' where album_cover like 'First 10 Years.jpg'; 

select * from `Music`.artist_albums al where al.cover_idx = 1 ; 

select * from `Music`.artist_albums al where al.cover_name like '%Rubber Soul%'; 

update `Music`.artist_albums set cover_name = "", cover_idx = NULL where cover_name like 'Download';



select * from `Music`.album_covers ac where ac.album_cover like '%15BigOnesCover.jpg%';



-- data verifications

select count(*) from `Music`.album2songs where artist like '%Doors'; -- and album like 'Stonedhenge%';
select * from `Music`.album2songs where artist like 'Deep Purple' order by album;

select distinct album from `Music`.album2songs where artist like '%%' order by album;

delete from `Music`.album2songs where `Music`.album2songs.index in (3881,3882,3883,3884,3885,3886,3887,3888,3889,3890,3891,3892,3893,3894,3895);

update `Music`.album2songs set type = 'CD' where album like 'Platinum Jazz';
update `Music`.album2songs set genre = 'Blues' where album like 'Platinum Jazz';

-- 7807  08-29-2017
commit;

select count(distinct artist) from `Music`.album2songs;
-- 470
select count(distinct album) from `Music`.album2songs;
-- 882
select count(song) from `Music`.album2songs; -- where song like '%.m%' or song like '%.aif%';

select song from `Music`.album2songs where song not like '%.m%' and song not like '%.aif%';
-- 7953  there are duplicate song titles


update `Music`.album2songs set song = 'The Hobbit (Live in Frankfurt)' where song like 'The Hobbit (Live in Frankfurt).m4a';
delete from `Music`.album2songs where song like '%.pdf%';
delete from `Music`.album2songs where song like 'Let It Be - iTunes LP (v2.1).itlp';

select count(*) from `Music`.artist;
-- 567  08-29-2017

select count(*) from `Music`.artist_albums;
-- 929  08-29-2017

select count(*) from `Music`.album_covers;
-- 468  08-29-2017

select * from `Music`.genre order by g_idx;
/*
Rock, 1
Alternative, 7
BlueGrass, 8
Blues, 9
Classical, 10
Country, 11
Folk, 12
Holiday, 13
Jazz, 14
Latino, 15
Pop, 16
Regae, 17
RockaBilly, 18
Soul, 19
Talk, 20
TestGenre, 21
TexMex, 22
Traditional, 23
World, 24
NewGenre, 25
Easy Listening, 26
Classic, 27
*/

select a.genre, count(a.genre)  from `Music`.album2songs a group by a.genre order by a.genre;
/*
'Alternative','3'
'BlueGrass','157'
'Blues','446'
'Classical','43'
'Country','897'
'Easy Listening','28'
'Folk','599'
'Holiday','97'
'Jazz','759'
'Latino','1'
'Pop','362'
'Regae','23'
'Rock','4140'
'RockaBilly','32'
'Soul','44'
'Talk','1'
'TestGenre','3'
'TexMex','134'
'Traditional','23'
'World','15'
*/

/* update song name */
update `Music`.album2songs set song = '06 What You Do To Me.mp3' where song like '06What You Do To Me.mp3';

/* update album genre */
update `Music`.album2songs set genre = 'Country' where album like 'Mono';

commit;

select * from `Music`.artist a where a.artist like '%Beach%';

select * from `Music`.artist_albums al where al.album like '%More%';

select * from `Music`.album_covers ac where ac.album_cover like '%Tapes%';

/* counts */
select count(*)  from `Music`.album_covers;
select count(*) from `Music`.album2songs;
select count(*) from `Music`.artist;
select count(*) from `Music`.artist_albums;

select max(`index`)  from `Music`.album_covers;
select max(`index`) from `Music`.album2songs;
select max(`index`) from `Music`.artist;
select max(`index`) from `Music`.artist_albums;

select count(*) from `Music`.album2songs a where a.genre like 'Folk';

/* trouble shooting normalized table*/

select distinct sng.`index`, sng.song,  art.`index`, alb.`index`, alb.album 
                    from `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb 
                    where sng.album = alb.album  
                    and sng.artist = art.artist 
                    and alb.album like 'Noel'
                    order by sng.`index`;
                    
select distinct sng.`index`, sng.song, sng.genre, art.`index`, alb.`index` ,alb.album 
                    from `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb 
                    where sng.album = alb.album  
                    and sng.artist = art.artist 
                    and art.artist like 'Drop%'
                    order by sng.`index`;                    

commit;
/* match CD to album cover */

select count(*) from `Music`.artist_albums a where a.`type` like 'CD' and a.cover_idx is NULL;

select * from `Music`.artist_albums a where a.`type` like 'CD' and a.cover_idx is NULL;

select * from `Music`.album_covers where album_cover like '%Hell%';

delete from `Music`.artist_albums where `index` = 1018;


select * from `Music`.artist_albums where album like 'Drivin\' Wheels_ Best Of 1972-1982 [Disc 1]';

update `Music`.artist_albums set album = 'Keith Urban Fuse' where `index` = 1017;

update `Music`.album_covers set album_cover = 'Waylon and Willie.jpeg' where album_cover like 'Waylon and Willie.jpg';

select *  from `Music`.album_covers order by cover_idx desc;

delete from `Music`.album_covers where cover_idx = 309;




select sng.song, count(sng.song) from `Music`.album2songs sng group by sng.song order by count(sng.song) desc;

/*
ALTER TABLE `Music`.`normal_song` 
CHANGE COLUMN `artist_idx` `artist_idx` BIGINT(5) NOT NULL ,
CHANGE COLUMN `song_idx` `song_idx` BIGINT(5) NOT NULL ;
*/

/*
'01 I Want You.mp3', '3'
'06 Love \'Em And Leave \'Em.mp3', '3'
'04 Ladies Room.mp3', '3'
'09 Hard Luck Woman.mp3', '3'
'02 Take Me.mp3', '3'
'07 Mr. Speed.mp3', '3'normal_song
'05 Baby Driver.mp3', '3'
'10 Makin\' Love.mp3', '3'
'03 Calling Dr. Love.mp3', '3'
'08 See You In Your Dreams.mp3', '3'
'02 New Potato Caboose.mp3', '2'
*/


select * from `Music`.album2songs sng where sng.song like '10 Makin\' Love.mp3';

delete from `Music`.album2songs where `index` in (7022, 7032);


select art.artist, count(art.artist) from `Music`.artist art group by art.artist order by count(art.artist) desc;

/*
'Jose Feliciano', '2'
'Padraig MacMathuna', '2'
*/

select * from `Music`.artist art where art.artist like 'Padraig MacMathuna';

delete from `Music`.artist where `index` in (334);


select al.album, count(al.album) from `Music`.artist_albums al group by al.album order by count(al.album) desc;

/*
'20th Century Rocks 60s Rock Bands - Wild Thing (Re-Recorded Versions)', '20'
'The Music Inside_ A Collaboration Dedicated To Waylon Jennings, Volume II', '12'
'The Departed', '11'
'The Music Inside - A Collaboration Dedicated to Waylon Jennings, Vol. 1', '11'
'4 John Paul George Ringo - EP', '4'
'Delta Lady_ The Rita Coolidge Anthology [Disc 2]', '4'
'50\'s Rock', '4'
'Mambo Bounce', '4'
'The Cream Of Clapton', '3'
'The Sunshine Collection', '3'
'Easy Rider (Soundtrack from the Motion Picture) [Deluxe Edition]', '3'
'Dont Stop The Music', '3'
'In Time - The Best of R.E.M. 1988-2003', '3'
'Workin\' With The Miles Davis Quintet', '2'
'Nightrider', '2'
'Driving Music', '2'
'Legend (Remastered)', '2'
'Oh My Heart - Single', '2'
'Rock Masters_ Bobby Rydell', '2'
'Hair', '2'
'CityScape', '2'
'Unknown Album', '2'
'The Mamas & The Papas Greatest Hits', '2'
'Delta Lady _ The Anthology', '2'
'Back To Back', '2'
'Collapse Into Now', '2'
'See What Tomorrow Brings', '2'

*/

select * from `Music`.artist art where art.artist like 'Hair%';

select * from `Music`.artist_albums al where al.album like 'The Sunshine Collection';

delete from `Music`.artist_albums where `index` in (507,804);

update `Music`.artist_albums set artist = 'various artist' where `index` in (134,507,804);




/* work on delete scripts and rename and adjust for faults in scripts*/

select * from Music.album2songs a where a.artist like '%Dave Matthews Band%';

select * from Music.artist_albums a where a.artist like '%Dave Matthews Band%';

select * from Music.artist_albums a where a.album like 'Everyday';

select * from Music.album2songs a where a.song like '%Johnny B. Goode.mp3';

select * from Music.artist b where b.artist like '%Dave Matthews Band%';

-- insert into Music.artist_albums values (


/* set and unset safe mode */
SET SQL_SAFE_UPDATES = 0;

select count(*) from Music.album2songs;
-- 7069

select max(`index`)   from Music.album2songs;
-- 7084

select count(*) from Music.artist;
-- 559
select max(`index`) from Music.artist;
-- 586

select count(*) from Music.artist_albums;
-- 906
select max(`index`) from Music.artist_albums;
-- 1004


/* add music */

select * from Music.album2songs a where a.artist like '%Airplane%';

update Music.album2songs set album = 'The Essential Jefferson Airplane' where album like 'The Essential Jefferson Airplane [Disc 1]';

update Music.artist_albums set album = 'The Essential Jefferson Airplane' where album like 'The Essential Jefferson Airplane [Disc 1]';

delete from Music.artist_albums where album like 'The Essential Jefferson Airplane [Disc 2]';


select * from Music.artist_albums;

delete from Music.artist_albums where `index` = 998;

select * from Music.artist where artist like '%Dave Matthews%';



/* album cover table */
CREATE TABLE `Music`.`album_covers` (
  `album_cover` VARCHAR(100) NOT NULL,
  `description` VARCHAR(200) NULL,
  `cover_idx` INT NOT NULL,
  `album_idx` VARCHAR(45) NULL,
  UNIQUE INDEX `album_cover_UNIQUE` (`album_cover` ASC),
  PRIMARY KEY (`cover_idx`),
  UNIQUE INDEX `cover_idx_UNIQUE` (`cover_idx` ASC));
  
select * from `Music`.artist_albums a WHERE a.artist like '%Dog Night%';

select count(*) from `Music`.artist_albums a WHERE a.type like 'Vinyl' and a.cover_name is NULL;

select * from `Music`.artist_albums a WHERE a.type like 'Vinyl' and a.cover_name is NULL;

select * from `Music`.artist_albums a WHERE a.type like 'Vinyl' and a.artist like '%Arlo%';

select * from `Music`.album_covers a where a.album_cover like '%Janis%';

select max(cover_idx) from `Music`.album_covers;

select max(cover_idx) from `Music`.album_covers;

select * from  `Music`.album_covers ac;

select * from `Music`.album_covers ac where ac.album_cover like '%Test%';

select * from `Music`.album_covers order by cover_idx desc;

insert into `Music`.album_covers values ('BobbyDarin_MackTheKnife.jpeg','',303,'');

insert into `Music`.album_covers values ('Test Cover','',304,'');

delete from `Music`.album_covers where cover_idx = 305;

select * from `Music`.album_covers ac where ac.cover_idx > 303;

select * from `Music`.album_covers ac where ac.album_cover like 'Next%';

select * from `Music`.album2songs a where a.album like "Pete Seeger & Arlo Guthrie - Together In Concert";



select * from `Music`.artist_albums a WHERE a.`index` in (107,112,116);
delete from `Music`.artist_albums  WHERE `index` in (112,116);

select * from `Music`.artist_albums a where a.album like 'The Brecker Brothers';

update `Music`.album_covers set album_cover = 'chuck_berry.jpg' where cover_idx = 254;




ALTER TABLE `Music`.`album_covers` 
CHANGE COLUMN `cover_idx` `cover_idx` INT(11) UNSIGNED NOT NULL ;


INSERT into  `Music`.`album_covers` (cover_idx,album_cover,description,album_idx)  
values(0,"ABC Years.jpg","18 South",0);

select * from `Music`.`album_covers`;

select * from `Music`.artist_albums a where a.artist like '%Mayall%';

/* Verify all album2songs songs in normalized table */


update `Music`.artist_albums set artist = 'Grateful Dead' where artist = 'The Grateful Dead';
select * from `Music`.album2songs a where a.artist like 'Grateful Dead';

update `Music`.album2songs set artist = 'Grateful Dead' where artist = 'The Grateful Dead';

select max(a.`index`) from `Music`.album2songs a;

select * from `Music`.genre g where g.genre like 'Rock';
 
insert into `Music`.album2songs (`index`, server, path, artist, album, song, genre, type, genre_idx)  values (6862,'fake server','expect not in path','not in artist2','not in album2','expect not in normalized2','noType','Rock',1);


SELECT a.`index`,
       a.song,
       a.artist,
       a.album,
       a.path
  FROM `Music`.album2songs a
 WHERE a.`index` NOT IN (SELECT n.`song_idx`
                           FROM `Music`.normal_song n);



/* Artist table */

select b.artist, b.`index` from `Music`.artist b 
where b.artist NOT IN (select distinct a.artist from `Music`.album2songs a)
order by b.artist asc;

/* reverse artist table check */

select a.artist, a.`index` from `Music`.album2songs a
where a.artist NOT IN (select b.artist from `Music`.artist b )
order by a.artist asc;

select * from `Music`.artist a where a.artist like 'Hank Williams%';

update `Music`.album2songs set genre = 'Classical' where genre like 'classic';

delete from `Music`.artist where artist like "Glen Hansard & Markéta Irglová";

/*
04/22/2017
create genre table and sync albums2songs table

*/


/* project genre table */
insert into `Music`.genre set genre = 'Rock';

select * from `Music`.genre g ;
select g.g_idx from `Music`.genre g where genre like 'Rock';

select a.genre, count(a.genre) from `Music`.album2songs a group by a.genre order by a.genre;

/*
'Alternative','BlueGrass',Blues','Classic','Country','Folk','Holiday','Jazz','Latino','Pop','Regae',
'Rock','RockaBilly','Soul','Talk','TestGenre','TexMex','Traditional','World',
*/

/* Sync album2songs to genre table */

update `Music`.album2songs INNER JOIN  `Music`.genre
on album2songs.genre = genre.genre
set `Music`.album2songs.genre_idx = `Music`.genre.g_idx;

select a.genre, count(a.genre)   from `Music`.album2songs a group by a.genre order by count(a.genre) desc;

select a.genre_idx, count(a.genre_idx)   from `Music`.album2songs a group by a.genre_idx order by count(a.genre_idx) desc;

/* verify table sync */

select a.genre_idx, count(a.genre_idx)
FROM `Music`.album2songs a
group by a.genre_idx
order by count(a.genre_idx) desc;

select a.genre, count(a.genre)
FROM `Music`.album2songs a
group by a.genre
order by count(a.genre) desc;

/* project build normalized table */

/* Verify all album2songs songs in normalized table */

SELECT a.`index`,
       a.song,
       a.artist,
       a.album,
       a.path
  FROM `Music`.album2songs a
 WHERE a.`index` NOT IN (SELECT n.`song_idx`
                           FROM `Music`.normal_song n);
                           
SELECT sng.song as 'Song',
         sng.`index` as 'Song Index',
         art.`index` as 'Artist Index',
         alb.`index` as 'Album'
    FROM `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb
   WHERE sng.album = alb.album AND sng.artist = art.artist
ORDER BY art.`index`, alb.`index`, sng.`index`;

SELECT count(*)
  FROM `Music`.album2songs a
 WHERE a.`index` NOT IN (SELECT n.`song_idx`
                           FROM `Music`.normal_song n);

SELECT sng.song as 'Song',
         sng.`index` as 'Song Index',
         art.`index` as 'Artist Index',
         alb.`index` as 'Album'
    FROM `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb
   WHERE sng.album = alb.album AND sng.artist = art.artist
ORDER BY art.`index`, alb.`index`, sng.`index`;

SELECT a.song as 'song',
         a.`index` as 'song index',
         b.artist as 'artist',
         b.`index` as 'artist index',
         c.album as 'album',
         c.`index` as 'album index'
    FROM `Music`.album2songs a, `Music`.artist b, `Music`.artist_albums c
   WHERE a.album = c.album AND a.artist = b.artist
ORDER BY b.artist,c.album, a.song;


/* 
Collect songs under compilations artist name 
*/

SELECT *
  FROM music.album2songs
 WHERE music.album2songs.artist LIKE 'Compilations';


/*
Verify artist table and album table
*/

SELECT DISTINCT a.album,
                a.artist,
                a.genre,
                a.type
  FROM `Music`.album2songs a
 WHERE a.artist NOT IN (SELECT b.artist
                          FROM Music.artist b);
                    
SELECT DISTINCT a.album,
                a.artist,
                a.genre,
                a.type
  FROM `Music`.album2songs a
 WHERE a.album NOT IN (SELECT b.album
                          FROM `Music`.artist_albums b);


/*
sync artistalbum table to album2songs table
*/

SELECT b.album, b.`index`
 FROM `Music`.artist_albums b
 WHERE b.album NOT IN (SELECT a.album FROM `Music`.album2songs a)
 order by b.index;

SELECT count(*)
 FROM `Music`.artist_albums b
 WHERE b.album NOT IN (SELECT a.album FROM `Music`.album2songs a)
 order by b.album;

select count(distinct a.album) from `Music`.album2songs a;
-- 794

select count(distinct b.album) from `Music`.artist_albums b;
-- 794

select * from `Music`.artist_albums a where a.album like 'The Brecker Bothers';

select * from `Music`.album2songs a where a.album like 'The Brecker Bothers';

select * from `Music`.artist_albums a where a.`index` = 136;

delete from `Music`.artist_albums where `index` = 702;


-- from file

/* Artist table */

select b.artist, b.`index` from `Music`.artist b 
where b.artist NOT IN (select distinct a.artist from `Music`.album2songs a)
order by b.artist asc;


update `Music`.album2songs set artist = 'Al DiMeola' where song like '%Mediterranean Sundance.mp3';



select * from `Music`.album2songs a where a.artist like 'Eddie Vedder & The Million Dollar Bashers';

select * from `Music`.album2songs a where a.song like '%Tombstone Blues%';

select * from `Music`.album2songs a where a.album like 'The Music Inside - A Collaboration Dedicated to Waylon Jennings, Vol. 1';

delete from `Music`.album2songs  where album like 'Gypsy Soul_ New Flamenco' and `Music`.album2songs.index > 6844;

select * from `Music`.artist b where b.artist like 'Eddie Vedder & The Million Dollar Bashers';

select * from `Music`.artist_albums a where a.album like 'Antony & The Johnsons';

delete from `Music`.artist where artist like 'Angèle Dubeau & La Pietà';
/*
04/22/2017
create genre table and sync albums2songs table

*/


/* project genre table */
insert into `Music`.genre set genre = 'Rock';

select * from `Music`.genre g ;
select g.g_idx from `Music`.genre g where genre like 'Rock';

select a.genre, count(a.genre) from `Music`.album2songs a group by a.genre order by a.genre;

/*
'Alternative','BlueGrass',Blues','Classic','Country','Folk','Holiday','Jazz','Latino','Pop','Regae',
'Rock','RockaBilly','Soul','Talk','TestGenre','TexMex','Traditional','World',
*/

/* Sync album2songs to genre table */

update `Music`.album2songs INNER JOIN  `Music`.genre
on album2songs.genre = genre.genre
set `Music`.album2songs.genre_idx = `Music`.genre.g_idx;


/* verify table sync */

select a.genre_idx, count(a.genre_idx)
FROM `Music`.album2songs a
group by a.genre_idx
order by count(a.genre_idx) desc;

select a.genre, count(a.genre)
FROM `Music`.album2songs a
group by a.genre
order by count(a.genre) desc;

/* project build normalized table */

/* Verify all album2songs songs in normalized table */

SELECT a.`index`,
       a.song,
       a.artist,
       a.album,
       a.path
  FROM `Music`.album2songs a
 WHERE a.`index` NOT IN (SELECT n.`song_idx`
                           FROM `Music`.normal_song n);
                           
SELECT sng.song as 'Song',
         sng.`index` as 'Song Index',
         art.`index` as 'Artist Index',
         alb.`index` as 'Album'
    FROM `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb
   WHERE sng.album = alb.album AND sng.artist = art.artist
ORDER BY art.`index`, alb.`index`, sng.`index`;

SELECT count(*)
  FROM `Music`.album2songs a
 WHERE a.`index` NOT IN (SELECT n.`song_idx`
                           FROM `Music`.normal_song n);

SELECT sng.song as 'Song',
         sng.`index` as 'Song Index',
         art.`index` as 'Artist Index',
         alb.`index` as 'Album'
    FROM `Music`.album2songs sng, `Music`.artist art, `Music`.artist_albums alb
   WHERE sng.album = alb.album AND sng.artist = art.artist
ORDER BY art.`index`, alb.`index`, sng.`index`;

SELECT a.song as 'song',
         a.`index` as 'song index',
         b.artist as 'artist',
         b.`index` as 'artist index',
         c.album as 'album',
         c.`index` as 'album index'
    FROM `Music`.album2songs a, `Music`.artist b, `Music`.artist_albums c
   WHERE a.album = c.album AND a.artist = b.artist
ORDER BY b.artist,c.album, a.song;


/* 
Collect songs under compilations artist name 
*/

SELECT *
  FROM music.album2songs
 WHERE music.album2songs.artist LIKE 'Compilations';


/*
Verify artist table and album table
*/

SELECT DISTINCT a.album,
                a.artist,
                a.genre,
                a.type
  FROM `Music`.album2songs a
 WHERE a.artist NOT IN (SELECT b.artist
                          FROM Music.artist b);
                    
SELECT DISTINCT a.album,
                a.artist,
                a.genre,
                a.type
  FROM `Music`.album2songs a
 WHERE a.album NOT IN (SELECT b.album
                          FROM `Music`.artist_albums b);


/*
sync artistalbum table to album2songs table
*/

SELECT b.album, b.`index`
 FROM `Music`.artist_albums b
 WHERE b.album NOT IN (SELECT a.album FROM `Music`.album2songs a)
 order by b.index;

SELECT count(*)
 FROM `Music`.artist_albums b
 WHERE b.album NOT IN (SELECT a.album FROM `Music`.album2songs a)
 order by b.album;

select count(distinct a.album) from `Music`.album2songs a;
-- 794

select count(distinct b.album) from `Music`.artist_albums b;
-- 794

select * from `Music`.artist_albums a where a.album like 'The Brecker Bothers';

select * from `Music`.album2songs a where a.album like 'The Brecker Bothers';

select * from `Music`.artist_albums a where a.`index` = 136;

delete from `Music`.artist_albums where `index` = 702;

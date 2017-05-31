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

select * from `Music`.artist_albums a WHERE a.type like 'Vinyl' and a.cover_name is NULL;

select * from `Music`.artist_albums a WHERE a.type like 'Vinyl' and a.artist like '%Brecker Brothers%';

select * from `Music`.artist_albums a WHERE a.artist like '%Brecker%';

select * from `Music`.artist_albums a WHERE a.`index` in (107,112,116);

delete from `Music`.artist_albums  WHERE `index` in (112,116);

select * from `Music`.album_covers a where a.album_cover like '%Brecker%';
 

select max(cover_idx) from `Music`.album_covers;

insert into `Music`.album_covers values ('Ace Frehley.jpg','',249,'');



select * from `Music`.artist_albums a where a.album like 'The Brecker Brothers';

update `Music`.album_covers set album_cover = 'The Brecker Brothers.jpg' where cover_idx = 248;




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

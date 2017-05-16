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

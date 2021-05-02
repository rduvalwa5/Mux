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

select distinct album from Music.`album2songs` where genre = "Classical" order by album;

select distinct type from Music.`album2songs`;

select * from genre;

CREATE TABLE `type` (
  `type` varchar(20) NOT NULL,
  `type_idx` bigint(5) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`type_idx`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

INSERT INTO type (type) VALUES ('Download');
INSERT INTO type (type) VALUES ('Vinyl');
INSERT INTO type (type) VALUES ('CD');
INSERT INTO type (type) VALUES ('Tape');
INSERT INTO type (type) VALUES ('TestType');

select * from type;

commit;

select * from artist;

select * from `artist_albums`;

update `artist_albums` set genre = 'Rock';


select a.artist, a.genre, b.`album`,b.genre from `artist`a, `artist_albums` b
where a.artist = b.artist;


UPDATE artist_albums
        INNER JOIN
    artist ON artist_albums.artist = artist.artist
SET 
    artist_albums.genre = artist.genre;




select album from album2songs;

UPDATE artist_albums
        INNER JOIN
    album2songs ON artist_albums.album =  album2songs.album
SET 
    artist_albums.type = album2songs.type;


select album from album2songs;

UPDATE artist_albums
        INNER JOIN
    album_covers ON artist_albums.`album` =  album_covers.`album`
SET 
    artist_albums.`cover_name` = album_covers.`album_cover`;
    
    
UPDATE artist_albums
        INNER JOIN
    album_covers ON artist_albums.`album` =  album_covers.`album`
SET 
    artist_albums.`cover_idx` = album_covers.`cover_idx`;
    
    

select * from artist_albums where `cover_name` not like 'iTunesImages.jpg';

select * from artist_albums where artist like 'Weather Report';


/* UPDATE employees
        INNER JOIN
    merits ON employees.performance = merits.performance 
SET 
    salary = salary + salary * percentage;  */


update `artist_albums` set type = 'Download' where type like 'download';

select * from artist where artist like '%Edith%';
select * from artist_albums where album like '%50%';

select * from album2songs where artist like '%Edith%';

select * from album_covers where album like '%Areo%';

select * from album_covers where `album_cover` like '%iTu%';

select * from artist_albums where cover_name = "iTunesImages.jpg" order by artist;

select count(*) from artist_albums where cover_name is not null order by artist;

update artist_albums 
set cover_name = "iTunesImages.jpg"
where cover_name is null;

update artist_albums 
set cover_idx = 842
where cover_name = "iTunesImages.jpg";



/* 842	iTunesImages.jpg	0	0 */

DELETE FROM artist_albums WHERE `index` = 874;


/* left off here 
400	Beethoven	Beethoven Concerto In D Major OP 61	Rock	Download	Beethoven_Yehudi_Menuhin.jpg	84
*/

select * from artist_albums where artist like '%Miles%';


select * from artist_albums where artist like '%Beatles%';

select * from artist_albums where artist like '%Jaco%' and cover_name = "iTunesImages.jpg";

select * from artist_albums where album like 'The Marshall Tucker Band_ Live On Long Island - 4-18-80';

delete from artist_albums where `index` = 808;

delete from album_covers where cover_idx = 8;

select * from album_covers where album_covers.`album_cover` like '%Heart%';

select * from `album_covers`;

select * from artist_albums where cover_name is null order by Artist; 

select * from artist_albums where cover_name is null order by Artist; 

select * from artist_albums where artist_albums.`cover_name` like 'EricClapton_The_Complete.jpg';



select * from album_covers;

select * from album2songs where album like '%Birthday%';
select * from album2songs where artist like '%Jaco%';

select * from artist_albums where artist like '%Compilations%' and artist_albums.`cover_name` is null;

select * from artist where artist like '%Jaco%';


select * from `artist_albums` where `artist_albums`.`cover_name` is null; 


select * from artist_albums where artist like  '%Alex Hargr%';

select * from artist_albums where artist like  'Alex Hargreavese';

select * from artist_albums where artist in ('Sarah McLachlan','Stray Birds','Freddy Fender','Strawberry Alarm Clock','Tina Turner','Johnny Mathis','Peter Bjorn and John','REO Speedwagon','The Honeycombs','Roy Orbison, The Ozark Mountain Daredevils');

commit;

UPDATE artist_albums
        INNER JOIN
    album_covers ON artist_albums.`album` =  album_covers.`album`
SET 
    artist_albums.`cover_name` = album_covers.`album_cover`;
    
    
UPDATE artist_albums
        INNER JOIN
    album_covers ON artist_albums.`album` =  album_covers.`album`
SET 
    artist_albums.`cover_idx` = album_covers.`cover_idx`;
    
    
select count(*) from artist_albums where `artist_albums`.`cover_name` is null;
select count(*) from artist_albums where `artist_albums`.`cover_name` is not null;

select artist, count(artist) from `artist_albums` group by artist order by count(artist) desc;

select * from `artist_albums` where artist like '.localized';

delete from `artist_albums` where artist like '.localized';

delete from `artist_albums` where `index` = 88;

select * from album2songs where album like 'The Music Inside_ A Collaboration Dedicated To Waylon Jennings, Volume II';

select * from album2songs where album like 'JACO Original Soundtrack' order by song;

delete from album2songs where album like 'JACO Original Soundtrack' and artist like 'Compilations';

commit;

select * from `album_covers` where album_cover like '%ELO%';

select * from `album_covers` where album like 'iTunesImages'

delete from `album_covers` where album like 'iTunesImages';

delete from `album_covers` where `cover_idx` in (1483,1482,213,214,215,216);

select * from `album_covers` order by `cover_idx`;

select * from `album_covers` where album like 'iTunesImages'



select count(*) from `artist_albums` where `artist_albums`.`cover_name` is null;  -- 97
select count(*) from `artist_albums` where `artist_albums`.`cover_name` is not null; -- 1145


select genre, count(genre) from album2songs group by genre order by count(genre) desc; 


select * from genre; 


select a.album, a.`cover_name`, a.`cover_idx`,b.`album_cover`, b.`cover_idx` from artist_albums a, `album_covers`b
where a.`album` = b.`album` 
and a.`cover_name` != b.`album_cover`;

UPDATE artist_albums
        INNER JOIN
    album_covers ON artist_albums.`album` =  album_covers.`album`
SET 
    artist_albums.`cover_idx` = album_covers.`cover_idx`;
    
UPDATE artist_albums
        INNER JOIN
    album_covers ON artist_albums.`album` =  album_covers.`album`
SET 
    artist_albums.`cover_name` = album_covers.`album_cover`;
    
commit;    

select * from artist_albums where artist like 'The Paul Butterfield Blues Band';

select * from artist_albums where album like 'Mono';

select * from album_covers where artist like '%ZZ%';

select * from album_covers where album like 'Mono'; 

select * from album_covers where `cover_idx` = 1409; 

delete from album_covers where cover_idx = 1546;

-- compare album2songs to artist albums 

select distinct a.`album`, a.artist  from album2songs a
where a.`album`  not in (select b.`album` from artist_albums b);

delete from album2songs where artist like '';

delete from album2songs where album like  '';

select * from album2songs where artist like 'Marianne Faithfull';

select * from album2songs where album like 'The Swinging Sixties: 15 Classic Tracks (Re-Recorded Versions)';

select * from artist_albums where artist like 'Asko Ensemble, Riccardo Chailly, Royal Concertgebouw Orchestra & Various Artists';



update album2songs set album = 'Supremes Gold [Disc 2]' where album like 'Gold [Disc 2]' and artist like 'The Supremes';

select * from album2songs where `index` > 12140; -- Lester Young With The Oscar Peterson Trio/Lester Young With The Oscar Peterson Trio

select * from artist where artist like  'Alvin Lee%'; -- Alison Krauss

/*
Alvin Lee & Ten Years Later
Alvin Lee & Company
Alvin Lee & Richard Newman
Alvin Lee & Mylon LeFevre 
Alvin Lee

*/

select album from music.artist_albums order by artist_albums.album;

delete from artist where `index` = 455;

delete from artist where artist like 'Unknown Artist';


select distinct artist from album2songs where artist like 'Alvin Lee%';

select * from album2songs where artist like 'Alvin Lee%';

update album2songs set artist = 'The Moody Blues' where artist = 'Moody Blues';

select * from artist where artist in ('Beck', 'Bob Marley & The Wailers', 'Buddy Tate', 'Dexter Gordon', 'Diego Garcia', 'Dolly Parton', 'Douglas Adams', 'Duke Ellington', 'Freddie Notes & the Rudies', 'Glasser', 'James Morrison', 'Jeremy Camp', 'Jerry Gonzalez & The Fort Apache Band', 'Jesse Thomas', 'Josh Rouse', 'Joshua Redman', 'Mannheim Steamroller', 'Matt Nathanson', 'Meat Loaf', 'Nine Black Alps', 'Noam Chomsky', 'Norah Jones', 'Philip Selway', 'S. Carey', 'Say Hi', 'The Coats', "Tim O'Brien", 'Unknown Artist', 'Vienna Teng', 'Wayne Shorter', 'Wayne Shorter Quartet', 'We Are Augustines', 'ZZ_ZTest')

delete from artist where artist in ('Beck', 'Bob Marley & The Wailers', 'Buddy Tate', 'Dexter Gordon', 'Diego Garcia', 'Dolly Parton', 'Douglas Adams', 'Duke Ellington', 'Freddie Notes & the Rudies', 'Glasser', 'James Morrison', 'Jeremy Camp', 'Jerry Gonzalez & The Fort Apache Band', 'Jesse Thomas', 'Josh Rouse', 'Joshua Redman', 'Mannheim Steamroller', 'Matt Nathanson', 'Meat Loaf', 'Nine Black Alps', 'Noam Chomsky', 'Norah Jones', 'Philip Selway', 'S. Carey', 'Say Hi', 'The Coats', "Tim O'Brien", 'Unknown Artist', 'Vienna Teng', 'Wayne Shorter', 'Wayne Shorter Quartet', 'We Are Augustines', 'ZZ_ZTest')


-- ['.localized', 'Asko Ensemble, Riccardo Chailly, Royal Concertgebouw Orchestra & Various Artists', 'Automatically Add to Music.localized', 'Bachman', 'Beethoven', 'Branford Marsalis Trio', 'Dave Matthews & Tim Reynolds', 'Devin Duval, Vishal Nayak, Daniel Rio', 'Don Cherry & John Coltrane', 'Doug Sahm', 'Emmylou Harris & Rodney Crowell', 'Freddie Notes & The Rudies', 'Gerry & The Pacemakers', 'Gustav Holst', 'Herb Albert', 'Herb Alpert & The Tijuana Brass', 'Ivan Shekov', 'Janos Sebestyen', 'Johann Strauss', 'Judy Collins & Ari Hest', 'Lloyd Price', 'London Philharmonic Orchestra', 'Lulu', 'Max Reger', "Miguel Zeno'n", 'R.E.M_', 'Stan Getz', 'TestArtist', 'The Bad Plus', 'The Black Keys', 'The Brothers Johnson', 'The Fortunes', 'The Grass Roots', 'Tim OBrien', 'Wayne Fontana', 'Wilbert Harrison', 'Woody Guthrie', 'conductor Neil Warner']


/* manual sync song genre to itunes *************************************************************************/
 
 /* alternative */
update artist set genre = 'Alternative'  where  artist in ('The Pretenders','Tom Waits','B.R.M.C','Red Hot Chili Peppers','Devo','Dirty Heads','The Black Keys','Pearl Jam','Mark O\'Connor','John Fahey & His Orchestra','Armik','The Belle Brigade','Yo La Tengo');
select * from artist where genre like 'Alternative';
update artist_albums set genre = 'Alternative'  where  artist in ('The Pretenders','Tom Waits','B.R.M.C','Red Hot Chili Peppers','Devo','Dirty Heads','The Black Keys','Pearl Jam','Mark O\'Connor','John Fahey & His Orchestra','Armik','The Belle Brigade','Yo La Tengo');
update album2songs set genre = 'Alternative' where  artist in ('The Pretenders','Tom Waits','B.R.M.C','Red Hot Chili Peppers','Devo','Dirty Heads','The Black Keys','Pearl Jam','Mark O\'Connor','John Fahey & His Orchestra','Armik','The Belle Brigade','Yo La Tengo');
select * from album2songs where  artist in ('The Pretenders','Tom Waits','B.R.M.C','Red Hot Chili Peppers','Devo','Dirty Heads','The Black Keys','Pearl Jam','Mark O\'Connor','John Fahey & His Orchestra','Armik','The Belle Brigade','Yo La Tengo');
select distinct artist from album2songs where genre = 'Alternative';
/* alternative End */

/* Blue Grass Start */
update artist set genre = 'Blue Grass'   where  artist in  ('Tim OBrien','The Chieftains','Sarah Jarosz','Infamous Stringdusters','Mountain Heart','Crooked Still','Uncle Earl','Walela');
select * from artist where genre like 'Blue Grass';
update artist_albums set genre = 'Blue Grass' where artist in ('Tim OBrien','The Chieftains','Sarah Jarosz','Infamous Stringdusters','Mountain Heart','Crooked Still','Uncle Earl','Walela');
select * from artist_albums where  artist in ('Tim OBrien','The Chieftains','Sarah Jarosz','Infamous Stringdusters','Mountain Heart','Crooked Still','Uncle Earl','Walela');
select * from artist_albums where artist in ('Tim OBrien','The Chieftains','Sarah Jarosz','Infamous Stringdusters','Mountain Heart','Crooked Still','Uncle Earl','Walela');
update album2songs set genre = 'Blue Grass' where  artist in  ('Tim OBrien','The Chieftains','Sarah Jarosz','Infamous Stringdusters','Mountain Heart','Crooked Still','Uncle Earl','Walela');
select * from album2songs where  artist in ('Tim OBrien','The Chieftains','Sarah Jarosz','Infamous Stringdusters','Mountain Heart','Crooked Still','Uncle Earl','Walela');
select distinct artist from album2songs where genre = 'Blue Grass' order by artist;
/* Blue Grass End */

/* Reggae Start */
update artist set genre = 'Reggae' where  artist in ('Desmond Dekker','Bob Marley','Amazula','Freddie Notes & The Rudies');
select * from artist where genre like 'Reggae';
update artist_albums set genre = 'Reggae' where  artist in ('Desmond Dekker','Bob Marley','Amazula','Freddie Notes & The Rudies');
select * from artist_albums where genre like 'Reggae';
update album2songs set genre = 'Reggae' where  artist in  ('Desmond Dekker','Bob Marley','Amazula','Freddie Notes & The Rudies');
select * from album2songs where genre like 'Reggae';
select distinct artist from album2songs where genre = 'Reggae' order by artist;

/* Reggae End */

/* Rockabilly Start */
update album2songs set genre = 'Rockabilly' where  artist in ('Buddy Holly	','Carl Perkins','Jerry Lee Lewis','Bill Haley & His Comets','Dale Hawkins','Billy Lee Riley');
select * from artist where genre like 'Rockabilly';
select * from artist_albums where genre like 'Rockabilly';
select count(*) from `album2songs` where artist in ('Buddy Holly','Carl Perkins','Jerry Lee Lewis','Bill Haley & His Comets','Dale Hawkins','Billy Lee Riley');
select count(*) from `album2songs` where genre like 'Rockabilly';
select distinct artist from album2songs where genre = 'Rockabilly' order by artist;
/* Rockabilly End */

/* R&B */

update artist set genre = 'R&B' where  artist in ('Tower of Power','Bill Withers','Al Green','The Chi-Lites','The Spinners','Otis Redding','Earth, Wind & Fire','The 5th Dimension','The Isley Brothers','Teddy Pendergrass','Wilson Pickett','Roberta Flack','Gladys Knight & The Pips','The Supremes','Aloe Blacc','Aretha Franklin','Booker T. & The MG\'s','Isaac Hayes','Roberta Flack','Marvin Gaye','The Temptations','Mavis Staples','Roberta Flack & Donny Hathaway','Martha Reeves & The Vandellas','Ben E. King','The Coasters','Ike and Tina Turner','The Four Tops','Mavis Staples','James Brown');
select * from artist where genre like 'R&B';
update artist_albums set genre = 'R&B' where  artist in ('Tower of Power','Bill Withers','Al Green','The Chi-Lites','The Spinners','Otis Redding','Earth, Wind & Fire','The 5th Dimension','The Isley Brothers','Teddy Pendergrass','Wilson Pickett','Roberta Flack','Gladys Knight & The Pips','The Supremes','Aloe Blacc','Aretha Franklin','Booker T. & The MG\'s','Isaac Hayes','Roberta Flack','Marvin Gaye','The Temptations','Mavis Staples','Roberta Flack & Donny Hathaway','Martha Reeves & The Vandellas','Ben E. King','The Coasters','Ike and Tina Turner','The Four Tops','Mavis Staples','James Brown');
select * from artist_albums where genre like 'R&B';
update album2songs set genre = 'R&B' where  artist in  ('Tower of Power','Bill Withers','Al Green','The Chi-Lites','The Spinners','Otis Redding','Earth, Wind & Fire','The 5th Dimension','The Isley Brothers','Teddy Pendergrass','Wilson Pickett','Roberta Flack','Gladys Knight & The Pips','The Supremes','Aloe Blacc','Aretha Franklin','Booker T. & The MG\'s','Isaac Hayes','Roberta Flack','Marvin Gaye','The Temptations','Mavis Staples','Roberta Flack & Donny Hathaway','Martha Reeves & The Vandellas','Ben E. King','The Coasters','Ike and Tina Turner','The Four Tops','Mavis Staples','James Brown');
select * from album2songs where artist in  ('Tower of Power','Bill Withers','Al Green','The Chi-Lites','The Spinners','Otis Redding','Earth, Wind & Fire','The 5th Dimension','The Isley Brothers','Teddy Pendergrass','Wilson Pickett','Roberta Flack','Gladys Knight & The Pips','The Supremes','Aloe Blacc','Aretha Franklin','Booker T. & The MG\'s','Isaac Hayes','Roberta Flack','Marvin Gaye','The Temptations','Mavis Staples','Roberta Flack & Donny Hathaway','Martha Reeves & The Vandellas','Ben E. King','The Coasters','Ike and Tina Turner','The Four Tops','Mavis Staples','James Brown');
select distinct artist from `album2songs` where genre like 'R&B' order by artist;
/* R&B End */
/* Soundtrack Start By album */
update `artist_albums` set genre = 'Soundtrack' where  album in ('The Departed','Easy Rider (Soundtrack from the Motion Picture) [Deluxe Edition]','Hair','I\'m Not There [Disc 1]','I\'m Not There [Disc 2]','Man Of La Mancha','Masked & Anonymous','2001 A Space Odyssey');
select * from `artist_albums` where genre like 'Soundtrack';
update `album2songs` set genre = 'Soundtrack' where  album in ('The Departed','Easy Rider (Soundtrack from the Motion Picture) [Deluxe Edition]','Hair','I\'m Not There [Disc 1]','I\'m Not There [Disc 2]','Man Of La Mancha','Masked & Anonymous','2001 A Space Odyssey');
select distinct Album from `album2songs` where genre like 'Soundtrack';
select * from `album2songs` where album like 'The Departed';
/* Soundtrack End */
/* Classical */
update artist set genre = 'Classical' where  artist in ('Antonio Vivaldi','Janos Sebestyen','Beethoven','Wagner','A Fielder Boston Pops','Alfred Hause And His Vienna Waltz Country Ballroom Orchestra','Branford Marsalis & Orpheus Chamber Orchestra','London Philharmonic Orchestra','Dvorak','Stravinsky','The Tennesse Waltz/Keep The Old Ark Rolling','Angele Dubeau & La Pieta','Max Reger','Ivan Shekov','Schubert','Mozart','Tchaikovsky','Gustav Holst','Ravel','Oliver Kane','Johann Strauss','Andre Kostelanetz and his orchestra','Alacran','Asko Ensemble, Riccardo Chailly, Royal Concertgebouw Orchestra & Various Artists','Wagner','London Philharmonic Orchestra & David Parry','Stanley Kubrick');
select * from artist where genre like 'Classical';
update artist_albums set genre = 'Classical' where  artist in ('Antonio Vivaldi','Janos Sebestyen','Beethoven','Wagner','A Fielder Boston Pops','Alfred Hause And His Vienna Waltz Country Ballroom Orchestra','Branford Marsalis & Orpheus Chamber Orchestra','London Philharmonic Orchestra','Dvorak','Stravinsky','The Tennesse Waltz/Keep The Old Ark Rolling','Angele Dubeau & La Pieta','Max Reger','Ivan Shekov','Schubert','Mozart','Tchaikovsky','Gustav Holst','Ravel','Oliver Kane','Johann Strauss','Andre Kostelanetz and his orchestra','Alacran','Asko Ensemble, Riccardo Chailly, Royal Concertgebouw Orchestra & Various Artists','Wagner','London Philharmonic Orchestra & David Parry','Stanley Kubrick');
select * from artist_albums where genre like 'Classical';
update album2songs set genre = 'Classical' where  artist in ('Antonio Vivaldi','Janos Sebestyen','Beethoven','Wagner','A Fielder Boston Pops','Alfred Hause And His Vienna Waltz Country Ballroom Orchestra','Branford Marsalis & Orpheus Chamber Orchestra','London Philharmonic Orchestra','Dvorak','Stravinsky','The Tennesse Waltz/Keep The Old Ark Rolling','Angele Dubeau & La Pieta','Max Reger','Ivan Shekov','Schubert','Mozart','Tchaikovsky','Gustav Holst','Ravel','Oliver Kane','Johann Strauss','Andre Kostelanetz and his orchestra','Alacran','Asko Ensemble, Riccardo Chailly, Royal Concertgebouw Orchestra & Various Artists','Wagner','London Philharmonic Orchestra & David Parry','Stanley Kubrick');
select count(*) from album2songs where artist in  ('Antonio Vivaldi','Janos Sebestyen','Beethoven','Wagner','A Fielder Boston Pops','Alfred Hause And His Vienna Waltz Country Ballroom Orchestra','Branford Marsalis & Orpheus Chamber Orchestra','London Philharmonic Orchestra','Dvorak','Stravinsky','The Tennesse Waltz/Keep The Old Ark Rolling','Angele Dubeau & La Pieta','Max Reger','Ivan Shekov','Schubert','Mozart','Tchaikovsky','Gustav Holst','Ravel','Oliver Kane','Johann Strauss','Andre Kostelanetz and his orchestra','Alacran','Asko Ensemble, Riccardo Chailly, Royal Concertgebouw Orchestra & Various Artists','Wagner','London Philharmonic Orchestra & David Parry','Stanley Kubrick');
select count(*) from album2songs where genre = 'Classical';
select distinct artist from album2songs where genre = 'Classical' order by artist;

update album2songs set artist = 'London Philharmonic Orchestra & David Parry' where album like 'The 50 Greatest Pieces of Classical Music';
/* Classical End */

/* Blues */
select distinct artist from album2songs where genre like 'Blues' order by artist;

update artist set genre = 'Blues' where  artist in ('18 South','Alvin Lee','Alvin Lee & Company','Alvin Lee & Mylon LeFevre ','Alvin Lee & Richard Newman','Alvin Lee & Ten Years Later','B.B. King','Billie Holiday','Billy Holliday','Bob Forrest','Clarence Gatermouth Brown','Cream','Eric Clapton','Eric Clapton & B.B. King','Gregg Allman','Hot Tuna','John Lee Hooker','John Mayall','John Mayall & The Bluesbreakers','Johnny Winter','Muddy Waters','North Mississippi Allstars','Percy Sledge','R.L. Burnside','Richie Havens','Savoy Brown','Stevie Ray Vaughan','Stevie Ray Vaughan & Double Trouble','Ten Years After','The Paul Butterfield Blues Band','The Yardbirds','Canned Heat','Jimmy Witherspoon','The Doors','Joe Louis Walker','Eric Clapton & Steve Winwood','Wynton Marsalis & Eric Clapton','Bachman');
select * from artist where genre like 'Blues';
update artist_albums set genre = 'Blues' where  artist in ('18 South','Alvin Lee','Alvin Lee & Company','Alvin Lee & Mylon LeFevre ','Alvin Lee & Richard Newman','Alvin Lee & Ten Years Later','B.B. King','Billie Holiday','Billy Holliday','Bob Forrest','Clarence Gatermouth Brown','Cream','Eric Clapton','Eric Clapton & B.B. King','Gregg Allman','Hot Tuna','John Lee Hooker','John Mayall','John Mayall & The Bluesbreakers','Johnny Winter','Muddy Waters','North Mississippi Allstars','Percy Sledge','R.L. Burnside','Richie Havens','Savoy Brown','Stevie Ray Vaughan','Stevie Ray Vaughan & Double Trouble','Ten Years After','The Paul Butterfield Blues Band','The Yardbirds','Canned Heat','Jimmy Witherspoon','The Doors','Joe Louis Walker','Eric Clapton & Steve Winwood','Wynton Marsalis & Eric Clapton','Bachman');
select * from artist_albums where genre like 'Blues';
update album2songs set genre = 'Blues' where  artist in ('18 South','Alvin Lee','Alvin Lee & Company','Alvin Lee & Mylon LeFevre ','Alvin Lee & Richard Newman','Alvin Lee & Ten Years Later','B.B. King','Billie Holiday','Billy Holliday','Bob Forrest','Clarence Gatermouth Brown','Cream','Eric Clapton','Eric Clapton & B.B. King','Gregg Allman','Hot Tuna','John Lee Hooker','John Mayall','John Mayall & The Bluesbreakers','Johnny Winter','Muddy Waters','North Mississippi Allstars','Percy Sledge','R.L. Burnside','Richie Havens','Savoy Brown','Stevie Ray Vaughan','Stevie Ray Vaughan & Double Trouble','Ten Years After','The Paul Butterfield Blues Band','The Yardbirds','Canned Heat','Jimmy Witherspoon','The Doors','Joe Louis Walker','Eric Clapton & Steve Winwood','Wynton Marsalis & Eric Clapton','Bachman');
select * from album2songs where artist in ('18 South','Alvin Lee','Alvin Lee & Company','Alvin Lee & Mylon LeFevre ','Alvin Lee & Richard Newman','Alvin Lee & Ten Years Later','B.B. King','Billie Holiday','Billy Holliday','Bob Forrest','Clarence Gatermouth Brown','Cream','Eric Clapton','Eric Clapton & B.B. King','Gregg Allman','Hot Tuna','John Lee Hooker','John Mayall','John Mayall & The Bluesbreakers','Johnny Winter','Muddy Waters','North Mississippi Allstars','Percy Sledge','R.L. Burnside','Richie Havens','Savoy Brown','Stevie Ray Vaughan','Stevie Ray Vaughan & Double Trouble','Ten Years After','The Paul Butterfield Blues Band','The Yardbirds','Canned Heat','Jimmy Witherspoon','The Doors','Joe Louis Walker','Eric Clapton & Steve Winwood','Wynton Marsalis & Eric Clapton','Bachman');

select * from `artist_albums` where album like '%Blues%';
select * from `album2songs` where album like 'Blues Selects';
select * from `artist_albums` where album like 'Blues Selects';

/* Blues End */

/* Rock Start */

select distinct artist from album2songs where genre like 'Rock' order by artist;

update artist set genre = 'Rock' where  artist in ('Rock','38 Special','Ace Frehley','AC_DC','Aerosmith','Alice Cooper','America','Average White Band','Bachman-Turner Overdrive','Bad Company','Badfinger','Ben Harper','Big Brother & the Holding Company_Janis Joplin','Bill Perry','Billy Joel','BJ Thomas','Black Sabbath','Blackfoot','Blind Faith','Blondie','Blood Sweat & Tears','Blue Cheer','Blue Oyster Cult','Blue Swede','Blues Image','Bob Seger','Bobby Darin','Bobby Rydell','Bon Jovi','Booker T. Jones','Boston','Boz Scaggs','Bread','Brewer & Shipley','Bruce Springsteen','Bruce Springsteen & The E Street Band','Buffalo Springfield','Carole King','Cat Stevens','Chad & Jeremy','Cheap Trick','Chicago','Chris Robinson Brotherhood','Chuck Berry','Citizen Cope','City and Colour','Commander Cody & His Lost Planet Airmen','Creedence Clearwater Revival','Crosby, Stills, Nash & Young','Dave Dee, Dozy, Beaky, Mick & Tich','Dave Edmunds','Dave Mason','Dave Matthews Band','David Allan Coe','David Bowie','David Bromberg Band','Deep Purple','Dick Dale & His Del-Tones','Dire Straits','Don McLean','Donovan','Doobie Brothers','Dr. John','Drive-By Truckers','Dropkick Murphys','Duran Duran','Eagles','Eddie Vedder','Edgar Winter','Electric Light Orchestra','Elton John','Elvin Bishop','Elvis Costello','Elvis Presley','Emerson, Lake & Palmer','Faces','Fleet Foxes','Fleetwood Mac','Foghat','Genesis','George Baker','George Harrison','Gerry & The Pacemakers','Gerry Rafferty','Gillian Welch','Golden Earring','Grand Funk Railroad','Grateful Dead','Guns N\' Roses','Harry Nilsson','Heart','Herman\'s Hermits','Huey Lewis & The News','Humble Pie','Ian Anderson','Iggy & The Stooges','Iron & Wine','Iron Butterfly','Iron Butterfly & Vanilla Fudge','J. J. Cale With Leon Russell','J.J. Cale','J.J. Cale & Eric Clapton','James Gang','Jan & Dean','Janis Joplin','Jason Isbell & The 400 Unit','Jeff Beck','Jefferson Airplane','Jerry Garcia Band','Jethro Tull','Jim Croce','Jimi Hendrix','Joe Cocker','Joe Walsh','John Fogerty','John Lennon','John Mellencamp','Johnny Nash','Johnny Rivers','Journey','Kansas','Keith Richards','Keith Urban','Kenny Rogers & The First Edition','Kiss','Led Zeppelin','Lenny Kravitz','Leonard Cohen','Linda Ronstadt','Linkin Park','Little Dragon','Little Feat','Little Richard','Little River Band','Loggins And Messina','Los Bravos','Los Lobos','Lou Reed','Lovin Spoonful','Lynyrd Skynyrd','Mark Knopfler','Mark Knopfler & Emmylou Harris','Mark Knopfler_Emmylou Harris','Mason Williams','Meat Loaf','Men At Work','Mitch Ryder & The Detroit Wheels','Motley Crue','Motorhead','Mungo Jerry','Nashville Teens','Neil Diamond','Neil Young','Neil Young & Crazy Horse','Neko Case','New Riders of the Purple Sage','Nirvana','Nitty Gritty Dirt Band','Patti Smith','Paul McCartney & Wings','Pete Segear Arlo Guthrie','Pete Townshend & Ronnie Lane','Peter & Gordon','Pink Floyd','Poco','Prince','Procol Harum','Queen','Queenryche','R.E.M.','Radiohead','Ram Jam','REO Speedwagon','Ricketic','Ringo Starr','Ritchie Valens','Robert Plant','Rod Stewart','Rodriguez','Roy Orbison','Rush','Santo And Johnny','Seals & Crofts','Simon & Garfunkel','Small Faces','Sonny & Cher','Spanky & Our Gang','Stealers Wheel','Steely Dan','Steppenwolf','Steve Miller Band','Sting & The Police','Strawberry Alarm Clock','Stray Cats','Styx','Supertramp','T. Rex','The 5.6.7.8\'s','The Allman Brothers Band','The Amazing Rhythm Aces','The Animals','The B-52\'s','The Band','The Beach Boys','The Beatles','The Byrds','The Cars','The Centurions','The Dave Clark Five','The Diamonds','The Dickey Betts Band','The Doobie Brothers','The Electric Prunes','The Everly Brothers','The Georgia Satellites','The Grass Roots','The Guess Who','The Hollies','The Kingsmen','The Kinks','The Knack','The Left Banke','The Marshall Tucker Band','The Monkees','The Moody Blues','The Outlaws','The Ozark Mountain Daredevils','The Pointer Sisters','The Police','The Righteous Brothers','The Rolling Stones','The Searchers','The Seeds','The Shadows','The Sonics','The Soundtrack Studio Stars','The Spencer Davis Group','The Stooges','The Surfaris','The Sweet','The Tokens','The Traveling Wilburys','The Tremeloes','The Troggs','The Turtles','The Ventures','The Who','The Who At Filllmore East 1968','The Young Rascals','The Youngbloods','The Zombies','Them','Thin Lizzy','Three Dog Night','Tina Turner','Tom Jones','Tom Petty & The Heartbreakers','Tommy James & The Shondells','Toto','Traffic','Traveling Wilburys','Triumph','U2','Union Gap','Van Morrison','War','Wayne Fontana & The Mindbenders','White Lion','Yes','ZZ Top','_ & The Mysterians','Alligator Stew','The Box Tops','The Brothers Johnson','Arcade Fire','Billy J. Kramer');
select * from artist where genre like 'Rock';
update artist_albums set genre = 'Rock' where  artist in  ('Rock','38 Special','Ace Frehley','AC_DC','Aerosmith','Alice Cooper','America','Average White Band','Bachman-Turner Overdrive','Bad Company','Badfinger','Ben Harper','Big Brother & the Holding Company_Janis Joplin','Bill Perry','Billy Joel','BJ Thomas','Black Sabbath','Blackfoot','Blind Faith','Blondie','Blood Sweat & Tears','Blue Cheer','Blue Oyster Cult','Blue Swede','Blues Image','Bob Seger','Bobby Darin','Bobby Rydell','Bon Jovi','Booker T. Jones','Boston','Boz Scaggs','Bread','Brewer & Shipley','Bruce Springsteen','Bruce Springsteen & The E Street Band','Buffalo Springfield','Carole King','Cat Stevens','Chad & Jeremy','Cheap Trick','Chicago','Chris Robinson Brotherhood','Chuck Berry','Citizen Cope','City and Colour','Commander Cody & His Lost Planet Airmen','Creedence Clearwater Revival','Crosby, Stills, Nash & Young','Dave Dee, Dozy, Beaky, Mick & Tich','Dave Edmunds','Dave Mason','Dave Matthews Band','David Allan Coe','David Bowie','David Bromberg Band','Deep Purple','Dick Dale & His Del-Tones','Dire Straits','Don McLean','Donovan','Doobie Brothers','Dr. John','Drive-By Truckers','Dropkick Murphys','Duran Duran','Eagles','Eddie Vedder','Edgar Winter','Electric Light Orchestra','Elton John','Elvin Bishop','Elvis Costello','Elvis Presley','Emerson, Lake & Palmer','Faces','Fleet Foxes','Fleetwood Mac','Foghat','Genesis','George Baker','George Harrison','Gerry & The Pacemakers','Gerry Rafferty','Gillian Welch','Golden Earring','Grand Funk Railroad','Grateful Dead','Guns N\' Roses','Harry Nilsson','Heart','Herman\'s Hermits','Huey Lewis & The News','Humble Pie','Ian Anderson','Iggy & The Stooges','Iron & Wine','Iron Butterfly','Iron Butterfly & Vanilla Fudge','J. J. Cale With Leon Russell','J.J. Cale','J.J. Cale & Eric Clapton','James Gang','Jan & Dean','Janis Joplin','Jason Isbell & The 400 Unit','Jeff Beck','Jefferson Airplane','Jerry Garcia Band','Jethro Tull','Jim Croce','Jimi Hendrix','Joe Cocker','Joe Walsh','John Fogerty','John Lennon','John Mellencamp','Johnny Nash','Johnny Rivers','Journey','Kansas','Keith Richards','Keith Urban','Kenny Rogers & The First Edition','Kiss','Led Zeppelin','Lenny Kravitz','Leonard Cohen','Linda Ronstadt','Linkin Park','Little Dragon','Little Feat','Little Richard','Little River Band','Loggins And Messina','Los Bravos','Los Lobos','Lou Reed','Lovin Spoonful','Lynyrd Skynyrd','Mark Knopfler','Mark Knopfler & Emmylou Harris','Mark Knopfler_Emmylou Harris','Mason Williams','Meat Loaf','Men At Work','Mitch Ryder & The Detroit Wheels','Motley Crue','Motorhead','Mungo Jerry','Nashville Teens','Neil Diamond','Neil Young','Neil Young & Crazy Horse','Neko Case','New Riders of the Purple Sage','Nirvana','Nitty Gritty Dirt Band','Patti Smith','Paul McCartney & Wings','Pete Segear Arlo Guthrie','Pete Townshend & Ronnie Lane','Peter & Gordon','Pink Floyd','Poco','Prince','Procol Harum','Queen','Queenryche','R.E.M.','Radiohead','Ram Jam','REO Speedwagon','Ricketic','Ringo Starr','Ritchie Valens','Robert Plant','Rod Stewart','Rodriguez','Roy Orbison','Rush','Santo And Johnny','Seals & Crofts','Simon & Garfunkel','Small Faces','Sonny & Cher','Spanky & Our Gang','Stealers Wheel','Steely Dan','Steppenwolf','Steve Miller Band','Sting & The Police','Strawberry Alarm Clock','Stray Cats','Styx','Supertramp','T. Rex','The 5.6.7.8\'s','The Allman Brothers Band','The Amazing Rhythm Aces','The Animals','The B-52\'s','The Band','The Beach Boys','The Beatles','The Byrds','The Cars','The Centurions','The Dave Clark Five','The Diamonds','The Dickey Betts Band','The Doobie Brothers','The Electric Prunes','The Everly Brothers','The Georgia Satellites','The Grass Roots','The Guess Who','The Hollies','The Kingsmen','The Kinks','The Knack','The Left Banke','The Marshall Tucker Band','The Monkees','The Moody Blues','The Outlaws','The Ozark Mountain Daredevils','The Pointer Sisters','The Police','The Righteous Brothers','The Rolling Stones','The Searchers','The Seeds','The Shadows','The Sonics','The Soundtrack Studio Stars','The Spencer Davis Group','The Stooges','The Surfaris','The Sweet','The Tokens','The Traveling Wilburys','The Tremeloes','The Troggs','The Turtles','The Ventures','The Who','The Who At Filllmore East 1968','The Young Rascals','The Youngbloods','The Zombies','Them','Thin Lizzy','Three Dog Night','Tina Turner','Tom Jones','Tom Petty & The Heartbreakers','Tommy James & The Shondells','Toto','Traffic','Traveling Wilburys','Triumph','U2','Union Gap','Van Morrison','War','Wayne Fontana & The Mindbenders','White Lion','Yes','ZZ Top','_ & The Mysterians');
select * from artist_albums where genre like 'Rock';
update album2songs set genre = 'Rock' where  artist in  ('Rock','38 Special','Ace Frehley','AC_DC','Aerosmith','Alice Cooper','America','Average White Band','Bachman-Turner Overdrive','Bad Company','Badfinger','Ben Harper','Big Brother & the Holding Company_Janis Joplin','Bill Perry','Billy Joel','BJ Thomas','Black Sabbath','Blackfoot','Blind Faith','Blondie','Blood Sweat & Tears','Blue Cheer','Blue Oyster Cult','Blue Swede','Blues Image','Bob Seger','Bobby Darin','Bobby Rydell','Bon Jovi','Booker T. Jones','Boston','Boz Scaggs','Bread','Brewer & Shipley','Bruce Springsteen','Bruce Springsteen & The E Street Band','Buffalo Springfield','Carole King','Cat Stevens','Chad & Jeremy','Cheap Trick','Chicago','Chris Robinson Brotherhood','Chuck Berry','Citizen Cope','City and Colour','Commander Cody & His Lost Planet Airmen','Creedence Clearwater Revival','Crosby, Stills, Nash & Young','Dave Dee, Dozy, Beaky, Mick & Tich','Dave Edmunds','Dave Mason','Dave Matthews Band','David Allan Coe','David Bowie','David Bromberg Band','Deep Purple','Dick Dale & His Del-Tones','Dire Straits','Don McLean','Donovan','Doobie Brothers','Dr. John','Drive-By Truckers','Dropkick Murphys','Duran Duran','Eagles','Eddie Vedder','Edgar Winter','Electric Light Orchestra','Elton John','Elvin Bishop','Elvis Costello','Elvis Presley','Emerson, Lake & Palmer','Faces','Fleet Foxes','Fleetwood Mac','Foghat','Genesis','George Baker','George Harrison','Gerry & The Pacemakers','Gerry Rafferty','Gillian Welch','Golden Earring','Grand Funk Railroad','Grateful Dead','Guns N\' Roses','Harry Nilsson','Heart','Herman\'s Hermits','Huey Lewis & The News','Humble Pie','Ian Anderson','Iggy & The Stooges','Iron & Wine','Iron Butterfly','Iron Butterfly & Vanilla Fudge','J. J. Cale With Leon Russell','J.J. Cale','J.J. Cale & Eric Clapton','James Gang','Jan & Dean','Janis Joplin','Jason Isbell & The 400 Unit','Jeff Beck','Jefferson Airplane','Jerry Garcia Band','Jethro Tull','Jim Croce','Jimi Hendrix','Joe Cocker','Joe Walsh','John Fogerty','John Lennon','John Mellencamp','Johnny Nash','Johnny Rivers','Journey','Kansas','Keith Richards','Keith Urban','Kenny Rogers & The First Edition','Kiss','Led Zeppelin','Lenny Kravitz','Leonard Cohen','Linda Ronstadt','Linkin Park','Little Dragon','Little Feat','Little Richard','Little River Band','Loggins And Messina','Los Bravos','Los Lobos','Lou Reed','Lovin Spoonful','Lynyrd Skynyrd','Mark Knopfler','Mark Knopfler & Emmylou Harris','Mark Knopfler_Emmylou Harris','Mason Williams','Meat Loaf','Men At Work','Mitch Ryder & The Detroit Wheels','Motley Crue','Motorhead','Mungo Jerry','Nashville Teens','Neil Diamond','Neil Young','Neil Young & Crazy Horse','Neko Case','New Riders of the Purple Sage','Nirvana','Nitty Gritty Dirt Band','Patti Smith','Paul McCartney & Wings','Pete Segear Arlo Guthrie','Pete Townshend & Ronnie Lane','Peter & Gordon','Pink Floyd','Poco','Prince','Procol Harum','Queen','Queenryche','R.E.M.','Radiohead','Ram Jam','REO Speedwagon','Ricketic','Ringo Starr','Ritchie Valens','Robert Plant','Rod Stewart','Rodriguez','Roy Orbison','Rush','Santo And Johnny','Seals & Crofts','Simon & Garfunkel','Small Faces','Sonny & Cher','Spanky & Our Gang','Stealers Wheel','Steely Dan','Steppenwolf','Steve Miller Band','Sting & The Police','Strawberry Alarm Clock','Stray Cats','Styx','Supertramp','T. Rex','The 5.6.7.8\'s','The Allman Brothers Band','The Amazing Rhythm Aces','The Animals','The B-52\'s','The Band','The Beach Boys','The Beatles','The Byrds','The Cars','The Centurions','The Dave Clark Five','The Diamonds','The Dickey Betts Band','The Doobie Brothers','The Electric Prunes','The Everly Brothers','The Georgia Satellites','The Grass Roots','The Guess Who','The Hollies','The Kingsmen','The Kinks','The Knack','The Left Banke','The Marshall Tucker Band','The Monkees','The Moody Blues','The Outlaws','The Ozark Mountain Daredevils','The Pointer Sisters','The Police','The Righteous Brothers','The Rolling Stones','The Searchers','The Seeds','The Shadows','The Sonics','The Soundtrack Studio Stars','The Spencer Davis Group','The Stooges','The Surfaris','The Sweet','The Tokens','The Traveling Wilburys','The Tremeloes','The Troggs','The Turtles','The Ventures','The Who','The Who At Filllmore East 1968','The Young Rascals','The Youngbloods','The Zombies','Them','Thin Lizzy','Three Dog Night','Tina Turner','Tom Jones','Tom Petty & The Heartbreakers','Tommy James & The Shondells','Toto','Traffic','Traveling Wilburys','Triumph','U2','Union Gap','Van Morrison','War','Wayne Fontana & The Mindbenders','White Lion','Yes','ZZ Top','_ & The Mysterians');
select count(*) from album2songs where genre = 'Rock';

select * from album2songs where artist like '%Allman Brothers%';

/* Rock End */

/* Country Start */

select distinct artist from album2songs where genre like 'Rock' order by artist;

update artist set genre = 'Country' where  artist in ('Alabama','Alison Krauss','Alison Krauss & Union Station','Bill Monroe','Boxcar Willie','Brenda Lee','Charlie Rich','Chet Atkins and Hank Snow','Cody Bryant and The Riders Of The Purple Sage','David Allan Coe','Della Mae','Dierks Bentley','Dixie Chicks','Dolly Parton, Linda Ronstadt & Emmylou Harris','Eilen Jewell','Emmylou Harris','Emmylou Harris & Rodney Crowell','Eric Church','Florida Georgia Line','Foy Willing & The Riders Of The Purple Sage','Hank Williams','Jerry Jeff Walker','Jewel','Jimmy Buffet','Jo Dee Messina','John Denver','John Prine','Johnny Cash','Kenny Rogers','Kris Kristofferson','Linda Ronstadt','Linda Ronstadt & Emmylou Harris','Lonestar','Lori McKenna','Lynyrd Skynyrd','Marty Robbins','Michael Martin Murphey','Old Crow Medicine Show','Olivia Newton-John','Pat Benatar','Patsy Cline','Polecat','Prairie Flyer','Redbird','Rita Coolidge','Robert Plant & Alison Krauss','Stray Birds','The Charlie Daniels Band','The Handsome Family','Waylon and Willie','Waylon Jennings','Waylon Jennings & The Waylors','Waylon Jennings & Willie Nelson','Willie Nelson and Leon Russel','Zac Brown Band','Judy Collins & Ari Hest','Keith Urban ','The Marshall Tucker Band','Nitty Gritty Dirt Band');
select * from artist where genre like 'Country' order by artist;
update artist_albums set genre = 'Country' where  artist in  ('Alabama','Alison Krauss','Alison Krauss & Union Station','Bill Monroe','Boxcar Willie','Brenda Lee','Charlie Rich','Chet Atkins and Hank Snow','Cody Bryant and The Riders Of The Purple Sage','David Allan Coe','Della Mae','Dierks Bentley','Dixie Chicks','Dolly Parton, Linda Ronstadt & Emmylou Harris','Eilen Jewell','Emmylou Harris','Emmylou Harris & Rodney Crowell','Eric Church','Florida Georgia Line','Foy Willing & The Riders Of The Purple Sage','Hank Williams','Jerry Jeff Walker','Jewel','Jimmy Buffet','Jo Dee Messina','John Denver','John Prine','Johnny Cash','Kenny Rogers','Kris Kristofferson','Linda Ronstadt','Linda Ronstadt & Emmylou Harris','Lonestar','Lori McKenna','Lynyrd Skynyrd','Marty Robbins','Michael Martin Murphey','Old Crow Medicine Show','Olivia Newton-John','Pat Benatar','Patsy Cline','Polecat','Prairie Flyer','Redbird','Rita Coolidge','Robert Plant & Alison Krauss','Stray Birds','The Charlie Daniels Band','The Handsome Family','Waylon and Willie','Waylon Jennings','Waylon Jennings & The Waylors','Waylon Jennings & Willie Nelson','Willie Nelson and Leon Russel','Zac Brown Band','Judy Collins & Ari Hest','Keith Urban ','The Marshall Tucker Band','Nitty Gritty Dirt Band');
select * from artist_albums where genre like 'Country' order by artist;
update album2songs set genre = 'Country' where  artist in  ('Alabama','Alison Krauss','Alison Krauss & Union Station','Bill Monroe','Boxcar Willie','Brenda Lee','Charlie Rich','Chet Atkins and Hank Snow','Cody Bryant and The Riders Of The Purple Sage','David Allan Coe','Della Mae','Dierks Bentley','Dixie Chicks','Dolly Parton, Linda Ronstadt & Emmylou Harris','Eilen Jewell','Emmylou Harris','Emmylou Harris & Rodney Crowell','Eric Church','Florida Georgia Line','Foy Willing & The Riders Of The Purple Sage','Hank Williams','Jerry Jeff Walker','Jewel','Jimmy Buffet','Jo Dee Messina','John Denver','John Prine','Johnny Cash','Kenny Rogers','Kris Kristofferson','Linda Ronstadt','Linda Ronstadt & Emmylou Harris','Lonestar','Lori McKenna','Lynyrd Skynyrd','Marty Robbins','Michael Martin Murphey','Old Crow Medicine Show','Olivia Newton-John','Pat Benatar','Patsy Cline','Polecat','Prairie Flyer','Redbird','Rita Coolidge','Robert Plant & Alison Krauss','Stray Birds','The Charlie Daniels Band','The Handsome Family','Waylon and Willie','Waylon Jennings','Waylon Jennings & The Waylors','Waylon Jennings & Willie Nelson','Willie Nelson and Leon Russel','Zac Brown Band','Judy Collins & Ari Hest','Keith Urban ','The Marshall Tucker Band','Nitty Gritty Dirt Band');

select * from album2songs where artist in ();
select distinct artist from album2songs where genre like 'Country' order by artist;

/* Country End */

/* Folk Start */

select distinct artist from album2songs where genre like 'Folk' order by artist;

update artist set genre = 'Folk' where  artist in ('Arlo Guthrie','Barry McGuire','Bee Gees','Bob Dylan','Gordon Lightfoot','Joan Baez','Joni Mitchell','Judy Collins','Mark Lanegan','Monsters Of Folk','Pete Seeger & Arlo Guthrie','Peter, Paul & Mary','Steve Goodman','The Kingston Trio','The Wailin\' Jennys','Bob Forrest','Gillian Welch','The Handsome Family','Harry Belafonte','John Prine','Leo Kottke','Leonard Cohen','Pete Seeger & Arlo Guthrie ','Richie Havens','Woody Guthrie');
select * from artist where genre like 'Folk';
update artist_albums set genre = 'Folk' where  artist in ('Arlo Guthrie','Barry McGuire','Bee Gees','Bob Dylan','Gordon Lightfoot','Joan Baez','Joni Mitchell','Judy Collins','Mark Lanegan','Monsters Of Folk','Pete Seeger & Arlo Guthrie','Peter, Paul & Mary','Steve Goodman','The Kingston Trio','The Wailin\' Jennys','Bob Forrest','Gillian Welch','The Handsome Family','Harry Belafonte','John Prine','Leo Kottke','Leonard Cohen','Pete Seeger & Arlo Guthrie ','Richie Havens','Woody Guthrie');

select * from artist_albums where genre like 'Folk';
update album2songs set genre = 'Folk' where  artist in ('Arlo Guthrie','Barry McGuire','Bee Gees','Bob Dylan','Gordon Lightfoot','Joan Baez','Joni Mitchell','Judy Collins','Mark Lanegan','Monsters Of Folk','Pete Seeger & Arlo Guthrie','Peter, Paul & Mary','Steve Goodman','The Kingston Trio','The Wailin\' Jennys','Bob Forrest','Gillian Welch','The Handsome Family','Harry Belafonte','John Prine','Leo Kottke','Leonard Cohen','Pete Seeger & Arlo Guthrie ','Richie Havens','Woody Guthrie');

select * from album2songs where genre like 'Folk' order by artist;

select * from artist where artist like '%Lightfoot%';

/* Folk End */

/* French Pop Start */
update artist set genre = 'French Pop' where  artist in ('Edith Piaf','Jacques Brel','Leo Ferre');
select * from artist where genre like 'French Pop';
update artist_albums set genre = 'French Pop' where  artist in ('Edith Piaf','Jacques Brel','Leo Ferre');
select * from artist_albums where genre like 'French Pop';
update album2songs set genre = 'French Pop' where  artist in ('Edith Piaf','Jacques Brel','Leo Ferre');
select * from album2songs where genre like 'French Pop';
select distinct artist from album2songs where genre = 'French Pop' order by artist;

/* French Pop End */

/* New Age Start */
update artist set genre = 'New Age' where  artist in ('Ottmar Liebert','Ottmar Liebert/Luna Negra');
select * from artist where genre like 'New Age';
update artist_albums set genre = 'New Age' where  artist in ('Ottmar Liebert','Ottmar Liebert/Luna Negra');
select * from artist_albums where genre like 'New Age';
update album2songs set genre = 'New Age' where  artist in ('Ottmar Liebert','Ottmar Liebert/Luna Negra');
select * from album2songs where genre like 'New Age';
select distinct artist from album2songs where genre = 'New Age' order by artist;

/* New Age End */

/* Jazz Start */
update artist set genre = 'Jazz' where  artist in ('Branford Marsalis','Brecker Brothers','Cal Tjader','Charlie Parker','Chick Corea','Darius Brubeck','Dave Brubeck','Dave Brubeck Quartet','Devin Duval','Fats Waller','Gary Burton, Steve Swallow, Roy Haynes, Tiger Okoshi','Herb Albert','Jaco Pastorius','Joe Henderson','John Coltrane','John Coltrane & Johnny Hartman','John Scofield','Keith Jarrett','Kenny Burrell & John Coltrane','Les McCann','Less McCann and Eddie Harris','Lester Young','Lester Young With The Oscar Peterson Trio','Madeleine Peyroux','Marsalis-Branford','Michael Brecker','Miles Davis','Miles Davis John Coltrane','Miles Davis Quintet','Oscar Peterson','Pat Metheny','Pat Metheny Group','Pat Metheny Trio','Sonny Rollins','Stanley Turrentine','The Cal Tjader Quintet','The Jazz Crusaders','The Overton Berry Trio','The Quintet','Thelonious Monk','Thelonious Monk Quartet With John Coltrane','Tony Burgos & His Swing Shift Orchestra','Walt Weiskopf Nonet','Weather Report','Alex Hargreaves','The Bad Plus','Don Cherry & John Coltrane','Herb Alpert & The Tijuana Brass','Herbie Hancock','Jimmy Witherspoon','Miguel Zeno\'n','Stan Getz');
select * from artist where genre like 'Jazz';
update artist_albums set genre = 'Jazz' where  artist in  ('Branford Marsalis','Brecker Brothers','Cal Tjader','Charlie Parker','Chick Corea','Darius Brubeck','Dave Brubeck','Dave Brubeck Quartet','Devin Duval','Fats Waller','Gary Burton, Steve Swallow, Roy Haynes, Tiger Okoshi','Herb Albert','Jaco Pastorius','Joe Henderson','John Coltrane','John Coltrane & Johnny Hartman','John Scofield','Keith Jarrett','Kenny Burrell & John Coltrane','Les McCann','Less McCann and Eddie Harris','Lester Young','Lester Young With The Oscar Peterson Trio','Madeleine Peyroux','Marsalis-Branford','Michael Brecker','Miles Davis','Miles Davis John Coltrane','Miles Davis Quintet','Oscar Peterson','Pat Metheny','Pat Metheny Group','Pat Metheny Trio','Sonny Rollins','Stanley Turrentine','The Cal Tjader Quintet','The Jazz Crusaders','The Overton Berry Trio','The Quintet','Thelonious Monk','Thelonious Monk Quartet With John Coltrane','Tony Burgos & His Swing Shift Orchestra','Walt Weiskopf Nonet','Weather Report','Alex Hargreaves','The Bad Plus','Don Cherry & John Coltrane','Herb Alpert & The Tijuana Brass','Herbie Hancock','Jimmy Witherspoon','Miguel Zeno\'n','Stan Getz');
select * from artist_albums where genre like 'Jazz';
update album2songs set genre = 'Jazz' where  artist in ('Branford Marsalis','Brecker Brothers','Cal Tjader','Charlie Parker','Chick Corea','Darius Brubeck','Dave Brubeck','Dave Brubeck Quartet','Devin Duval','Fats Waller','Gary Burton, Steve Swallow, Roy Haynes, Tiger Okoshi','Herb Albert','Jaco Pastorius','Joe Henderson','John Coltrane','John Coltrane & Johnny Hartman','John Scofield','Keith Jarrett','Kenny Burrell & John Coltrane','Les McCann','Less McCann and Eddie Harris','Lester Young','Lester Young With The Oscar Peterson Trio','Madeleine Peyroux','Marsalis-Branford','Michael Brecker','Miles Davis','Miles Davis John Coltrane','Miles Davis Quintet','Oscar Peterson','Pat Metheny','Pat Metheny Group','Pat Metheny Trio','Sonny Rollins','Stanley Turrentine','The Cal Tjader Quintet','The Jazz Crusaders','The Overton Berry Trio','The Quintet','Thelonious Monk','Thelonious Monk Quartet With John Coltrane','Tony Burgos & His Swing Shift Orchestra','Walt Weiskopf Nonet','Weather Report','Alex Hargreaves','The Bad Plus','Don Cherry & John Coltrane','Herb Alpert & The Tijuana Brass','Herbie Hancock','Jimmy Witherspoon','Miguel Zeno\'n','Stan Getz');
select * from album2songs where genre like 'Jazz';
select distinct artist from album2songs where genre = 'Jazz' order by artist;

/* Jazz End */

/* Pop Start */

update artist set genre = 'Pop' where  artist in ('The Shangri-Las','Parts & Labor','Paul Simon','Peter Bjorn and John','Petula Clark','Playing for Change','Sonny & Cher','The Swinging Blue Jeans','Telekinesis','The Tokens','Tom Jones','The Airborne Toxic Event','Wrabel','Wye Oak','Roy Orbison','Blondie','Bobby Darin','Bobby Rydell','Boz Scaggs','Bread','Carole King','City and Colour','Cold War Kids','Crispian St. Peters','Death Cab for Cutie','Del Shannon','The Diamonds','The Drifters','Dusty Springfield','Elton John','Elton John & Leon Russell','The Everly Brothers','Frank Sinatra','Freddie & The Dreamers','Generationals','George Baker','Gerry & The Pacemakers','Jackson Browne','Jose Feliciano','Junip','k.d. lang and the Siss Boom Bang','Kris Kristofferson & Rita Coolidge','Leo Sayer','Lesley Gore','The Lettermen','Lulu','The Mamas & The Papas','Manfred Mann','Marianne Faithfull','The Merseybeats','The Monkees','Neil Sedaka','Wilbert Harrison');
select * from artist where genre like 'Pop';
update artist_albums set genre = 'Pop' where  artist in ('The Shangri-Las','Parts & Labor','Paul Simon','Peter Bjorn and John','Petula Clark','Playing for Change','Sonny & Cher','The Swinging Blue Jeans','Telekinesis','The Tokens','Tom Jones','The Airborne Toxic Event','Wrabel','Wye Oak','Roy Orbison','Blondie','Bobby Darin','Bobby Rydell','Boz Scaggs','Bread','Carole King','City and Colour','Cold War Kids','Crispian St. Peters','Death Cab for Cutie','Del Shannon','The Diamonds','The Drifters','Dusty Springfield','Elton John','Elton John & Leon Russell','The Everly Brothers','Frank Sinatra','Freddie & The Dreamers','Generationals','George Baker','Gerry & The Pacemakers','Jackson Browne','Jose Feliciano','Junip','k.d. lang and the Siss Boom Bang','Kris Kristofferson & Rita Coolidge','Leo Sayer','Lesley Gore','The Lettermen','Lulu','The Mamas & The Papas','Manfred Mann','Marianne Faithfull','The Merseybeats','The Monkees','Neil Sedaka','Wilbert Harrison');
select * from artist_albums where genre like 'Pop';
update album2songs set genre = 'Pop' where  artist in ('The Shangri-Las','Parts & Labor','Paul Simon','Peter Bjorn and John','Petula Clark','Playing for Change','Sonny & Cher','The Swinging Blue Jeans','Telekinesis','The Tokens','Tom Jones','The Airborne Toxic Event','Wrabel','Wye Oak','Roy Orbison','Blondie','Bobby Darin','Bobby Rydell','Boz Scaggs','Bread','Carole King','City and Colour','Cold War Kids','Crispian St. Peters','Death Cab for Cutie','Del Shannon','The Diamonds','The Drifters','Dusty Springfield','Elton John','Elton John & Leon Russell','The Everly Brothers','Frank Sinatra','Freddie & The Dreamers','Generationals','George Baker','Gerry & The Pacemakers','Jackson Browne','Jose Feliciano','Junip','k.d. lang and the Siss Boom Bang','Kris Kristofferson & Rita Coolidge','Leo Sayer','Lesley Gore','The Lettermen','Lulu','The Mamas & The Papas','Manfred Mann','Marianne Faithfull','The Merseybeats','The Monkees','Neil Sedaka','Wilbert Harrison');
select * from album2songs where genre like 'Pop';
select distinct artist from album2songs where genre = 'Pop' order by artist;



select * from artist_albums where album in ('Rat Pack_ Members Edition [Live]');
update artist_albums set genre = 'Pop' where album in ('Rat Pack_ Members Edition [Live]');
select * from album2songs where album in ('Rat Pack_ Members Edition [Live]');
update album2songs set genre = 'Pop' where album in ('Rat Pack_ Members Edition [Live]');

/* Pop End */

/* Find exceptions */

update artist set genre = 'Sound Track' where genre like 'Soundtrack';  -- artist in ('Ottmar Liebert','Ottmar Liebert/Luna Negra');

select * from artist where genre not in ('Alternative','Blue Grass','Blues','Classic','Classical','Country','Easy Listening','Folk','French Pop','Holiday','Jazz','Latino','New Age','Pop','R&B','Reggae','RockaBilly','Soul','Talk','TestGenre','TexMex','Traditional','World','Audio Book','Sound Track') order by artist;

update artist_albums set genre = 'New Age' where  artist in ('Ottmar Liebert','Ottmar Liebert/Luna Negra');
select * from artist_albums where genre like 'New Age';
update album2songs set genre = 'New Age' where  artist in ('Ottmar Liebert','Ottmar Liebert/Luna Negra');
select * from album2songs where genre like 'New Age';
select distinct artist from album2songs where genre = 'New Age' order by artist;

select genre from genre order by genre;
update genre set genre = 'reggae' where genre like 'regae';
update album2songs set genre = 'Blue Grass' where genre like 'BlueGrass';
update `artist_albums` set genre = 'Blue Grass' where genre like 'BlueGrass';
update artist set genre = 'Blue Grass' where genre like 'BlueGrass';

update album2songs set genre = 'Reggae' where genre like 'Regae';

/*
'Alternative','BlueGrass','Blues','Classic','Classical','Country','Easy Listening','Folk',French Pop','Holiday','Jazz','Latino','New Age','Pop'.'R&B,'Reggae','Rock','RockaBilly','Soul','Talk','TestGenre','TexMex','Traditional','World','Soundttrack'

*/

select * from `artist_albums` where genre not in ()

select genre, count(genre) from album2songs group by genre order by count(genre) desc; 

select * from `artist_albums` where genre like 'Latino';
select * from `album2songs` where genre like 'Soul';
commit;

select distinct artist from album2songs where genre like 'Classical' order by artist asc;

select * from album2songs where genre like 'Classical' order by album asc;

select distinct album from album2songs where genre like 'Soundtrack' order by album asc;

update album2songs set genre = 'Jazz' where album like 'Jazz Selects';

update album2songs set genre = 'Classical' where album like 'Le Chant Du Monde 1983';

select * from album2songs where artist like 'Compilations';
select * from artist_albums where album like 'Let\'s Rock';
select * from artist where artist like 'The Black Keys';

select * from album2songs where artist like 'Compilations' and genre like 'Alternative';


/*. -----------------------   */


select aa.`album`, aa.`artist`, aa.genre,  a.artist, a.genre from artist a , artist_albums aa 
where a.artist = aa.`artist`
and aa.artist not in  ('Compilations')
and  a.`genre` != aa.`genre`;



select aa.`album`, aa.`artist`, aa.genre,  a.artist, a.genre from artist a, artist_albums aa 
where aa.`album` like 'Marianne Faithfull_ Greatest Hits' 
and a.artist = aa.artist
and aa.artist like 'Marianne Faithfull';


select distinct aa.`album`, aa.genre, ab.album ,ab.genre, ab.artist from artist_albums aa , album2songs ab where aa.`album` = ab.`album` and  aa.`genre` != ab.`genre`;

select distinct aa.`album`, aa.type, ab.album ,ab.type, ab.artist from artist_albums aa , album2songs ab
where aa.`album` = ab.`album`
and  aa.`type` != ab.`type`;
 
select distinct aa.`album`, aa.type, ab.album ,ab.type, ab.artist from artist_albums aa , album2songs a bwhere aa.`album` = ab.`album`and  aa.`type` != ab.`type`;

update album2songs set type = 'Download' where album like 'Gunfighter Ballads And Trail Songs';

update artist set genre = 'Pop' where artist like 'Neil Diamond';

update artist_albums set album = 'Amazul Montego Bay' where album like 'Montego Bay' and artist like 'Amazula';

update artist_albums set genre = 'Vinyl' where album like 'Amazul Montego Bay' and artist like 'Amazula';

update album2songs set genre = 'Pop'  where artist like 'Neil Diamond';

update album2songs set album = 'Amazul Montego Bay'  where artist like 'Amazula';

update artist_albums set type = 'Vinyl' where album like 'Amazul Montego Bay';

select * from artist where artist like 'Neil Diamond';

select * from album2songs where album like 'Montego Bay';

delete from artist where artist like 'Josh Rouse';
delete from album2songs where artist like 'Josh Rouse';
delete from artist_albums where artist like 'Josh Rouse';

select * from album2songs where album like 'The Anthology';

update artist_albums set genre = 'Pop' where album like 'More Solid Gold 60s Volume 2';

update album2songs set genre = 'Pop' where album like 'All-Time Greatest Hits';

update album2songs set Type = 'Download' where album like 'Beatles For Sale';

update album2songs set genre = 'Pop' where artist like 'Freddie & The Dreamers';

update artist_albums set album = 'The Ultimate Collection-Freddie' where artist like 'Freddie & The Dreamers';

update album2songs set album = 'The Ultimate Collection-Freddie' where artist like 'Freddie & The Dreamers';

update album2songs set genre = 'Folk' where album like 'Both Sides Now - The Very Best Of [Disc 2]';

update album2songs set artist = 'Judy Collins' where album like 'Both Sides Now - The Very Best Of [Disc 2]';

select * from album2songs where album like 'Both Sides Now - The Very Best Of [Disc 2]';



select * from artist where artist = 'Hair';

update artist set genre = 'Soundtrack' where artist like 'Neil Warner';

select * from genre order by genre;

insert into genre values ('New Age', 26);

update genre set genre = 'Reggae' where `g_idx` = 12;

select `genre`, count(`genre`) from album2songs group by `genre` order by `genre`;

delete from genre where genre like 'NewGenre';

/*   Alternative	338
Audio Book	81
Audiobooks	2
Blue Grass	192
Blues	1136
Classical	118
Country	1031
Folk	735
French Pop	78
Jazz	827
New Age	39
Pop	759
R&B	577
Reggae	24
Rock	5691
RockaBilly	32
Soundtrack	89
Talk	1
TestGenre	3
TexMex	194

Alternative	2
Blue Grass	3
Blues	4
Classical	5
Country	6
Easy Listening	21
Folk	7
French Pop	24
Holiday	8
Jazz	9
Latino	10
New Age	26
Pop	11
R&B	23
Reggae	12
Rock	1
RockaBilly	13
Soul	14
Soundtrack	25
Talk	15
TestGenre	16
TexMex	17
Traditional	18
World	19
*/

commit;


select * from `artist_albums` where artist like '' order by album;

select * from album2songs where song like '%Comfortably%';

select * from album2songs where album like 'Masked & Anonymous' order by song;

select * from album2songs where artist like 'Compilations'  order by album,song;


select * from album2songs where artist like '%Doug%';

select * from album2songs where artist like '%ZZ Top%';

select * from album2songs where album like "Doug Sahm Live Austin TX" order by genre, song;


select * from `artist_albums` where artist like '%Doobie%' order by album;
select * from album2songs where album like 'Esta Bueno (Deluxe Edition)' order by song;

delete from album2songs where album like "Who Did That to You (Best Western Songs)" and artist = "Compilations";

delete from artist_albums where `index` = 10012;



select * from artist_albums where album like "Who Did That to You (Best Western Songs)";

select * from album2songs where album like '%Who Did%' order by album;



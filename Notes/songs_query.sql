commit;

use Music;
select * from Music.songs;
-- order by iTunesSongs.artist;

select count(*) from Music.songs;
-- 6502
-- 6528

select * from new_music.iTunesSongs
where iTunesSongs.artist like 'Jose Fel%';

-- where songs.genre like 'Country';
-- 752
use new_music;
select count(*) from new_music.songs
where songs.genre like 'Jazz';
-- 858
use new_music;
select count(*) from new_music.songs
where songs.genre like 'Rock';
-- 3683
select count(*) from new_music.songs
where songs.genre like 'Folk';
-- 573

select iTunesSongs.genre, count(songs.genre) 
from new_music.iTunesSongs
group by songs.genre
order by count(songs.genre);


select Music.songs.artist, count(Music.songs.artist) 
from Music.songs
group by Music.songs.artist
order by count(Music.songs.artist) desc;

select count(distinct Music.songs.artist) 
from Music.songs;




select iTunesSongs.Index, count(iTunesSongs.Index) 
from new_music.iTunesSongs
group by iTunesSongs.Index
order by count(iTunesSongs.Index) desc;
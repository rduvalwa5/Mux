SELECT count(*) FROM `Music`.album2songs;

-- 6570

SELECT count(*) FROM `Music`.artist_albums;

-- 869

SELECT count(*) FROM `Music`.artist;

-- 511

/*
6570
done
869
done
511
done
*/

/* update artist for genre
Single-table syntax:

UPDATE [LOW_PRIORITY] [IGNORE] table_reference
    SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]
Multiple-table syntax:

UPDATE [LOW_PRIORITY] [IGNORE] table_references
    SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    [WHERE where_condition]

 */

UPDATE `Music`.artist, `Music`.artist_albums, `Music`.album2songs
   SET `Music`.artist.genre = 'Folk',
       `Music`.artist_albums.genre = 'Folk',
       `Music`.album2songs.genre = 'Folk'
 WHERE    `Music`.artist.artist = 'Joan Baez'
       OR `Music`.artist_albums.artist = 'Joan Baez'
       OR `Music`.album2songs.artist = 'Joan Baez';

UPDATE `Music`.artist
   SET `Music`.artist.genre = 'Folk'
 WHERE `Music`.artist.artist = 'Joan Baez';

SELECT *
  FROM `Music`.artist
 WHERE artist = 'Joan Baez';
CREATE TABLE artist_albums(
  index int NOT NULL,
  artist varchar(100) NOT NULL,
  album varchar(200) NOT NULL,
  genre varchar(20),
  type varchar(20),
  cover_name varchar(100),
  cover_idx int
);
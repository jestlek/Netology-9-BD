CREATE TABLE IF NOT EXISTS genres (
	genre_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS artists (
	artist_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS albums (
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	date DATE
);

CREATE TABLE IF NOT EXISTS tracks (
	track_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	duration INTEGER NOT NULL,
	albums_id INTEGER NOT NULL REFERENCES albums(album_id)
);

CREATE TABLE IF NOT EXISTS compilation (
	comp_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	date DATE
);

CREATE TABLE IF NOT EXISTS ArtistsGenres (
	genre_id INTEGER REFERENCES genres(genre_id),
	artist_id INTEGER REFERENCES artists(artist_id),
	CONSTRAINT pk PRIMARY KEY (genre_id, artist_id)
);

CREATE TABLE IF NOT EXISTS ArtistsAlbums (
	album_id INTEGER REFERENCES albums(album_id),
	artist_id INTEGER REFERENCES artists(artist_id),
	CONSTRAINT pk1 PRIMARY KEY (album_id, artist_id)
);

CREATE TABLE IF NOT EXISTS TracksCompilations (
	track_id INTEGER REFERENCES tracks(track_id),
	comp_id INTEGER REFERENCES compilation(comp_id),
	CONSTRAINT pk2 PRIMARY KEY (track_id, comp_id)
);


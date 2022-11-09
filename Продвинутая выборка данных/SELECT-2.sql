SELECT g.name, count(a.name) FROM genres AS g
JOIN artistsgenres AS ag ON g.genre_id = ag.genre_id 
JOIN artists AS a ON ag.artist_id = a.artist_id 
GROUP BY g.name
ORDER BY count(a.name);

SELECT count(t.name) FROM albums AS a
JOIN tracks AS t ON t.albums_id = a.album_id
WHERE a.date >= '01.01.2018' AND a.date <= '31.12.2020';

SELECT a.name, avg(t.duration) FROM tracks AS t
JOIN albums AS a ON a.album_id = t.albums_id 
GROUP BY a.name
ORDER BY avg(t.duration);

SELECT a.name FROM artists AS a
JOIN artistsalbums AS aa ON aa.artist_id = a.artist_id 
JOIN albums AS am ON am.album_id = aa.album_id 
WHERE NOT am.date >= '01.01.2020' AND am.date <= '31.12.2020';

SELECT DISTINCT c.name FROM compilation AS c
JOIN trackscompilations AS tc ON c.comp_id = tc.comp_id 
JOIN tracks AS t ON t.track_id = tc.track_id 
JOIN albums AS a ON a.album_id = t.albums_id
JOIN artistsalbums AS aa ON aa.album_id = a.album_id 
JOIN artists AS art ON art.artist_id = aa.artist_id
WHERE art.name LIKE '%2pack%';

SELECT a.name FROM albums AS a
JOIN artistsalbums AS aa ON aa.album_id = a.album_id 
JOIN artists AS art ON art.artist_id = aa.artist_id 
JOIN artistsgenres AS ag ON ag.artist_id = art.artist_id
JOIN genres AS g ON g.genre_id = ag.genre_id
GROUP BY a.name
HAVING count(DISTINCT g.name) > 1;

SELECT t.name FROM tracks AS t
LEFT JOIN trackscompilations AS tc ON tc.track_id = t.track_id 
WHERE tc.track_id IS NULL

SELECT a.name, t.duration FROM tracks AS t
JOIN albums AS alb ON alb.album_id = t.albums_id 
JOIN artistsalbums AS aa ON aa.album_id = alb.album_id 
JOIN artists AS a ON a.artist_id = aa.artist_id
GROUP BY a.name, t.duration 
HAVING t.duration = (SELECT min(duration) FROM tracks);

SELECT DISTINCT a.name FROM albums AS a
JOIN tracks AS t on t.albums_id = a.album_id 
WHERE t.albums_id IN (
    SELECT album_id FROM tracks
    HAVING count(albums_id) = (
        SELECT count(albums_id) FROM tracks
        GROUP BY album_id));


















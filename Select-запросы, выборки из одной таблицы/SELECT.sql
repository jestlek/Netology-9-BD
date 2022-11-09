SELECT name, date FROM albums
WHERE date >= '01.01.2018';

SELECT name, duration FROM tracks
ORDER BY duration DESC 
LIMIT 1;

SELECT name, duration FROM tracks
WHERE duration >= 3.5;

SELECT name FROM compilation
WHERE date BETWEEN '01.01.2018' AND '31.12.2020';

SELECT name FROM artists
WHERE name NOT LIKE '% %';

SELECT name FROM tracks
WHERE name LIKE '%my%';
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT b.name AS genre, count(a.show_id) AS number_of_shows
FROM tv_show_genres a 
LEFT JOIN tv_genres b 
ON a.genre_id = b.id
GROUP BY a.genre_id
ORDER BY 2 DESC;

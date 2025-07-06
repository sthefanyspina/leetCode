SELECT name, SUM(case when distance is NULL THEN 0 ELSE distance END) AS travelled_distance 
FROM Users LEFT JOIN Rides ON Users.id = Rides.user_id GROUP BY Users.id, name ORDER BY travelled_distance DESC, name ASC

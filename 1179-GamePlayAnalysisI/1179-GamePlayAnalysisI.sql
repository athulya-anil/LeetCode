-- Last updated: 10/12/2025, 07:40:55
SELECT 
    player_id, 
    MIN(event_date) AS first_login
FROM 
    Activity
GROUP BY 
    player_id;

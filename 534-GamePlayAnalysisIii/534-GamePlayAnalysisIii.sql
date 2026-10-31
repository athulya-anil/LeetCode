-- Last updated: 31/10/2026, 19:07:10
select player_id, event_date, 
SUM(games_played) over(partition by player_id order by event_date) as 'games_played_so_far'
from Activity
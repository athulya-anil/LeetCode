-- Last updated: 23/07/2026, 09:58:06
# Write your MySQL query statement below
select player_id, event_date, 
sum(games_played) over(partition by player_id order by event_date) as 'games_played_so_far'
from Activity
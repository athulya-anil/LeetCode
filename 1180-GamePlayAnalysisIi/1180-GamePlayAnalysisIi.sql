-- Last updated: 13/07/2026, 16:48:22
# Write your MySQL query statement below
with cte as (select player_id, device_id, games_played, event_date,
DENSE_RANK() over(PARTITION BY player_id order by event_date) as rank1
from Activity)

select player_id, device_id
from cte
where rank1 = 1


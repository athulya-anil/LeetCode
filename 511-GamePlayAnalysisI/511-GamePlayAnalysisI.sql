-- Last updated: 31/10/2026, 19:07:17
# Write your MySQL query statement below
with cte as(select player_id, event_date,
DENSE_RANK() over(PARTITION BY player_id order by event_date) as rank1
from Activity)

select player_id, event_date as first_login
from cte
where rank1 = 1
-- Last updated: 14/06/2026, 23:02:28
# Write your MySQL query statement below
select round(count(a1.player_id) / (select count(distinct player_id) from Activity),2) as fraction
from Activity a1 join Activity a2
on datediff(a1.event_date,a2.event_date) = 1 and a1.player_id=a2.player_id
where (a1.player_id, a2.event_date) in (select player_id,min(event_date) from Activity group by 1)
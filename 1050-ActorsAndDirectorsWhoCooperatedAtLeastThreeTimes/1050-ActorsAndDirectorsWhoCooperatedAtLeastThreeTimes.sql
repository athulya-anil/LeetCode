-- Last updated: 31/10/2026, 19:07:40
# Write your MySQL query statement below
select actor_id, director_id
from ActorDirector
group by 1,2
having count(*) >= 3

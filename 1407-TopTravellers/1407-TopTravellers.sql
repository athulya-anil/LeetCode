-- Last updated: 31/10/2026, 19:05:28
# Write your MySQL query statement below
select DISTINCT name, coalesce(sum(distance),0) as travelled_distance
from Users u left join Rides r 
on u.id = r.user_id
group by user_id
order by 2 desc, 1
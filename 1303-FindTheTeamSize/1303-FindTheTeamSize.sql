-- Last updated: 31/10/2026, 19:06:00
# Write your MySQL query statement below
with cte as (select team_id, count(*) as team_size
from Employee
group by 1)

select employee_id, team_size
from Employee e left join cte c
on e.team_id = c.team_id
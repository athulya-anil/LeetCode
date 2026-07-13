-- Last updated: 13/07/2026, 17:48:02
# Write your MySQL query statement below
with cte as (select team_id, count(*) as team_size
from Employee
group by 1)

select employee_id, team_size
from Employee e left join cte c
on e.team_id = c.team_id
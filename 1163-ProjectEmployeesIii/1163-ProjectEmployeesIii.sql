-- Last updated: 13/07/2026, 16:48:25
# Write your MySQL query statement below
with cte as (select e.name, p.project_id, e.employee_id,
DENSE_RANK() over(PARTITION BY project_id order by experience_years desc) as order1
from Project p join Employee e
on p.employee_id = e.employee_id)

select project_id, employee_id
from cte 
where order1<=1
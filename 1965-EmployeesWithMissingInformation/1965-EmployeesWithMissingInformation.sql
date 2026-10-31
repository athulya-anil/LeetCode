-- Last updated: 31/10/2026, 19:03:21
# Write your MySQL query statement below
with cte as (select employee_id
from Employees e
where not EXISTS (select * from Salaries  s where e.employee_id = s.employee_id)
UNION ALL
select employee_id 
from Salaries s
where not EXISTS (select * from Employees e where e.employee_id = s.employee_id ))
select employee_id
from cte 
order by 1
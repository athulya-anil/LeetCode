-- Last updated: 14/06/2026, 23:01:39
# Write your MySQL query statement below
select employee_id
from Employees
where salary < 30000 and manager_id IS NOT NULL and manager_id not in (select employee_id from Employees)
order by 1
-- Last updated: 31/10/2026, 19:03:38
# Write your MySQL query statement below
select employee_id, (CASE WHEN name not like 'M%'and employee_id %2 != 0 then salary
ELSE 0 END) as bonus
from Employees
order by 1
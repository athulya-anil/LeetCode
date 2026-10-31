-- Last updated: 31/10/2026, 19:03:07
select employee_id
from Employees
where manager_id is not null and manager_id not in (select employee_id from Employees)
and salary <30000
order by 1
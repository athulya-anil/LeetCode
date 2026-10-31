-- Last updated: 31/10/2026, 19:05:37
select e1.unique_id as unique_id, e.name
from Employees e left join EmployeeUNI e1
on e.id = e1.id;

-- Last updated: 14/06/2026, 23:02:10
# Write your MySQL query statement below
select e1.unique_id, e.name
from Employees e left join EmployeeUNI e1
on e.id = e1.id
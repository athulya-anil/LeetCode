-- Last updated: 31/10/2026, 19:05:38
# Write your MySQL query statement below
select id, name
from Students
where department_id not in (select id from Departments)
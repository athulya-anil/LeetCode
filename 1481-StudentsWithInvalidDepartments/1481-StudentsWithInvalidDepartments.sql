-- Last updated: 13/07/2026, 17:47:58
# Write your MySQL query statement below
select id, name
from Students
where department_id not in (select id from Departments)
-- Last updated: 31/10/2026, 19:04:00
# Write your MySQL query statement below
select event_day as day, emp_id, sum(out_time-in_time) as total_time
from Employees
group by 1,2
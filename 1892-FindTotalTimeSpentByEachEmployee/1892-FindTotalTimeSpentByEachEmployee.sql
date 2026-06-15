-- Last updated: 14/06/2026, 23:01:52
# Write your MySQL query statement below

select event_day as day, emp_id, sum(out_time-in_time) as total_time from Employees group by 1,2

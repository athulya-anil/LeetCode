-- Last updated: 10/12/2025, 07:40:15
# Write your MySQL query statement below

select event_day as day, emp_id, sum(out_time-in_time) as total_time from Employees group by 1,2

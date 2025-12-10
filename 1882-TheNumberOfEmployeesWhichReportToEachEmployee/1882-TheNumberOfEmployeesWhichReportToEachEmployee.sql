-- Last updated: 10/12/2025, 07:40:16
# Write your MySQL query statement below

select e.reports_to as employee_id, c.name, count(e.employee_id) as reports_count, ROUND(AVG(e.age),0) as average_age from Employees e join Employees c on c.employee_id = e.reports_to group by 1 order by 1


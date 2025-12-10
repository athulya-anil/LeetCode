-- Last updated: 10/12/2025, 07:40:58
# Write your MySQL query statement below

select project_id, ROUND(avg(experience_years),2) as average_years
from Project p left join Employee e on p.employee_id = e.employee_id group by 1
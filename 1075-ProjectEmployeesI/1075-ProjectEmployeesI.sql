-- Last updated: 31/10/2026, 19:07:25
# Write your MySQL query statement below
select p.project_id, round(avg(experience_years),2) as 'average_years'
from Project p left join Employee e 
on p.employee_id = e.employee_id 
group by 1
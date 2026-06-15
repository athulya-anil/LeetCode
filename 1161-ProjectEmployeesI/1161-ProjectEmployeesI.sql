-- Last updated: 14/06/2026, 23:02:31
select project_id, round(avg(experience_years),2) as average_years
from Project p left join Employee e on p.employee_id = e.employee_id
group by 1
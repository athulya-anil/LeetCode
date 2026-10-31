-- Last updated: 31/10/2026, 19:04:11
select e.employee_id, e.name, count(m.employee_id) as reports_count, round(avg(m.age),0) as average_age
from Employees m join Employees e
on e.employee_id = m.reports_to
group by 1,2
order by 1
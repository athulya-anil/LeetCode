-- Last updated: 31/10/2026, 19:03:57
with cte as (
    select employee_id, department_id, count(department_id) as department_count from Employee
    group by 1
)

select employee_id, department_id from cte
where department_count = 1 
UNION ALL
select employee_id, department_id
from Employee where primary_flag = 'Y'
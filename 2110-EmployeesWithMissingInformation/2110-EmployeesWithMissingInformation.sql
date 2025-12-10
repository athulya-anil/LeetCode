-- Last updated: 10/12/2025, 07:40:03
# Write your MySQL query statement below
with cte as (select employee_id from Employees
union all
select employee_id from Salaries
)

select distinct employee_id from cte where employee_id not in (select employee_id from Employees) or employee_id not in (select employee_id from Salaries) order by 1
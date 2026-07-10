-- Last updated: 10/07/2026, 11:59:34
# Write your MySQL query statement below
with cte as(
    select departmentId, max(salary) as m from Employee group by 1
)
select d.name as Department, e.name as Employee, e.salary as Salary from Employee e join Department d on d.id=e.departmentId
where (e.salary,departmentId) in (select m, departmentId from cte)
-- Last updated: 10/12/2025, 07:42:26
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from Employee where salary not in (select max(salary) from Employee)

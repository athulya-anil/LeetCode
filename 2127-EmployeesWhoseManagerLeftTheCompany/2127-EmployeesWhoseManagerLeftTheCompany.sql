-- Last updated: 10/12/2025, 07:40:02
# Write your MySQL query statement below
select employee_id from Employees where salary<30000 and 
manager_id IS NOT NULL and manager_id not in (select employee_id from Employees where employee_id IS NOT NULL) order by 1;

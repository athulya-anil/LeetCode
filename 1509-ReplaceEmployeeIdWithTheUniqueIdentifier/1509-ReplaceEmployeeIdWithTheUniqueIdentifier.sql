-- Last updated: 10/12/2025, 07:40:34
# Write your MySQL query statement below
select unique_id, name
from Employees left join EmployeeUNI on EmployeeUNI.id = Employees.id
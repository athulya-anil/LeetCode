-- Last updated: 10/12/2025, 07:40:10
# Write your MySQL query statement below

select employee_id, case
    when employee_id%2 !=0 and name not like 'M%' then salary
    else 0
    end as bonus 

from Employees order by 1
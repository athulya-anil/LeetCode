-- Last updated: 14/06/2026, 23:03:09
# Write your MySQL query statement below
select class
from Courses 
group by 1
having count(student) >= 5
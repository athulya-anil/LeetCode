-- Last updated: 10/12/2025, 07:41:31
# Write your MySQL query statement below
select class from Courses group by class having count(student)>=5;
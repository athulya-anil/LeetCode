-- Last updated: 31/10/2026, 19:06:58
# Write your MySQL query statement below
with cte as (select student_id, course_id, grade,
ROW_NUMBER() OVER(PARTITION BY student_id order by grade desc, course_id) as rk
from Enrollments)

select student_id, course_id, grade
from cte 
where rk = 1
order by 1
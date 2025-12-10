-- Last updated: 10/12/2025, 07:40:40
# Write your MySQL query statement below

select s.student_id, s.student_name, s1.subject_name, count(e.subject_name) as attended_exams
from Students s 
cross join Subjects s1 
left join Examinations e 
on s.student_id = e.student_id and s1.subject_name = e.subject_name group by 1,2,3 order by 1,2
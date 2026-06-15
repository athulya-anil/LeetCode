-- Last updated: 14/06/2026, 23:01:28
# Write your MySQL query statement below
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by 1
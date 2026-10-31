-- Last updated: 31/10/2026, 19:02:20
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by 1
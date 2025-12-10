-- Last updated: 10/12/2025, 07:39:50
# Write your MySQL query statement below

select teacher_id, count(distinct(subject_id)) as cnt from Teacher group by 1;
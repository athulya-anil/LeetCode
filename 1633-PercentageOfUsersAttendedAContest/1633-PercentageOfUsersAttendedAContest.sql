-- Last updated: 31/10/2026, 19:04:37
# Write your MySQL query statement below

select contest_id, round(count(r.user_id)/(select count(*) from Users)*100,2) as percentage
from Users u join Register r on u.user_id = r.user_id
group by 1 
order by 2 desc,1 
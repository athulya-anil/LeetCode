-- Last updated: 14/06/2026, 23:01:42
# Write your MySQL query statement below
select s.user_id, round(count(case when c.action = 'confirmed' then 1 end)/count(*),2) as confirmation_rate
from Signups s left join Confirmations c
on s.user_id = c.user_id 
group by 1
-- Last updated: 31/10/2026, 19:03:35
# Write your MySQL query statement below
with cte as (select user_id, time_stamp,
DENSE_RANK() over(PARTITION BY user_id order by time_stamp desc) as rk1
from Logins
where YEAR(time_stamp) = 2020)

select user_id, time_stamp as last_stamp
from cte
where rk1 = 1  

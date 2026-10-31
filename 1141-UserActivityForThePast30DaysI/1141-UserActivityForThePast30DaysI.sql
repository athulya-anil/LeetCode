-- Last updated: 31/10/2026, 19:06:56
select activity_date as day, count(DISTINCT user_id) as active_users
from Activity
where activity_date between '2019-07-27' - INTERVAL 29 DAY and '2019-07-27' 
group by 1
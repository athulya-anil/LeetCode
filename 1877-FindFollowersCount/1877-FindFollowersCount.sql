-- Last updated: 14/06/2026, 23:01:54
# Write your MySQL query statement below
select user_id, count(follower_id) as followers_count
from Followers
group by 1
order by 1
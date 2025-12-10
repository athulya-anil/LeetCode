-- Last updated: 10/12/2025, 07:40:17
# Write your MySQL query statement below

select user_id, count(follower_id) as followers_count
from Followers group by 1 order by 1;
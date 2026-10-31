-- Last updated: 31/10/2026, 19:04:13
select user_id, count(distinct follower_id) as followers_count
from Followers
group by 1
-- Last updated: 14/06/2026, 23:01:56
# Write your MySQL query statement below
select tweet_id
from Tweets
where length(content) > 15
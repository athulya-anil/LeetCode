-- Last updated: 10/12/2025, 07:40:19
# Write your MySQL query statement below

select tweet_id
from Tweets
where char_length(content) > 15
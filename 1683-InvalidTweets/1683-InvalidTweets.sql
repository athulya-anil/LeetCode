-- Last updated: 31/10/2026, 19:04:24
select tweet_id
from Tweets
where char_length(content) > 15;
-- Last updated: 24/07/2026, 02:04:12
# Write your MySQL query statement below
select LEAST(from_id,to_id) as person1, GREATEST(from_id,to_id) as person2, count(*) as call_count, sum(duration) as total_duration
from Calls
group by 1,2
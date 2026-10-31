-- Last updated: 31/10/2026, 19:04:28
# Write your MySQL query statement below
select user_id, concat(substr(UPPER(name),1,1),substr(LOWER(name),2,length(name))) as name
from Users
order by 1


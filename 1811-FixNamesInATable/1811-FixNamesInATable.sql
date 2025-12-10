-- Last updated: 10/12/2025, 07:40:21
# Write your MySQL query statement below

select user_id, concat(substr(UPPER(name),1,1),substr(lower(name),2,length(name))) as name from Users order by 1;
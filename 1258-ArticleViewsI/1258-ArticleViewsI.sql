-- Last updated: 10/12/2025, 07:40:50
# Write your MySQL query statement below

select distinct author_id as id
from Views 
where author_id = viewer_id
order by 1

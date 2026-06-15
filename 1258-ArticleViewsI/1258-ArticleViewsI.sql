-- Last updated: 14/06/2026, 23:02:25
# Write your MySQL query statement below
select distinct author_id as id
from Views
where viewer_id = author_id
order by 1
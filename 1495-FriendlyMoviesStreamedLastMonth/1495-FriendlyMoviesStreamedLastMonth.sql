-- Last updated: 31/10/2026, 19:05:19
# Write your MySQL query statement below
select distinct title
from TVProgram p left join Content c 
on p.content_id = c.content_id
where Kids_content = 'Y' and content_type = 'Movies' and program_date like '2020-06%'
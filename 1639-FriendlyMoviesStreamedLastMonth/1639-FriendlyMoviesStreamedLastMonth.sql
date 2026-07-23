-- Last updated: 23/07/2026, 09:57:40
# Write your MySQL query statement below
select distinct title
from TVProgram p left join Content c 
on p.content_id = c.content_id
where Kids_content = 'Y' and content_type = 'Movies' and program_date like '2020-06%'
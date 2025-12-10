-- Last updated: 10/12/2025, 07:42:23
# Write your MySQL query statement below

select score, DENSE_RANK() OVER (ORDER BY score desc) as 'rank' 
from Scores order by 1 desc
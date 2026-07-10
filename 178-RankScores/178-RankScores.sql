-- Last updated: 10/07/2026, 11:59:40
# Write your MySQL query statement below

select score, DENSE_RANK() OVER (ORDER BY score desc) as 'rank' 
from Scores order by 1 desc
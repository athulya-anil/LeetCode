-- Last updated: 31/10/2026, 19:02:05
# Write your MySQL query statement below
(select 'bull' as word, count(*) as count
from Files
where content like '% bull %')
UNION
(select 'bear' as word, count(*) as count
from Files
where content like '% bear %')

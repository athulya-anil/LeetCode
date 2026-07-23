-- Last updated: 23/07/2026, 09:56:45
# Write your MySQL query statement below
(select 'bull' as word, count(*) as count
from Files
where content like '% bull %')
UNION
(select 'bear' as word, count(*) as count
from Files
where content like '% bear %')

-- Last updated: 24/08/2026, 12:55:28
# Write your MySQL query statement below
select min(abs(b.x-a.x)) as shortest
from Point a join Point b
on a.x<b.x
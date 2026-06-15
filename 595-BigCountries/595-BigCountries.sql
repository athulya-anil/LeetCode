-- Last updated: 14/06/2026, 23:03:10
# Write your MySQL query statement below
select name, population, area
from World
where area >= 3000000 or population >= 25000000;
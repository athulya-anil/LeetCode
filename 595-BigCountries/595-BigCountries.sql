-- Last updated: 10/12/2025, 07:41:33
# Write your MySQL query statement below

select name, population, area
from World
where area >= '3000000' or population >= '25000000'
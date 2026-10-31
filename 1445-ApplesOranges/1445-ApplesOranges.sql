-- Last updated: 31/10/2026, 19:05:23
# Write your MySQL query statement below
select sale_date, SUM(CASE WHEN fruit = 'apples' then sold_num ELSE 0 END) - SUM(CASE WHEN fruit = 'oranges' then sold_num ELSE 0 END) 
as diff
from Sales
group by sale_date
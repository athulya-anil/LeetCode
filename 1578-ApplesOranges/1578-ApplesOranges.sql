-- Last updated: 24/07/2026, 02:04:24
# Write your MySQL query statement below
select sale_date, SUM(CASE WHEN fruit = 'apples' then sold_num ELSE 0 END) - SUM(CASE WHEN fruit = 'oranges' then sold_num ELSE 0 END) 
as diff
from Sales
group by sale_date
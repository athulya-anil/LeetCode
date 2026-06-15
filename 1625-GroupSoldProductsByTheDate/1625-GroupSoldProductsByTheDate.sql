-- Last updated: 14/06/2026, 23:02:08
# Write your MySQL query statement below
select sell_date, count(distinct(product)) as num_sold, group_concat(distinct(product) order by product) as products
from Activities group by 1;
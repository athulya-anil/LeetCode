-- Last updated: 31/10/2026, 19:07:31
# Write your MySQL query statement below
select product_id, sum(quantity) as total_quantity
from Sales
group by 1
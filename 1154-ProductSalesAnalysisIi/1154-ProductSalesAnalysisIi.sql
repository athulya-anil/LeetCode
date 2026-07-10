-- Last updated: 10/07/2026, 11:57:35
# Write your MySQL query statement below
select product_id, sum(quantity) as total_quantity
from Sales
group by 1
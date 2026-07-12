-- Last updated: 12/07/2026, 02:54:15
# Write your MySQL query statement below
with cte as(select p.product_id, p.product_name, order_date, order_id,
DENSE_RANK() over(PARTITION BY product_name order by order_date desc) as rank1
from Orders o join Products p 
on o.product_id = p.product_id)

select product_name, product_id, order_id, order_date
from cte
where rank1=1
order by 1, 2 asc, 3


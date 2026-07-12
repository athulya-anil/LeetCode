-- Last updated: 12/07/2026, 02:54:16
# Write your MySQL query statement below
with cte as (select c.customer_id, c.name as customer_name, o.order_id, o.order_date, o.cost,
DENSE_RANK() over(PARTITION BY customer_id order by order_date desc) as rank1
from Orders o join Customers c
on o.customer_id = c.customer_id)

select customer_name, customer_id, order_id, order_date
from cte 
where rank1<=3
order by 1,2,4 desc
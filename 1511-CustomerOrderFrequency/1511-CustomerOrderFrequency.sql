-- Last updated: 31/10/2026, 19:05:05
# Write your MySQL query statement below
with cte as (select o.customer_id, order_id, p.product_id, order_date, (price*quantity) as total
from Product p join Orders o
on p.product_id = o.product_id),

cte_june as(select customer_id, sum(total) as total_june
from cte
where order_date like '2020-06%' 
group by 1),

cte_july as(select customer_id, sum(total) as total_july
from cte
where order_date like '2020-07%' 
group by 1)

select cte_june.customer_id, c.name
from cte_june join cte_july on cte_june.customer_id = cte_july.customer_id
left join Customers c on cte_july.customer_id = c.customer_id
where total_july >= 100 and total_june >= 100
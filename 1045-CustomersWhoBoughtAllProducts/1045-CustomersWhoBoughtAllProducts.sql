-- Last updated: 31/10/2026, 19:07:43
with cte as (
    select c.customer_id, count(distinct c.product_key) as purchased
from Customer c join Product p
on c.product_key = p.product_key
group by 1

)

select customer_id from cte where purchased = (select count(distinct product_key) from Product)

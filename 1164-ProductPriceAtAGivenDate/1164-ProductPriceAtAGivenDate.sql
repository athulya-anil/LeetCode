-- Last updated: 31/10/2026, 19:06:45
with cte as (select product_id, change_date, new_price,
DENSE_RANK() over(PARTITION BY product_id ORDER BY change_date desc) as rk
from Products
where change_date <= '2019-08-16')

select distinct product_id, new_price as price
from cte
where rk = 1
UNION ALL
select distinct product_id, 10 as price
from Products
where product_id not in (select product_id from cte)
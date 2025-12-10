-- Last updated: 10/12/2025, 07:40:48
# Write your MySQL query statement below
with cte as (
    select buyer_id, count(order_id) as orders_in_2019 from Orders where order_date like '%2019%' group by 1
)

select user_id as buyer_id, join_date, COALESCE(c.orders_in_2019, 0) as orders_in_2019
from Users u left join cte c on u.user_id = c.buyer_id


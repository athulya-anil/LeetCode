-- Last updated: 14/06/2026, 23:02:22
# Write your MySQL query statement below
with cts as(select sum(
    case when order_date = customer_pref_delivery_date then 1 else 0 end
) as immediate_order, sum(
    case when order_date != customer_pref_delivery_date then 1 else 0 end
) as scheduled
from Delivery
where (customer_id, order_date) in (select customer_id, min(order_date) from Delivery group by 1
))
select round(immediate_order/(immediate_order + scheduled)*100,2) as immediate_percentage from cts

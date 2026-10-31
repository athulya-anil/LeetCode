-- Last updated: 31/10/2026, 19:06:41
# Write your MySQL query statement below
with cte as (select delivery_id, customer_id, order_date, customer_pref_delivery_date,
(CASE WHEN order_date = customer_pref_delivery_date then 'immediate' ELSE 'scheduled' END) as order_type
from Delivery)

select ROUND((sum(CASE WHEN order_type = 'immediate' then 1 ELSE 0 END)/(select count(*) from Delivery)) * 100,2) as immediate_percentage
from cte

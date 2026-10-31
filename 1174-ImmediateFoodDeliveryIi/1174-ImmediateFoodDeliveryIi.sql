-- Last updated: 31/10/2026, 19:06:39
with cte as(
    select delivery_id, customer_id, order_date, CASE 
                                        WHEN order_date = customer_pref_delivery_date then 'immediate'
                                        ELSE 'scheduled' END as order_type
    from Delivery                                     
),
first_order as(
    select customer_id, min(order_date) as first_order_date from cte group by 1
)

select round(SUM(CASE WHEN order_type = 'immediate' then 1 else 0 end)/count(*)*100,2) as immediate_percentage
from cte c join first_order f
on c.customer_id = f.customer_id and c.order_date = f.first_order_date

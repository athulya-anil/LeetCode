-- Last updated: 10/12/2025, 07:40:47
# Write your MySQL query statement below

with cte as(
    select customer_id,min(order_date),min(customer_pref_delivery_date),
        case
            when min(order_date) = min(customer_pref_delivery_date) then 'immediate'
            else 'scheduled'
            end as type
    from Delivery group by 1
)

select ROUND((sum(case when type='immediate' then 1 else 0 end)/(select count(type) from cte)*100),2) as immediate_percentage from cte;


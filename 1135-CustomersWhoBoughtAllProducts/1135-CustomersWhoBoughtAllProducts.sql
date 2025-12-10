-- Last updated: 10/12/2025, 07:41:04
# Write your MySQL query statement below

with cte as (
    select customer_id, product_key, group_concat(product_key order by product_key) as products1, count(distinct product_key) as count from Customer group by 1    
), 

cte2 as (
    select count(distinct product_key) from Product 
)

select customer_id from cte where count = (select * from cte2)


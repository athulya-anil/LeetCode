-- Last updated: 13/07/2026, 16:47:18
# Write your MySQL query statement below
select user_id, sum(price*quantity) as spending
from Sales s left join Product p 
on p.product_id = s.product_id
group by 1
order by 2 desc, 1
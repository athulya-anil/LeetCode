-- Last updated: 31/10/2026, 19:04:39
# Write your MySQL query statement below
select seller_name
from Seller s left join Orders o
on s.seller_id = o.seller_id
and YEAR(sale_date) = 2020
where o.seller_id is null
order by 1


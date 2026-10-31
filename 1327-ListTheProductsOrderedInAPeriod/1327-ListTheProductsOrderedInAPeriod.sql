-- Last updated: 31/10/2026, 19:05:55
# Write your MySQL query statement below
select product_name, sum(unit) as unit
from Products p join Orders o on o.product_id = p.product_id
where order_date like  '2020-02%' 
group by 1
having sum(unit)>=100;
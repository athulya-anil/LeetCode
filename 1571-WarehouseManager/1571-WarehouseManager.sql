-- Last updated: 31/10/2026, 19:04:50
# Write your MySQL query statement below
select name as warehouse_name, sum((Width*Length*Height) * units) as volume
from Warehouse w left join
Products p
on p.product_id = w.product_id
group by 1

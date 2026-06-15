-- Last updated: 14/06/2026, 23:02:34
# Write your MySQL query statement below
select product_name, year, price
from Product p join Sales s
on p.product_id = s.product_id
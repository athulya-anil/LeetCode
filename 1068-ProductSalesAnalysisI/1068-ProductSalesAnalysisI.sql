-- Last updated: 31/10/2026, 19:07:34
select product_name, year, price
from Product p join Sales s
on p.product_id = s.product_id
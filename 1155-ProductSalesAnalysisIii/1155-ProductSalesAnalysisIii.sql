-- Last updated: 14/06/2026, 23:02:32
# Write your MySQL query statement below
with cte as (
    select product_id, min(year) as first_year from Sales group by 1
)

select s.product_id, c.first_year, s.quantity, s.price
from Sales s join cte c 
on c.product_id = s.product_id and c.first_year = s.year
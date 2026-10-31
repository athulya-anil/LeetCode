-- Last updated: 31/10/2026, 19:07:29
with first_year_table as (
    select product_id, min(year) as first_year
from Sales
group by 1
)

select f.product_id, f.first_year, s.quantity, s.price
from first_year_table f join Sales s
on s.product_id = f.product_id and s.year = f.first_year

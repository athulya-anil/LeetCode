-- Last updated: 14/06/2026, 23:02:17
select p.product_id, coalesce(round(sum(p.price*u.units)/sum(units),2),0) as average_price
from Prices p left join UnitsSold u
on p.product_id = u.product_id
and purchase_date between start_date and end_date
group by 1
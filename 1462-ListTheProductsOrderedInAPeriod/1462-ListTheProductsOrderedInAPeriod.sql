-- Last updated: 10/12/2025, 07:40:36
with cte as 
(select product_id, sum(unit) as feb_unit from orders
where year(order_date)=2020 and month(order_date)=02
group by product_id)

select p.product_name, c.feb_unit as unit from cte c
left join products p on
p.product_id=c.product_id
where c.feb_unit>=100;
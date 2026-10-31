-- Last updated: 31/10/2026, 19:06:28
with cte as (select turn, person_id as ID, person_name as Name, weight, 
sum(weight) over(order by turn) as total_weight
from Queue)

select name as person_name
from cte
where total_weight <= 1000
order by total_weight desc 
limit 1

-- Last updated: 31/10/2026, 19:01:43
# Write your MySQL query statement below

select transaction_date, sum(case when amount%2 != 0 then amount else 0 end) as odd_sum, sum(case when amount%2 = 0 then amount else 0 end) as even_sum 
from transactions group by 1 order by 1

-- Last updated: 12/07/2026, 02:54:01
# Write your MySQL query statement below
with cte as(select transaction_id, 
DENSE_RANK() OVER(PARTITION BY day order by amount desc) as rk
from Transactions)

select transaction_id
from cte where rk = 1
order by 1
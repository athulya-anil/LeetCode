-- Last updated: 31/10/2026, 19:04:45
# Write your MySQL query statement below
with cte as(select account, sum(amount) as balance
from Transactions
group by 1)

select name, balance
from users u left join cte c 
on u.account = c.account
where balance > 10000
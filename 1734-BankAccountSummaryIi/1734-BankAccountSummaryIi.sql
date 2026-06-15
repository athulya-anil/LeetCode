-- Last updated: 14/06/2026, 23:02:01
# Write your MySQL query statement below
with cte as(
select name, sum(amount) as s from Transactions t join Users u on u.account = t.account group by 1 
)

select name as NAME, s as BALANCE from cte where s > 10000
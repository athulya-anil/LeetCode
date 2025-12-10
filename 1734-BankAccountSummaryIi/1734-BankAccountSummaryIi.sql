-- Last updated: 10/12/2025, 07:40:24
# Write your MySQL query statement below
with cte as(
select name, sum(amount) as s from Transactions t join Users u on u.account = t.account group by 1 
)

select name as NAME, s as BALANCE from cte where s > 10000
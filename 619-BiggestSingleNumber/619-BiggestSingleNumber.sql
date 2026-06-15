-- Last updated: 14/06/2026, 23:03:03
# Write your MySQL query statement below
with cte as (select num from MyNumbers group by 1 having count(num) = 1) 

select max(num) as num from cte
-- Last updated: 31/10/2026, 19:03:51
# Write your MySQL query statement below
select distinct customer_id
from Customers
where year = 2021 and revenue >0;
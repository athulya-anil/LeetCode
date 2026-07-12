-- Last updated: 12/07/2026, 02:53:59
# Write your MySQL query statement below
select distinct customer_id
from Customers
where year = 2021 and revenue >0;
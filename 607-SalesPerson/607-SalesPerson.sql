-- Last updated: 10/12/2025, 07:41:28
# Write your MySQL query statement below
select s.name
from SalesPerson s
where s.name not in
(select s.name from SalesPerson s join Orders o on o.sales_id = s.sales_id
join Company c on c.com_id = o.com_id where c.name = 'RED')
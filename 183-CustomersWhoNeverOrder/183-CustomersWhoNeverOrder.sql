-- Last updated: 10/07/2026, 11:59:36
# Write your MySQL query statement below
select name as 'Customers' from Customers where id not in (select customerID from Orders);
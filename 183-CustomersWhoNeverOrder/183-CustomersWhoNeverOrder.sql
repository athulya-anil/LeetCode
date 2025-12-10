-- Last updated: 10/12/2025, 07:42:19
# Write your MySQL query statement below
select name as 'Customers' from Customers where id not in (select customerID from Orders);
-- Last updated: 10/12/2025, 07:42:21
# Write your MySQL query statement below
select email as 'Email' from Person group by email having count(id)>1;
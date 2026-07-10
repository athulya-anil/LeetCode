-- Last updated: 10/07/2026, 11:59:37
# Write your MySQL query statement below
select email as Email 
from Person 
group by email 
having count(*)>1;
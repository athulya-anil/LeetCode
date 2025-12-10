-- Last updated: 10/12/2025, 07:41:38
# Write your MySQL query statement below

select e1.name from Employee e1 join Employee e2 on e1.id = e2.managerId 
group by e1.id, e1.name
HAVING count(e1.id) >=5
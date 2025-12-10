-- Last updated: 10/12/2025, 07:42:14
# Write your MySQL query statement below

select t2.id as 'Id' from Weather t1 join Weather t2 on datediff(t2.recordDate, t1.recordDate)=1 where t2.temperature>t1.temperature 
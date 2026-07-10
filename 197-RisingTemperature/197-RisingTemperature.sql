-- Last updated: 10/07/2026, 11:59:30
# Write your MySQL query statement below
select w1.id
from Weather w1 join Weather w2
on datediff(w1.recordDate,w2.recordDate) = 1
where w1.temperature>w2.temperature
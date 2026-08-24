-- Last updated: 24/08/2026, 12:56:04
# Write your MySQL query statement below
select distinct c1.seat_id
from Cinema c1 join Cinema c2
on abs(c1.seat_id - c2.seat_id)=1
where c1.free = 1 and c2.free = 1
order by seat_id

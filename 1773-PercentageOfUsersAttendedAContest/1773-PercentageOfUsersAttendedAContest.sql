-- Last updated: 14/06/2026, 23:02:00
select r.contest_id, round(count(r.user_id)/(select count(user_id) from Users) * 100,2) as percentage
from Users u join Register r 
on u.user_id = r.user_id
group by 1
order by 2 desc, 1
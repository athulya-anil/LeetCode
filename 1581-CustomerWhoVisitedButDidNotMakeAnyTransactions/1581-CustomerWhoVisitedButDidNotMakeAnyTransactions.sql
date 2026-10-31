-- Last updated: 31/10/2026, 19:04:47
# Write your MySQL query statement below
select customer_id, count(*) as count_no_trans
from Visits v left join Transactions t
on v.visit_id = t.visit_id
where t.visit_id is null
group by 1
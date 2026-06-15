-- Last updated: 14/06/2026, 23:03:08
# Write your MySQL query statement below
with cte as(
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
)

select id, count(*) as num from cte group by 1 order by num desc limit 1




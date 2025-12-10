-- Last updated: 10/12/2025, 07:41:30
# Write your MySQL query statement below
with cte as(
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id FROM RequestAccepted
)

select id, count(*) as num from cte group by 1 order by num desc limit 1




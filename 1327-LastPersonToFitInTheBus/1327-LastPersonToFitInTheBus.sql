-- Last updated: 14/06/2026, 23:02:19
# Write your MySQL query statement below

with cte as(
select turn, person_name, weight, sum(weight) over (ORDER BY turn) as total_weight from Queue order by turn
)

select person_name from cte where total_weight <= 1000 order by turn desc limit 1
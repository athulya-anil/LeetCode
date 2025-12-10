-- Last updated: 10/12/2025, 07:40:44
# Write your MySQL query statement below

with cte as(
select turn, person_name, weight, sum(weight) over (ORDER BY turn) as total_weight from Queue order by turn
)

select person_name from cte where total_weight <= 1000 order by turn desc limit 1
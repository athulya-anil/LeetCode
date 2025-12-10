-- Last updated: 10/12/2025, 07:41:25
# Write your MySQL query statement below

with cte as (
    select x, y, z,
        case
            when x+y > z and x+z > y and y+z > x then 'Yes'
        else 'No'
        end as triangle 
    from Triangle       
)

select * from cte
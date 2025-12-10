-- Last updated: 10/12/2025, 07:41:26
# Write your MySQL query statement below
with cte as(
    select id, case
        when p_id is null then 'Root'
        when id in (select p_id from Tree) then 'Inner'
        else 'Leaf'
        end as type
        from Tree
)

select * from cte


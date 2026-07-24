-- Last updated: 24/07/2026, 02:04:25
# Write your MySQL query statement below
select left_operand, operator, e.right_operand, (CASE
WHEN operator = '>' and vr.value > vl.value THEN 'true' 
WHEN operator = '<' and vr.value < vl.value THEN 'true' 
WHEN operator = '=' and vr.value = vl.value THEN 'true' ELSE 'false'
END) as value
from Expressions e join Variables vr
on e.left_operand = vr.name
join Variables vl
on e.right_operand = vl.name
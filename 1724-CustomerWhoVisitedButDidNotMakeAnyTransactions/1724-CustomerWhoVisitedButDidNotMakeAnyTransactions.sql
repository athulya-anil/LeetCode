-- Last updated: 10/12/2025, 07:40:25
# Write your MySQL query statement below

select v.customer_id, count(v.visit_id) as count_no_trans from Visits v left join Transactions t on v.visit_id = t.visit_id where t.visit_id IS NULL group by 1
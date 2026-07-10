-- Last updated: 10/07/2026, 11:56:23
# Write your MySQL query statement below
with spendings as(
    select s.user_id, s.product_id, sum(s.quantity * p.price) as spent
    from Sales s join Product p on s.product_id = p.product_id group by 1,2
),
max_spendings as(
    select user_id, max(spent) as max_spent from spendings group by 1
)

select s1.user_id, s1.product_id from max_spendings s join spendings s1 
on s1.user_id = s.user_id and spent = max_spent
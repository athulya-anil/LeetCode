-- Last updated: 14/06/2026, 23:02:20
# Write your MySQL query statement below
select DATE_FORMAT(trans_date, '%Y-%m') as month, country, count(state) as trans_count, sum(case when state = 'approved' then 1 else 0 end) as approved_count, sum(amount) as trans_total_amount, sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by 1,2
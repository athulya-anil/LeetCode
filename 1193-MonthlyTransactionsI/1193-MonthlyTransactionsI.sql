-- Last updated: 31/10/2026, 19:06:30
select date_format(trans_date, '%Y-%m') as month, country, count(state) as trans_count,sum(CASE WHEN state = 'approved' then 1 ELSE 0 END) as approved_count, sum(amount) as trans_total_amount, sum(CASE WHEN state = 'approved' then amount ELSE 0 END) as approved_total_amount
from Transactions
group by 1,2
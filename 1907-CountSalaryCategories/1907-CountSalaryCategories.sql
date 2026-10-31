-- Last updated: 31/10/2026, 19:03:30
select 'High Salary' as category, count(account_id) as 'accounts_count'
from Accounts 
where income > 50000
group by 1
UNION ALL
select 'Low Salary' as category, count(account_id) as 'accounts_count'
from Accounts 
where income < 20000
group by 1
UNION ALL
select 'Average Salary' as category, sum(CASE WHEN income >= 20000 and income <=50000 then 1 ELSE 0 END ) as 'accounts_count'
from Accounts 
group by 1
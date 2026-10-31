-- Last updated: 31/10/2026, 19:04:21
# Write your MySQL query statement below
select date_id, make_name, count(distinct lead_id) as unique_leads, count(distinct partner_id) as unique_partners
from DailySales
group by 1,2
order by 1
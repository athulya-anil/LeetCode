-- Last updated: 14/06/2026, 23:01:55
# Write your MySQL query statement below

select date_id, make_name, COUNT(distinct lead_id) as unique_leads,COUNT(distinct partner_id) as unique_partners from DailySales group by 1,2
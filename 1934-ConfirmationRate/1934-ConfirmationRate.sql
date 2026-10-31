-- Last updated: 31/10/2026, 19:03:23
select s.user_id, round(sum(CASE 
                            WHEN c.action = 'confirmed' then 1
                            ELSE 0
                            END)/count(*),2) as confirmation_rate
from Signups s left join Confirmations c
on s.user_id = c.user_id
group by 1
-- Last updated: 10/12/2025, 07:40:04
select s.user_id, 
ROUND(COALESCE(SUM(CASE WHEN action = 'confirmed' THEN 1 else 0 END)/count(s.user_id),0),2) as confirmation_rate from Confirmations c right join Signups s on s.user_id = c.user_id
group by s.user_id
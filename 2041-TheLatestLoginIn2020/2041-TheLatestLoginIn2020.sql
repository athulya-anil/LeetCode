-- Last updated: 14/06/2026, 23:01:46
# Write your MySQL query statement below

select user_id, max(time_stamp) as last_stamp from Logins where time_stamp like '2020%' group by 1
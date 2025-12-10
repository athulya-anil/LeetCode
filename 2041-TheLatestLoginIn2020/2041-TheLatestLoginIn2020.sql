-- Last updated: 10/12/2025, 07:40:08
# Write your MySQL query statement below

select user_id, max(time_stamp) as last_stamp from Logins where time_stamp like '2020%' group by 1
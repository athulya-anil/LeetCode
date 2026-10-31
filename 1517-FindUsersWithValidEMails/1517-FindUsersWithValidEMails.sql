-- Last updated: 31/10/2026, 19:05:03
# Write your MySQL query statement below
select user_id, name, mail
from Users
where REGEXP_LIKE (mail,'^[A-Za-z][A-Za-z0-9._-]*@leetcode[.]com$','c')

-- Last updated: 10/12/2025, 07:41:23
# Write your MySQL query statement below
select id, movie, description, rating
from Cinema where description != 'boring' and id%2 !=0
order by rating desc;
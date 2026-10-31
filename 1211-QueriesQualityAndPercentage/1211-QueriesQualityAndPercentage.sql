-- Last updated: 31/10/2026, 19:06:26
# Write your MySQL query statement below
select query_name, round(sum(rating/position)/count(*),2) as quality, round(sum(CASE WHEN rating < 3 then 1
                                                            ELSE 0
                                                            END)/count(*)*100,2) as poor_query_percentage
from Queries
group by 1
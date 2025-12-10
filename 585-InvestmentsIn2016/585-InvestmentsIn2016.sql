-- Last updated: 10/12/2025, 07:41:35
# Write your MySQL query statement below

WITH cte AS (
    SELECT DISTINCT i.pid, concat(i.lat,i.lon), concat(j.lat,j.lon) 
    FROM Insurance i
    JOIN Insurance j
      ON i.tiv_2015 = j.tiv_2015 AND i.pid != j.pid 
)

select ROUND(sum(tiv_2016),2) as tiv_2016 from Insurance where pid in (SELECT pid FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1) and pid in (select pid from cte);





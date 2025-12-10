-- Last updated: 10/12/2025, 07:40:31
# Write your MySQL query statement below
select name, COALESCE(sum(distance),0) as travelled_distance from Rides r right join Users u on u.id = r.user_id 
group by user_id
order by 2 desc, 1 
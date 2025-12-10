-- Last updated: 10/12/2025, 07:40:23
# Write your MySQL query statement below
select contest_id, ROUND(count(u.user_id)/(select count(user_id) from Users),4)*100 as percentage from Register r left join Users u on r.user_id = u.user_id group by 1 order by 2 desc, 1


-- Last updated: 24/08/2026, 12:47:14
# Write your MySQL query statement below
with cte as ((select team_id, team_name, (CASE
WHEN host_goals > guest_goals then 3
WHEN host_goals < guest_goals then 0
WHEN host_goals = guest_goals then 1
ELSE 0
END) as 'points'
from Teams t left join 
Matches m on t.team_id = m.host_team)
UNION ALL
(select team_id, team_name, (CASE
WHEN guest_goals > host_goals then 3
WHEN guest_goals < host_goals then 0
WHEN guest_goals = host_goals then 1
ELSE 0
END) as 'points'
from Teams t left join 
Matches m on t.team_id = m.guest_team))

select team_id, team_name, sum(points) as num_points from cte
group by 1,2
order by 3 desc, 1


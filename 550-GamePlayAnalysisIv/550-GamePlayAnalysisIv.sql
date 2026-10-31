-- Last updated: 31/10/2026, 19:07:08
with first_login as(
    select player_id, min(event_date) as event_date
    from Activity group by 1
)

select round(count(a.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from first_login f join Activity a
on f.player_id = a.player_id and datediff(a.event_date,f.event_date)=1

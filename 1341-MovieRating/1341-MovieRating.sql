-- Last updated: 31/10/2026, 19:05:45
(select name as results
from Users u left join MovieRating m
on u.user_id = m.user_id
group by 1
order by count(*) desc, 1
limit 1)

UNION ALL

(select title as results
from Movies u left join MovieRating m
on u.movie_id = m.movie_id
where created_at like '2020-02-%'
group by 1
order by avg(rating) desc,1
limit 1)
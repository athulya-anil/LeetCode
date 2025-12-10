-- Last updated: 10/12/2025, 07:40:35
# Write your MySQL query statement below

with cte as(
    select u.user_id, u.name, count(movie_id) as movies_rated from MovieRating r join Users u on u.user_id = r.user_id group by 1,2
),
highestavgrating as(
    select movie_id, avg(rating) as avg1 from MovieRating 
    where created_at between '2020-02-01' and '2020-02-29'
    group by 1

)

(select name as results from cte where movies_rated = (select max(movies_rated) from cte) order by name limit 1)
union all
(select title from highestavgrating h join Movies m on h.movie_id = m.movie_id where avg1 = (select max(avg1) from highestavgrating) order by title limit 1)





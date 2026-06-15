-- Last updated: 14/06/2026, 23:03:02
select id, movie, description, rating
from Cinema
where id%2 != 0 and description != 'boring' 
order by 4 desc
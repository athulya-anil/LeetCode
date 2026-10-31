-- Last updated: 31/10/2026, 19:06:50
select distinct author_id as id
from Views
where viewer_id=author_id
order by 1;
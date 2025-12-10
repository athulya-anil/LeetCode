-- Last updated: 10/12/2025, 07:41:24
select max(num) as num from MyNumbers
where num in
(select num from MyNumbers group by num having count(num)=1) ;
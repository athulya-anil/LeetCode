-- Last updated: 14/06/2026, 23:03:01
# Write your MySQL query statement below

select CASE
    WHEN id %2 = 0 then id - 1
    WHEN id %2 != 0 and id + 1 <= (select max(id) from Seat) then id + 1
    ELSE id
    END as id, student from Seat order by id
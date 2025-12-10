-- Last updated: 10/12/2025, 07:41:22
# Write your MySQL query statement below

select CASE
    WHEN id %2 = 0 then id - 1
    WHEN id %2 != 0 and id + 1 <= (select max(id) from Seat) then id + 1
    ELSE id
    END as id, student from Seat order by id
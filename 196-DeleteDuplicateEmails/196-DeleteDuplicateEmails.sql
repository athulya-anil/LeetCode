-- Last updated: 10/07/2026, 11:59:32
# Write your MySQL query statement below

delete p1
from Person p1 join Person p2
on p1.email = p2.email and p1.id > p2.id



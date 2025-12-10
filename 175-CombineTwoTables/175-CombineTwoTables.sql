-- Last updated: 10/12/2025, 07:42:27
# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state from Person p left join Address a on p.personId = a.personId
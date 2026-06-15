-- Last updated: 14/06/2026, 23:03:00
# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
             WHEN sex = 'm' THEN 'f'
             WHEN sex = 'f' THEN 'm'
          END;

-- Last updated: 10/12/2025, 07:41:21
# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
             WHEN sex = 'm' THEN 'f'
             WHEN sex = 'f' THEN 'm'
          END;

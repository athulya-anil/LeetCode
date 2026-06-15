-- Last updated: 14/06/2026, 23:01:50
WITH cte AS (
    SELECT 
        employee_id, 
        department_id, 
        primary_flag, 
        COUNT(*) OVER (PARTITION BY employee_id) AS in_departments
    FROM Employee
)
SELECT 
    employee_id, 
    department_id
FROM cte
WHERE 
    (in_departments = 1 OR primary_flag = 'Y')
ORDER BY employee_id;

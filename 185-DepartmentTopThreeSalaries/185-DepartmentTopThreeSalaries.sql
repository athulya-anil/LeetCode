-- Last updated: 10/07/2026, 11:59:33
WITH RankedSalaries AS (
    SELECT 
        e.departmentId, 
        e.name AS Employee, 
        e.salary AS Salary, 
        d.name AS Department,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) AS rank1
    FROM 
        Employee e
    JOIN 
        Department d 
    ON 
        e.departmentId = d.id
)
SELECT 
    Department, 
    Employee, 
    Salary
FROM 
    RankedSalaries
WHERE 
    rank1 <= 3
ORDER BY 
    Department, Salary DESC;

-- Last updated: 10/12/2025, 07:40:07
WITH cte AS (
    SELECT 
        account_id, 
        income, 
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category
    FROM Accounts
),
cte2 AS (
    SELECT 
        SUM(CASE WHEN category = 'Low Salary' THEN 1 ELSE 0 END) AS low_count, 
        SUM(CASE WHEN category = 'Average Salary' THEN 1 ELSE 0 END) AS average_count, 
        SUM(CASE WHEN category = 'High Salary' THEN 1 ELSE 0 END) AS high_count 
    FROM cte
)
SELECT 
    'Low Salary' AS category, low_count AS accounts_count 
FROM cte2
UNION ALL
SELECT 
    'Average Salary', average_count 
FROM cte2
UNION ALL
SELECT 
    'High Salary', high_count 
FROM cte2;

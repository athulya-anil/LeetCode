-- Last updated: 31/10/2026, 19:05:34
/* Write your PL/SQL query statement below */
SELECT stock_name, SUM(CASE WHEN operation = 'Buy' THEN -price ELSE price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
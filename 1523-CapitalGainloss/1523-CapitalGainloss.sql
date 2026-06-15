-- Last updated: 14/06/2026, 23:02:09
/* Write your PL/SQL query statement below */
SELECT stock_name, SUM(CASE WHEN operation = 'Buy' THEN -price ELSE price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;
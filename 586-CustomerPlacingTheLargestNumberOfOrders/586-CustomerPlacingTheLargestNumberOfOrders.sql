-- Last updated: 10/12/2025, 07:41:34
# Write your MySQL query statement below


SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC limit 1;

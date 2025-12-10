-- Last updated: 10/12/2025, 07:40:41
WITH cte AS (
SELECT
p.product_id,
p.start_date,
p.end_date,
p.price,
COALESCE(u.purchase_date, p.start_date) AS p_date,
COALESCE(u.units, 0) AS units
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id
)
SELECT
product_id,
COALESCE(ROUND(SUM(units * price) / SUM(units), 2), 0) AS average_price
FROM cte
WHERE p_date BETWEEN start_date AND end_date OR price = 0
GROUP BY product_id;
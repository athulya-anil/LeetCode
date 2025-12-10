-- Last updated: 10/12/2025, 07:40:57
WITH FirstQuarterSales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
),
OtherSales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)
SELECT p.product_id, p.product_name
FROM Product AS p
JOIN FirstQuarterSales AS fqs
ON p.product_id = fqs.product_id
WHERE p.product_id NOT IN (SELECT product_id FROM OtherSales);

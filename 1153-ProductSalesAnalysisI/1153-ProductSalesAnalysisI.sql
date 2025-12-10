-- Last updated: 10/12/2025, 07:41:00
# Write your MySQL query statement below
select p.product_name, s.year, s.price from Product p join Sales s on s.product_id=p.product_id 
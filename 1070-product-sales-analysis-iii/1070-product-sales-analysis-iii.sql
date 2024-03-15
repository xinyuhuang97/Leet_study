# Write your MySQL query statement below

select s.product_id, s.year as first_year, s.quantity, s.price
from Sales s
join Product p
on s.product_id=p.product_id
where (s.product_id, s.year) in(
                            select Sales.product_id , min(Sales.year)
                            from Sales
                            group by Sales.product_id)
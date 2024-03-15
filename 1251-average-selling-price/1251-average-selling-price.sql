# Write your MySQL query statement below

select p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
from Prices p
left join UnitsSold u
on DATEDIFF(p.end_date,u.purchase_date)>=0 and DATEDIFF(u.purchase_date, p.start_date)>=0 and p.product_id=u.product_id
group by p.product_id
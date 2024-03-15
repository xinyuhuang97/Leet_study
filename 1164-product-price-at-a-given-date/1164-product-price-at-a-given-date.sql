# Write your MySQL query statement below

select product_id, new_price as price 
from Products where (product_id,change_date) 
in (
    select product_id , max(change_date) as date 
    from Products 
    where change_date <='2019-08-16' 
    group by product_id)

UNION
select p1.product_id, 10 as price
from Products p1
where Datediff('2019-08-16',change_date)<0 and Not EXISTS (
                        select *
                        from Products p2
                        where Datediff('2019-08-16',change_date)>=0 and p1.product_id=p2.product_id)
group by product_id



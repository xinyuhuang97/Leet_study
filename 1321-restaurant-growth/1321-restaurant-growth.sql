# Write your MySQL query statement below
select  c1.visited_on, (select sum(c2.amount) from Customer c2 where Datediff(c1.visited_on,c2.visited_on)<=6 and Datediff(c1.visited_on,c2.visited_on)>=0) as amount,round((select sum(c2.amount)/7 from Customer c2 where Datediff(c1.visited_on,c2.visited_on )<=6  and Datediff(c1.visited_on,c2.visited_on)>=0),2) as average_amount
from Customer c1
where Datediff(c1.visited_on ,(
                    select min(visited_on)
                    from Customer))>=6
group by c1.visited_on
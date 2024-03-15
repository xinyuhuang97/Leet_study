# Write your MySQL query statement below
select p1.person_name
from (
        select person_name ,sum(weight) over( order by Turn) as cumu from Queue) p1
where p1.cumu<=1000
order by p1.cumu DESC
Limit 1

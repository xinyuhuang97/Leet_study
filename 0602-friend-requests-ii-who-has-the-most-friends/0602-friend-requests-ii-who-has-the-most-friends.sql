# Write your MySQL query statement below

With allid as (
(select requester_id as id from RequestAccepted)
union all
(select accepter_id as id from RequestAccepted))
select id, count(*)as num
from allid
group by id
order by count(*) DESC
limit 1
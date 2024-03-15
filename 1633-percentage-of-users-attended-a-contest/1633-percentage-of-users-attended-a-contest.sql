# Write your MySQL query statement below

with Number as (
select count(Users.user_id) as number
from Users) 
select r.contest_id, ROUND(count(u.user_id)/n.number*100,2) as percentage
from Users u
join Register r
on u.user_id=r.user_id
CROSS JOIN Number n
group by r.contest_id
order by percentage DESC, contest_id ASC

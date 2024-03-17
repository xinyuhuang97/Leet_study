# Write your MySQL query statement below
SELECT IFNULL(
(select e1.salary 
from Employee e1
where 1= (
                select count(distinct e2.salary)
                from Employee e2
                where e1.salary<e2.salary)

order by e1.id DESC
limit 1)
,NULL) as SecondHighestSalary


# Write your MySQL query statement below

select d.name as Department, e1.name as Employee, e1.salary as Salary
from Employee e1
join Department d
on e1.departmentID=d.id
where 3>(
        select count(distinct e2.salary)
        from Employee e2
        where e1.departmentID=e2.departmentID and e1.salary<e2.salary
)



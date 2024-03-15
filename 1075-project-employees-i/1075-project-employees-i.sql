# Write your MySQL query statement below

select p.project_id, IFNULL(ROUND(sum(IFNULL(e.experience_years,0) )/sum(IF(e.experience_years is null,0,1) ),2) ,0) as average_years
from Project p
left join Employee e
on p.employee_id=e.employee_id
group by p.project_id
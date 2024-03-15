# Write your MySQL query statement below

select query_name, Round(avg(rating/position),2) as quality,
Round(sum(if(rating<3,1,0))/count(result)*100,2) as poor_query_percentage
from Queries
where NOT(query_name is NULL)
group by query_name
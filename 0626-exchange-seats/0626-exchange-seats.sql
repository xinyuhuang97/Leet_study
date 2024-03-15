# Write your MySQL query statement below

with cte as (
            select id, student, 
            LAG(id) OVER(ORDER BY id) as previous_id,
            Lead(id) OVER(ORDER BY id) as next_id
            from Seat 
)
select COALESCE( 
            CASE
                WHEN (id%2=1 and next_id  is not NULL) then next_id
                WHEN (id%2=0 )then previous_id
                ELSE ID
            END,
            id
) as id, student
from cte
order by id ASC

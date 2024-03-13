# Write your MySQL query statement below
select customer.name
from customer
where customer.referee_id IS NULL OR NOT (customer.referee_id=2)
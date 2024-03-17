# Write your MySQL query statement below

select patient_id, patient_name, conditions
from Patients
where REGEXP_LIKE(conditions,'(^DIAB1)|( +DIAB1)')
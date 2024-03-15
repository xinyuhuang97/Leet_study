# Write your MySQL query statement below

WITH count_action AS (
    SELECT s.user_id, 
        SUM(
            CASE
                WHEN c.action = 'confirmed' THEN 1
                ELSE 0
            END
        ) AS success,
        COUNT(c.user_id) AS total
    FROM Signups s
    left JOIN Confirmations c 
    ON s.user_id = c.user_id
    GROUP BY s.user_id
)

SELECT user_id, 
       IFNULL(ROUND(success * 1.0 / total, 2),0) AS confirmation_rate
FROM count_action;
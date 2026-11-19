-- Total aid, number of records and average amount for each aid type group.
-- Negative amounts are included, so the totals are net amounts.
SELECT
    aid_type_group_name,
    COUNT(*)                       AS records,
    SUM(current_amount)            AS total_amount,
    ROUND(AVG(current_amount), 0)  AS average_amount
FROM aid
GROUP BY aid_type_group_name
ORDER BY total_amount DESC;
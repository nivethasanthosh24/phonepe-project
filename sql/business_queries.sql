-- 1. Top 10 states by total transaction amount
SELECT state, SUM(amount) AS total_transaction_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_transaction_amount DESC
LIMIT 10;


-- 2. Top 10 states by transaction count
SELECT state, SUM(count) AS total_transaction_count
FROM aggregated_transaction
GROUP BY state
ORDER BY total_transaction_count DESC
LIMIT 10;


-- 3. Most popular transaction type by amount
SELECT type, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY type
ORDER BY total_amount DESC;


-- 4. Most popular transaction type by count
SELECT type, SUM(count) AS total_count
FROM aggregated_transaction
GROUP BY type
ORDER BY total_count DESC;


-- 5. Year-wise transaction growth
SELECT year, SUM(amount) AS total_amount, SUM(count) AS total_count
FROM aggregated_transaction
GROUP BY year
ORDER BY year;


-- 6. Quarter-wise transaction trend
SELECT year, quarter, SUM(amount) AS total_amount, SUM(count) AS total_count
FROM aggregated_transaction
GROUP BY year, quarter
ORDER BY year, quarter;


-- 7. Top 10 districts by transaction amount
SELECT district, state, SUM(amount) AS total_amount
FROM map_transaction
GROUP BY district, state
ORDER BY total_amount DESC
LIMIT 10;


-- 8. Top 10 districts by transaction count
SELECT district, state, SUM(count) AS total_count
FROM map_transaction
GROUP BY district, state
ORDER BY total_count DESC
LIMIT 10;


-- 9. State-wise registered users
SELECT state, SUM(users) AS total_registered_users
FROM map_user
GROUP BY state
ORDER BY total_registered_users DESC;


-- 10. District-wise app opens
SELECT district, state, SUM(appopens) AS total_app_opens
FROM map_user
GROUP BY district, state
ORDER BY total_app_opens DESC
LIMIT 10;


-- 11. Mobile brand-wise user count
SELECT brand, SUM(count) AS total_users
FROM aggregated_user
GROUP BY brand
ORDER BY total_users DESC;


-- 12. Insurance amount by state
SELECT state, SUM(amount) AS total_insurance_amount
FROM aggregated_insurance
GROUP BY state
ORDER BY total_insurance_amount DESC;


-- 13. Insurance count by state
SELECT state, SUM(count) AS total_insurance_count
FROM aggregated_insurance
GROUP BY state
ORDER BY total_insurance_count DESC;


-- 14. District-wise insurance performance
SELECT district, state, SUM(amount) AS total_insurance_amount
FROM map_insurance
GROUP BY district, state
ORDER BY total_insurance_amount DESC
LIMIT 10;


-- 15. Low-performing states by transaction amount
SELECT state, SUM(amount) AS total_amount
FROM aggregated_transaction
GROUP BY state
ORDER BY total_amount ASC
LIMIT 10;
-- Displays the 3 cities with the highest average temperatures between July and August.
SELECT city, temperature
FROM temperatures
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;

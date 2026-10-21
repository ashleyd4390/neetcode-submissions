SELECT customer_id, customer_name
FROM (
    SELECT c.customer_id, c.customer_name,
        COUNT(*) FILTER (WHERE o.product_name = 'A') AS a_count,
        COUNT(*) FILTER (WHERE o.product_name = 'B') AS b_count,
        COUNT(*) FILTER (WHERE o.product_name = 'C') AS c_count
    FROM orders AS o
    JOIN customers AS c ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name
) AS counts
WHERE a_count > 0 AND b_count > 0 AND c_count = 0
ORDER BY customer_name;
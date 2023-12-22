
SELECT * FROM Shippings
WHERE NOT status = 'Pending';

SELECT * FROM Shippings
WHERE status = 'Pending';

SELECT * FROM Shippings
WHERE customer = 2;

SELECT * FROM Customers
WHERE country = 'USA'
AND (age = 32 OR age = 22);

SELECT * FROM Customers
ORDER BY customer_id DESC

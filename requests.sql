SELECT COUNT(amount) FROM Orders;
SELECT AVG(amount) FROM Orders;
SELECT MAX(amount) FROM Orders;
SELECT MIN(amount) FROM Orders;

SELECT first_name, country
FROM Customers;

SELECT last_name, age
FROM Customers WHERE country = 'USA';

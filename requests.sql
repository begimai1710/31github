SELECT COUNT(amount) FROM Orders;
SELECT AVG(amount) FROM Orders;
SELECT MAX(amount) FROM Orders;
SELECT MIN(amount) FROM Orders;

SELECT first_name, country
FROM Customers;

SELECT last_name, age
FROM Customers WHERE country = 'USA';


Insert the missing statement to get all the columns from the Customers table.
SELECT from Customers;

Write a statement that will select the City column from the Customers table.
SELECT City FROM Customers;

Select all the different values from the Country column in the Customers table.
SELECT DISTINCT Country FROM Customers;

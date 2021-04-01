SELECT COUNT(*) FROM users;

SELECT AVG(age) FROM users
WHERE age >= 30;

SELECT count(age) FROM users
WHERE age >= 30;

SELECT first_name, MAX(balance), age FROM users;

SELECT SUM(balance), count(), AVG(balance) from users
where age<30;
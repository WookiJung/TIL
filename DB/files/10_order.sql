-- SELECT * from users
-- order by age DESC limit 20;

SELECT * from users
order by last_name, age asc limit 20;

select first_name, last_name, balance from users
order by balance desc limit 10;
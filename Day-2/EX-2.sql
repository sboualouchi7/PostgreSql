--1

SELECT * FROM customer;

--2 pour afficher le nom et le prenom dans un seul champs "full_name"

SELECT first_name || ' ' || last_name AS full_name FROM customer;

--3 afficher les dates sans duplication

SELECT DISTINCT create_date FROM customer;

--4 

SELECT * FROM customer ORDER BY first_name DESC;

--5

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;


--6

SELECT address, phone FROM address WHERE district = 'Texas';

--7

SELECT  * FROM film WHERE film_id =1 OR film_id=150


--8

SELECT film_id, title, description, length, rental_rate FROM film WHERE title = 'The Godfather';

--9

SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'the%';

--10

SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10

--11

SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate > (
    SELECT MIN(rental_rate) FROM film
)
ORDER BY rental_rate ASC
LIMIT 10;

--12

SELECT c.first_name , c.last_name, p.amount, p.payment_date From customer c INNER JOIN payment p ON c.customer_id = p.customer_id ORDER BY c.customer_id;

--13

SELECT f.film_id, f.title FROM film f
WHERE NOT EXISTS (
    SELECT 1 FROM inventory i
    WHERE i.film_id = f.film_id
);

--14
SELECT ci.city, co.country FROM city ci JOIN country co ON ci.country_id = co.country_id;






--1
--aficher la table
SELECT * FROM FILM ;
--changer la langue
UPDATE film SET language_id = 2 WHERE film_id IN (1, 2, 3, 4, 5);

SELECT * FROM FILM ;

--2
SELECT * FROM customer ;

/*
Foreign keys in customer table:

store_id && address_id 

we must provide valid store_id and address_id values
*/

--3
DROP TABLE customer_review;

--4

SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

--5

SELECT f.title, f.rental_rate FROM film f JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NULL ORDER BY f.rental_rate DESC
LIMIT 30;

--6

--6.1

SELECT film.title, film.description FROM film JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE (film.description ILIKE '%sumo wrestler%' )
AND actor.first_name = 'Penelope' AND actor.last_name = 'Monroe';

--6.2

SELECT film.title, film.description, film.length, film.rating FROM film WHERE film.length < 60
AND film.rating = 'R'
AND film.description ILIKE '%documentary%';

--6.3 && 6.4 i d'ont know



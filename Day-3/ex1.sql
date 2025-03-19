--1
SELECT * FROM 	language;

--2

SELECT f.title, f.description, l.name FROM film f JOIN language l ON f.language_id = l.language_id ; 

--3

SELECT f.title, f.description, l.name FROM film f RIGHT JOIN language l ON f.language_id = l.language_id ; 

--4

CREATE TABLE new_film (id SERIAL PRIMARY KEY, name VARCHAR(55) NOT NULL);

-- Insert some films 
INSERT INTO new_film (name) VALUES ('The Matrix');
INSERT INTO new_film (name) VALUES ('Legender');
INSERT INTO new_film (name) VALUES ('Oppenheimer');


-- 5
CREATE TABLE customer_review ( review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INTEGER CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM new_film ;

--6

--1er

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES (1, 1, 'REVIEW SALMAN MATRIX :)',8,'The Matrix IS THE MOSTE BEAUTIFUL FILM IN THE WORLD HHHH');

--2eme

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES (2,1,'REVIEW SALMAN :) ',9,'The Matrix IS THE MOSTE BEAUTIFUL FILM IN THE WORLD HHHH')

--7 table review before deleting film

SELECT * FROM customer_review;

--deleting 

DELETE FROM new_film WHERE id = 1;


--table review after deleting film

SELECT * FROM customer_review; 

-- we notice that the review is deleting automaticly after deleting the film


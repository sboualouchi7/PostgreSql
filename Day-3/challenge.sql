--PART 1
--1

CREATE TABLE Customer (id SERIAL PRIMARY KEY,first_name VARCHAR(50) ,last_name VARCHAR(50) NOT NULL);

CREATE TABLE CustomerProfile (id SERIAL PRIMARY KEY,isLoggedIn BOOLEAN DEFAULT false, customer_id INT UNIQUE REFERENCES Customer(id));

--2 
INSERT INTO Customer (first_name, last_name) VALUES('John', 'Doe'),('Jerome', 'Lalu'),('Lea', 'Rive');

SELECT * FROM customer;

--3

INSERT INTO CustomerProfile (isLoggedIn, customer_id) VALUES
(true, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe')),
(false, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

SELECT * from CustomerProfile ;

--4
--4.1
SELECT c.first_name FROM Customer c JOIN CustomerProfile cp ON c.id = cp.customer_id WHERE cp.isLoggedIn = true;

--4.2
SELECT c.first_name, cp.isLoggedIn FROM Customer c LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id;

--4.3
SELECT COUNT(*) FROM Customer c LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id WHERE cp.isLoggedIn = false OR cp.isLoggedIn IS NULL;


--PART 2

--1
CREATE TABLE Book (book_id SERIAL PRIMARY KEY, title VARCHAR(100) NOT NULL, author VARCHAR(100) NOT NULL);
--2
INSERT INTO Book (title, author) VALUES ('Alice In Wonderland', 'Lewis Carroll'), ('Harry Potter', 'J.K Rowling'), ('To kill a mockingbird', 'Harper Lee');
--3
CREATE TABLE Student ( student_id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL UNIQUE,age INT CHECK (age <= 15));
--4
INSERT INTO Student (name, age) VALUES('John', 12),('Lera', 11),('Patrick', 10),('Bob', 14);

--5
CREATE TABLE Library (book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);

--6

INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date) VALUES
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
((SELECT book_id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

SELECT * FROM Library;

SELECT s.name, b.titleFROM Library l JOIN Student s ON l.student_fk_id = s.student_id JOIN Book b ON l.book_fk_id = b.book_id;
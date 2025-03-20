--
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL
);

INSERT INTO items (item_id, name, price) VALUES
    (4, 'Small Desk', 100),
    (5, 'Large desk', 300),
    (6, 'Fan', 80);
INSERT INTO customers (customer_id, firstname, lastname) VALUES
    (1, 'Greg', 'Jones'),
    (2, 'Sandra', 'Jones'),
    (3, 'Scott', 'Scott'),
    (4, 'Trevor', 'Green'),
    (5, 'Melanie', 'Johnson');
	
SELECT * FROM items;


SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price <= 300;


SELECT * FROM customers WHERE lastname = 'Smith';


SELECT * FROM customers WHERE lastname = 'Jones';

SELECT * FROM customers WHERE firstname != 'Scott';

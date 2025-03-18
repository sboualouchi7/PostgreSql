--1 MIN-----MAX

SELECT * FROM items ORDER BY price ASC;

--2

SELECT * FROM items WHERE price >= 80 ORDER BY price DESC;

--3 DE A----Z

SELECT firstname, lastname FROM customers ORDER BY firstname ASC LIMIT 3;

--4 DE Z-----A

SELECT lastname FROM customers ORDER BY lastname DESC

 
CREATE TABLE student (
    id INT PRIMARY KEY,
    fullName VARCHAR(100),
    age INT
);

INSERT INTO student (id, fullName, age) VALUES
(1, 'Ridwan Johnson', 18), 
(2, 'Brian Nyikuli', 19), 
(3, 'Cara Akinyi', 21);

UPDATE student
SET age = 20
WHERE id = 2;
To create a MySQL database named "users", you can use the following query
CREATE DATABASE users;

To design a table "users" with the specified columns, you can use the following query
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(255)
);

Insert sample data into the "users" table:
INSERT INTO users (id, name, email, role) VALUES
(1, 'John Doe', 'john.doe@example.com', 'admin'),
(2, 'Jane Smith', 'jane.smith@example.com', 'user'),
(3, 'Bob Johnson', 'bob.johnson@example.com', 'user');

Retrieve all users from the "users" table:
SELECT * FROM users;

Retrieve a specific user by their ID
SELECT * FROM users WHERE id = 1;
Replace 1 with the desired user ID to retrieve a specific user.
These queries will help you interact with the MySQL database and perform the required operations on the "users" table.

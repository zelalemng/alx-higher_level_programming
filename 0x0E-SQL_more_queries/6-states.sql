-- creates the database hbtn_0d_usa and the table states on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- usa a database
USE hbtn_0d_usa;
-- create a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL
	AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY
KEY(ID));

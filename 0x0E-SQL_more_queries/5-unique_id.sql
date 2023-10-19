-- creates a table with specific columns whrer id must be unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

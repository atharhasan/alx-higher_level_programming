-- creates the table unique_id on your MySQL server.
CREATE table IF NOT EXISTS unique_id (
	id INT NOT NULL UNIQUE DEFAULT 1,
	name VARCHAR(256)
);

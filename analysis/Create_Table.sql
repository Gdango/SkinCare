-- create table for dry skin
CREATE TABLE Dry (brand character varying(100), product_name character varying(100), rating character varying(50), min_amount character varying(50), max_amount character varying(50));

-- to copy table from csv into table Dry;
--psql -h <end point> postgres -d <db name> -c "\copy Dry FROM 'path to file' with DELIMITER ',';"

-- create primary key for table
ALTER TABLE Dry ADD COLUMN ID SERIAL PRIMARY KEY;
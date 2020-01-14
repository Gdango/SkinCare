DROP TABLE Dry;

CREATE TABLE Dry
(
  brand character varying(100),
  product_name character varying(100),
  rating character varying(50),
  price character varying(50)                                     
  --max_amount character varying(50)
 );                 

-- imported table from command line using \copy:
--psql -h <host> -U <username> -d <dbname> -c "\copy Dry FROM 'path to file' with delimiter ',';"

 
       

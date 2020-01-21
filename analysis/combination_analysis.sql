-- find out which brand has the most product with rating 4 or higher
SELECT brand, count(brand) As num_prod, AVG(rating) As avg_rating from combination where rating >= 4 group by brand order by num_prod desc;
--shows most of the Clinique product has rating 4 or higher for combination skin


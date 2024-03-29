# Introduction

Currently the most frequent retail sites do not carry all the brands and products, so I have to visit multiple websites when I want to look for new products.  Retail sites also have sales throughout the year, so if we want the best price, we would have to check multiple sites to make sure we're getting the best deal.

# Potential Solutions

Create a centralize database that host data from the most frequent websites.  That way users could see all the information on one page.

# System Design and Architecture
Lambda --> RDS 1 --> RDS 2 (reporting database)

Lambda will scrape retail sites every 24 hours and update the tables as need. 

The number of database will be based on the number of retail sites being scraped.  

# Challenges

One of the challenges is the site might error out if the client is pulling the request while the database is being updated. To prevent that issue, two tables will be created to store the skincare products.  Table 1 will store the data and interact with the client.  Table 2 will be the working data for the update.  Once Table 2 finish updating, it will transfer the data to Table 1.  That will the interruption time will be minimal.

# Test Plan
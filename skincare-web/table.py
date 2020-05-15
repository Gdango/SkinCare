from flask_table import Table, Col

class Results(Table):
    brand = Col('Brand')
    prod_name = Col('Product Name')
    Price = Col('Price')
    Rating = Col('Rating')

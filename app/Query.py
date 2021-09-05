class Query:
    def __init__(self, skin_type, rating, price, order_by):
        self.skin_type = skin_type
        self.rating = rating
        self.price = price
        self.order_by = order_by

    def _desired_price(self):
        if self.price == '25-to-70':
            query = f'''select * from {self.skin_type} 
                    where (rating >= {self.rating}) 
                    and (max_amount between {self.price.split('-to-', 1)[0]} 
                    and {self.price.split('-to-',1)[1]})
                    order by {self.order_by};'''
        elif self.price == '70':
            query = f'''select * from {self.skin_type}
                    where (rating >= {self.rating})
                    and max_amount >= 70
                    order by {self.order_by};'''

        elif self.price == '25':
            query = f'''select * from {self.skin_type}
                    where (rating >= {self.rating})
                    and max_amount <= 25
                    order by {self.order_by};'''
        return query

    def create_table(self):
        query = f'''create table UltaProducts (
            product_id INTEGER(4294967295)
            brand VARCHAR (200),
            prod_name VARCHAR (200),
            rating FOAT(2),
        )'''

        return query

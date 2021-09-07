class Query(self):

    def _desired_price(self, skin_type, price, rating, order_by):
        if price == '25-to-70':
            query = f'''select * from {skin_type} 
                    where (rating >= {rating}) 
                    and (max_amount between {price.split('-to-', 1)[0]} 
                    and {price.split('-to-',1)[1]})
                    order by {order_by};'''
        elif price == '70':
            query = f'''select * from {skin_type}
                    where (rating >= {rating})
                    and max_amount >= 70
                    order by {order_by};'''

        elif price == '25':
            query = f'''select * from {skin_type}
                    where (rating >= {rating})
                    and max_amount <= 25
                    order by {order_by};'''
        return query

    def create_table(self, table_name):
        query = f'''create table {table_name} (
            line_id serial primary key,
            product_id INT,
            brand VARCHAR (200),
            prod_name VARCHAR (200),
            rating FOAT(2),
            min_amount float,
            max_amount float, 
            product_type VARCHAR (200),
            skin_type VARCHAR (200)
        )'''
        return query

    def update_table(self, table_name, data):
        query = f'''update {table_name}
        set product_id = data[0],
        brand = data[1],
        prod_name = data[2],
        rating = data[3],
        min_amount = data[4],
        max_amount = data[5],
        product_type = data[6],
        skin_type = data[7]'''

        return query
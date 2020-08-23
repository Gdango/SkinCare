import psycopg2
import access

split_input = access.key()
A = split_input[0]
B = split_input[1]
C = split_input[2]
D = split_input[3]
conn = psycopg2.connect(host=A, database=B, user=C, password=D)
cur = conn.cursor()

def get_info(query):
    
    cur.execute(query)
    rows = cur.fetchall()

    brand = []
    prod_name = []
    price = []
    rating = []

    for row in range(0, len(rows)):
        
        brand.append(rows[row][0])
        prod_name.append(rows[row][1])
        price.append(rows[row][2])
        rating.append(rows[row][3])
    
    #row = {'Brand': brand, 'Product': prod_name, 'Price': price, 'Rating': rating}
    row = [brand, prod_name, rating, price]
    
    cur.close()

    return row


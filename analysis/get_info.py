import psycopg2

user_input = input('Host=? database=? user=? password=?')
split_input = user_input.split()
A = split_input[0]
B = split_input[1]
C = split_input[2]
D = split_input[3]
conn = psycopg2.connect(host=A, database=B, user=C, password=D)
cur = conn.cursor()

def get_info(query):
    
    cur.execute(query)
    rows = cur.fetchall()
    num_brand = []
    brand_name = []
    for row in range(0, len(rows)):
        num_brand.append(rows[row][1])
        brand_name.append(rows[row][0])
    
    cur.close()
    
    return num_brand, brand_name
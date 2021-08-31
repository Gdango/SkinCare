import psycopg2
import access

def update_table():
    split_input = access.key()
    A = split_input[0]
    B = split_input[1]
    C = split_input[2]
    D = split_input[3]

    conn = psycopg2.connect(host=A, database=B, user=C, password=D)
    cur = conn.cursor()
    

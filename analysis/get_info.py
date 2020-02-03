import psycopg2
import matplotlib.pyplot as plt
import numpy as np

A,B,C = input('Host=?, database=?, user=?, password=?')
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
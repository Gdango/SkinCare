import psycopg2
import os

def access_database():
    host = os.environ['AWS_HOST']
    database = os.environ['AWS_SKINAPP_DATABASE']
    user = os.environ['AWS_SKINAPP_USER']
    password = os.environ['AWS_SKINAPP_PASSWORD']

    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cur = conn.cursor()
    
def main():
    access_database()
    Query.create_table()

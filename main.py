import psycopg2 as pg2

secret = "**********"
conn = pg2.connect(database='dvdrental', user='postgres,password=secret')
cur = conn.cursor()
cur.execute('SELECT * FROM payment')
cur.fetchone()
conn.close()

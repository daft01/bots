import psycopg2

conn = psycopg2.connect("dbname=bot user=danielmorales")
cur = conn.cursor()

sql = "INSERT INTO follow(username) VALUES('dafth01')"

cur.execute(sql)

print(id)

conn.commit()

cur.close()
conn.close()


# https://www.psycopg.org/docs/usage.html
import psycopg2

# Connect to existing database
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)
if conn:
    print(f"Conn: {conn}")
else:
    print("NO CONNECTION")
# Open cursor to perform database operation
cur = conn.cursor()

# Query the database
sql = "SELECT * FROM publisher;"
# sql = "SELECT * FROM employee;"

cur.execute(sql)
print(f"SQL: {sql}")
print("============")
rows = cur.fetchall()
if not len(rows):
    print("empty")
for row in rows:
    print(row)
print("============")

# Close communications with database
cur.close()
conn.close()

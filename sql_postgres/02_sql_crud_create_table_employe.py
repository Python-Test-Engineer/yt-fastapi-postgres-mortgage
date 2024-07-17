import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="host.docker.internal",
)
if conn:
    print(f"Conn: {conn}\n")
else:
    print("NO CONNECTION\n")

cursor = conn.cursor()

TABLE_NAME = "employee"

cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

# Creating table as per requirement
sql = f"""CREATE TABLE {TABLE_NAME} (
				name VARCHAR(255) NOT NULL,
            state VARCHAR(255) NOT NULL
)"""

try:
    cursor.execute(sql)
    conn.commit()
    print(f"{TABLE_NAME} table created successfully........\n")

except Exception as e:
    print(f"Error {e}")

cursor.close()
conn.close()
print("PostgreSQL connection is closed")

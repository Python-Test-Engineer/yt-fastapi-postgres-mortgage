import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="postgres-test",
    user="postgres",
    password="postgres",
    host="localhost",
)
if conn:
    print(f"Conn: {conn}\n")
else:
    print("NO CONNECTION\n")

cursor = conn.cursor()

TABLE_NAME = "employee_test"

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

try:
    sql = f"""
    ALTER TABLE IF EXISTS public.employee
    ADD CONSTRAINT "unique employee constraint" UNIQUE (name);
            
    """
    cursor.execute(sql)
    conn.commit()
    print(f"{TABLE_NAME} table created successfully........\n")

except Exception as e:
    print(f"Error {e}")

cursor.close()
conn.close()
print("PostgreSQL connection is closed")

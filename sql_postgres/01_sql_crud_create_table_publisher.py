import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    # host="host.docker.internal",
    host="localhost",  # seems to work now
)
if conn:
    print(f"Conn: {conn}\n")
else:
    print("NO CONNECTION\n")

cursor = conn.cursor()

TABLE_NAME = "publisher"

# cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

# Creating table as per requirement
sql = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
				publisher_id SERIAL PRIMARY KEY,
				publisher_name VARCHAR(255) NOT NULL,
				publisher_estd INT,
				publsiher_location VARCHAR(255),
				publsiher_type VARCHAR(255)
)"""

try:
    cursor.execute(sql)
    conn.commit()
    print(f"{TABLE_NAME} table created successfully........\n")

except Exception as e:
    print(f"Error {e}")


try:
    postgres_insert_query = f""" INSERT INTO {TABLE_NAME} (publisher_id,
	publisher_name, publisher_estd, publsiher_location, publsiher_type)
	VALUES (%s,%s,%s,%s,%s)"""

    record_to_insert = [
        (1, "Packt", 1950, "chennai", "books"),
        (2, "Springer", 1950, "chennai", "books"),
        (3, "Springer", 1950, "chennai", "articles"),
        (4, "Oxford", 1950, "chennai", "all"),
        (5, "MIT", 1950, "chennai", "books"),
    ]
    for i in record_to_insert:
        cursor.execute(postgres_insert_query, i)

        conn.commit()
        count = cursor.rowcount
        print(
            count,
            f"Record inserted successfully into {TABLE_NAME} table",
        )

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into publisher table", error)

try:
    postgreSQL_select_Query = f"select * from {TABLE_NAME}"

    cursor.execute(postgreSQL_select_Query)
    print(f"\nSelecting rows from {TABLE_NAME} table using cursor.fetchall")
    records = cursor.fetchall()

    for row in records:
        print(
            "publisher_id = ",
            row[0],
        )
        print("publisher_name = ", row[1])
        print("publisher_estd = ", row[2])
        print("publisher_location = ", row[3])
        print("publisher_type = ", row[4], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)


cursor.close()
conn.close()
print("PostgreSQL connection is closed")

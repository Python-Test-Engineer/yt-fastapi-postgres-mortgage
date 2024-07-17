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

TABLE_NAME = "publisher"

try:
    postgres_insert_query = f""" INSERT INTO {TABLE_NAME} (publisher_id,
	publisher_name, publisher_estd, publsiher_location, publsiher_type)
	VALUES (%s,%s,%s,%s,%s)"""

    record_to_insert = [
        (1001, "Packt", 1950, "chennai", "books"),
        (1002, "Packt", 1950, "chennai", "books"),
        (1003, "Packt", 1950, "chennai", "books"),
        (1004, "Packt", 1950, "chennai", "books"),
        (661, "Packt", 1950, "chennai", "books"),
        (662, "Springer", 1950, "chennai", "books"),
        (663, "Springer", 1950, "chennai", "articles"),
        (667, "Oxford", 1950, "chennai", "all"),
        (645, "MIT", 1950, "chennai", "books"),
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

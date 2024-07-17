import psycopg2


def bulkInsert(records):
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="host.docker.internal",
        )
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO employee (name, state) 
                           VALUES (%s,%s) """

        # executemany() to insert multiple rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        print(f"Failed inserting record into mobile table {error}")

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


records_to_insert = [("Ted", "NC"), ("Pete", "AZ")]
bulkInsert(records_to_insert)

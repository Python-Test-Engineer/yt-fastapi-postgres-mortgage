import psycopg2
import string
import random


def get_random_string(n):
    result = "".join(random.choices(string.ascii_uppercase + string.digits, k=n1))
    return result


try:
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal",
        # host="postgres", # does not work
    )
    cursor = connection.cursor()
    for i in range(20):
        n1 = random.randint(5, 15)
        n2 = random.randint(3, 10)
        postgres_insert_query = """ INSERT into employee(name, state) VALUES (%s, %s)"""
        record_to_insert = (get_random_string(n1), get_random_string(n2))
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

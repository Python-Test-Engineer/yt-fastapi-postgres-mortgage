import pytest
import psycopg2


def test_db_true():
    assert True


def test_can_connect_to_db():

    # Establishing the connection
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="localhost",  # "host.docker.internal",
    )
    if conn:
        print(f"\tConnected to DB...\n")
        assert True
        # print(conn)
    else:
        print("NO CONNECTION\n")
        assert False


def test_check_rows_in_employee_table_not_zero():

    # Establishing the connection
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="localhost",  # "host.docker.internal",
    )
    if conn:
        print(f"\tConnected to DB...\n")
        # print(conn)
    else:
        print("NO CONNECTION\n")

    cursor = conn.cursor()

    # Ensure employee table has been created and loaded with data from sql_postgres
    sql = f""" SELECT COUNT(*) FROM employee"""

    cursor.execute(sql)
    result = cursor.fetchone()

    # conn.commit()
    print(f"test completed OK with {result} rows returned\n")
    assert result[0] > 50

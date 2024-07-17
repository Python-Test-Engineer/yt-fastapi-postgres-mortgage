# FastAPI Postgres Docker Mortgage

For more info on registering with PgAdmin and Adminer see [https://github.com/Python-Test-Engineer/yt-docker-to-go/tree/main/python-postgres-pgadmin-adminer](https://github.com/Python-Test-Engineer/yt-docker-to-go/tree/main/python-postgres-pgadmin-adminer)

- python -m venv venv
- .\venv\Scripts\activate
- pip install - requirements.txt
- docker compose up -d
- fastapi run .\app\main.py --reload
- http://localhost:8000/api/healthchecker  
- python .\sql_postgres\02_sql_crud_create_table_employee.py # create table
- python .\sql_postgres\04_sql_crud_insert_random_many_employee.py # load data
- python -m pytest -vs tests/01_postgres # run postgres wiring tests
- python -m pytest -vs --dburl=postgresql://postgres:postgres@localhost:5432/postgres tests/02_mortgage # run mortgage_calculator tests
- python -m pytest -vs --dburl=postgresql://postgres:postgres@localhost:5433/postgres tests/02_mortgage # run mortgage_calculator tests in test_db 5433


##  API

- `fastapi run .\app\main.py --reload`
- http://localhost:8000/api/healthchecker     

api works

![API HEALTHCHECKER OK](./images/api-healthchecker-OK.png)

## Docker

docker compose uses postgres for all and I use my version with PgAdmin - see `docker.compose.yml` which is now in root

```
  postgres:  
    container_name: postgres_local  
    image: postgres:16-alpine #postgres:
    environment:
      - POSTGRES_DB=postgres # optional
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
```
and in `app/database.py`:

```
# Get Postgres Environment Variables
POSTGRES_HOST = "host.docker.internal"
POSTGRES_HOST = "localhost"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "postgres"


# SQLALCHEMY_DATABASE_URL = "sqlite:///./mortgage.db"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
)
```

tables created in DB

![TABLES CREATED](./images/pgadmin.png)

sql crud works OK - tested with publisher and employee in slq_postgres folder

The following are used in Python CRUD in sql_postgres folder

```
POSTGRES_HOST = "host.docker.internal" # localhost now seems to work...
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "postgres"
```

## PyTest

works OK for SQLite

Tests for `python -m pytest -vs tests/01_postgres` work OK using:

```
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="host.docker.internal", # localhost now seems to work...
    )
```
as we get PASS for connecting and getting row count > 0 for employee table after sql_postgres\02 and 04 run

`python -m pytest -vs --dburl=postgresql://postgres:postgres@localhost:5432/postgres tests/02_mortgage`

Test DB uses 5433

`python -m pytest -vs --dburl=postgresql://postgres:postgres@localhost:5433/postgres tests/02_mortgage` 





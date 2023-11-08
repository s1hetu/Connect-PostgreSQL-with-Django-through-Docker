## Connect PostgreSQL with Django through Docker
Create docker-compose.yaml file

1. Create a service for Django App
    - Provide port as 8000 (default for Django, can be updated.)
    - Provide environment variables
      - DB_NAME=<ANY_DB_NAME_OF_CHOICE>
      - DB_USER=<ANY_USERNAME>
      - DB_PASS=<ANY_PASSWORD>
      - DB_HOST=PostgreSQL Service name
    - Provide depends_on as PostgreSQL Service name


2. Create a service for PostgreSQL DB
    - Provide image as the postgres image
    - Provide port as 5432 (default for PostgreSQL, can be updated)
    - Provide environment variables
        - POSTGRES_DB=<ANY_DB_NAME_OF_CHOICE>
        - POSTGRES_USER=<ANY_USERNAME>
        - POSTGRES_PASSWORD=<ANY_PASSWORD>


## Create Super User
docker-compose run <SERVICE_NAME> python manage.py createsuperuser
```shell
docker-compose run test_db_conn_postgres python manage.py createsuperuser
```

## Build App
docker-compose build <SERVICE_NAME>
```shell
docker-compose build test_db_conn_postgres
```

## Run Django App
docker-compose up/run <SERVICE_NAME>
```shell
docker-compose up test_db_conn_postgres
```
<hr>
<br>




    

## NOTE
```
If you see Postgres Error, try changing PORT NUMBER.
```

<br>

## Check if DB got created
docker-compose exec <SERVICE_NAME> psql --username=<USER_NAME> --dbname=<DB_NAME>
```shell
docker-compose exec postgres_db psql --username=postgres --dbname=Test_DB1
```

```shell
\dt
```
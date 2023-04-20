=== TODO ===
secure connection with token to server (OAUTH2) (https://django-oauth-toolkit.readthedocs.io/en/stable/getting_started.html)
Front-End Pages: Login, Register, ForgotPassword, Place an order, Confirmation Page, your account, 404 page
add more info admin
encryption for ccv and card number
password hash

Add db User
    Token
    Username 
    password
    email
    last connected
    account created

Learn REGEX
Learn mongodb


=== Django Command ===
django-admin startproject [name of project] : Create project
django-admin startapp [name of app] : Create app

python3 manage.py inspectdb : Create a model from database
python3 manage.py runserver : run django server
python3 manage.py createsuperuser : create super user to access admin page

sqlite3 [database name] : open specified database
sqlite3 [database name] < [sql command file] : run a certain sql command

== sqlite3 ==
    .table : see all table
    .schema [table name] : see schema of specified table
    .exit : quit sqlite command line


== Postgres ==
psql : open postgres terminal
    CREATE TABLESPACE [name of tablespace] : create a table space (save a location for db)
    CREATE DATABASE [name of database] TABLESPACE [name of tablespace]: create a database in a specified location
    \l : List all the databases
    \db : List all the tablespaces
    \dt : show tables 
    \du : Show users
    SELECT rolname FROM pg_roles; : see all the roles


    psql
    DROP DATABASE db_cpfdualam;
    CREATE DATABASE db_cpfdualam TABLESPACE cpfdualam;
    \q
    psql -d db_cpfdualam -f /Users/dgauthier/Desktop/Django/CPFDUALAM/api/db_CPF_postgres.sql
# Essential Oils Database

Essential oils of Himachal database is a database project which will help maintain the data of plants and the essential oils they contain and help the users to retrieve that information easily using a web application.

## Installation instructions

1. Clone the project from `https://github.com/Varunvaruns9/EssentialOilsDatabase.git`

2. Install [PostgreSQL](https://www.postgresql.org/download/)

3. Run these commands in `psql` prompt to create the database (Use a different password and username).
```
CREATE DATABASE oilsdb;
CREATE USER admin WITH PASSWORD 'adminpass';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'Asia/Kolkata';
exit
```

4. Change the database username and password in the `oilsdb/settings.py` file. Use the same credentials as used in the last step.

5. Install the requirements (Preferable if done in a virtual environment).
```
pip install requirements.txt
```

6. Create the database and create the admin account.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

7. Run the server.
```
python manage.py runserver
```

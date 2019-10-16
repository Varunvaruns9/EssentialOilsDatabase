# Essential Oils Database

Essential oils of Himachal database is a database project which will help maintain the data of plants and the essential oils they contain and help the users to retrieve that information easily using a web application.

## Installation instructions

1. Clone the project from `https://github.com/Varunvaruns9/EssentialOilsDatabase.git`

2. Install the requirements (requires a properly configured version of PostgreSQL).
```
pip install requirements.txt
```

3. Create the database and create the admin account.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

4. Run the server.
```
python manage.py runserver
```

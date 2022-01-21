CREATE PostgreSQL
----
        pip install psycopg2-binary


1. Create user and DB in PostgreSQL
         
         sudo su postgres
         psql
         CREATE USER user_1 WITH PASSWORD 'user' CREATEDB;
         CREATE DATABASE test_db OWNER user_1;
         GRANT ALL PRIVILEGES ON DATABASE test_db TO user_1;
         exit



         DATABASES = {
             "default": {
                 "ENGINE": "django.db.backends.postgresql",
                 "NAME": "test_db",
                 "USER": "user_1",
                 "PASSWORD": "user",
                 "HOST": "localhost",
                 "PORT": 5432,
             }
         }
         


2. Requirements.txt
         
         pip install -r requirements.txt  
         pip freeze > requirements.txt


3. Create new "post"

         python manage.py startapp post

4. Createsuperuser
         
         python manage.py createsuperuser

5. Create  migrations

         python manage.py makemigrations
         python manage.py migrate
Virtual environment
----
Run from the project root

      python3.9 -m venv --copies venv

activate

      source venv/bin/activate

and install packages
      
      pip install -r requirements.txt


PostgreSQL
----
Create database and user
         
    sudo su postgresx
    psql
    CREATE USER user_1 WITH PASSWORD 'user' CREATEDB;
    CREATE DATABASE test_db OWNER user_1;
    GRANT ALL PRIVILEGES ON DATABASE test_db TO user_1;
    exit


Django
----
Edit `settings.py`

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


Superuser

    python manage.py createsuperuser --username admin

Run db migrations

    python manage.py makemigrations
    python manage.py migrate

    * check with linter (optional)
    python manage.py makemigrations --lint post



Collect static files in `app/static`

    python manage.py collectstatic


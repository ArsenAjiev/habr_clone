Virtual environment
----
Run from the project root
```shell
python3.9 -m venv --copies venv
```
activate
```shell
source venv/bin/activate
```

and install packages
      
```shell
pip install -r requirements.txt

pip freeze > requirements.txt
```


PostgreSQL
----
Create database and user
```shell
sudo su postgres
psql
```
```postgresql
CREATE USER user_1 WITH PASSWORD 'user' CREATEDB;
CREATE DATABASE test_db OWNER user_1;
GRANT ALL PRIVILEGES ON DATABASE test_db TO user_1;
```
```shell
exit
```

Django
----
Edit `settings.py`
```python
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
```

Superuser
```shell
python manage.py createsuperuser --username admin
```
    

Run db migrations
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```
```shell
# check with linter (optional)
python manage.py makemigrations --lint post
```



Collect static files in `app/static`
```shell
python manage.py collectstatic -c --no-input
```

Pytest
----
Run pytest
```shell

pip install pytest-django
pip install pytest-cov

pytest -s -v tests/
pytest --cov  --cov-report=html


```


django.test
----
Run tests
```shell


# Run all the tests
$ python manage.py test 

# Run all the tests found within the 'tests' package
$ python manage.py test tests

# Run all the tests in the tests.test_view_index module
$ python manage.py test tests.test_view_index

# Run just one test case
$ python manage.py test tests.test_view_index.PostIndexView

# Run just one test method
$ python manage.py test tests.test_view_index.PostIndexView.test_no_post

```
     Example how to сreate multiple instances
     number_of_students = 30
     for student_id in range(number_of_students):
        Student.objects.create(first_name=f"John{student_id}", last_name=f"Doe{student_id}")




Django-taggit 2.1.0
----
Run django-taggit 
```shell

pip install django-taggit

Add "taggit" to your INSTALLED_APPS
---------------------------------------
from django.db import models

from taggit.managers import TaggableManager


class Food(models.Model):
    # ... fields here

    tags = TaggableManager()
________________________________________

python manage.py makemigrations
python manage.py migrate
________________________________________

>>> apple = Food.objects.create(name="apple")
>>> apple.tags.add("red", "green", "delicious")
>>> apple.tags.all()
[<Tag: red>, <Tag: green>, <Tag: delicious>]
>>> apple.tags.remove("green")
>>> apple.tags.all()
[<Tag: red>, <Tag: delicious>]
>>> Food.objects.filter(tags__name__in=["red"])
[<Food: apple>, <Food: cherry>]    

```



# How to run Docker

### delete images, containers, volumes
```shell
# Show images, containers, volumes
docker ps -a
docker images
docker volume ls
```
```shell
# Delete images, containers, volumes
docker system prune -a
docker volume prune
```

### Create environment and install packages
```shell
# Create environment
python3.8 -m venv --copies app/venv
# Activate
source app/venv/bin/activate
# Make sure to use app/venv/bin/pip3.8 
which pip3.8
# Install packages
pip3.8 install -r app/requirements.txt
```


Collect static files in `app/static`
```shell
python manage.py collectstatic -c --no-input
```

### Run all at once

```shell
docker-compose up -d --build --force-recreate
```

Run db migrations
```shell
docker-compose exec app ./manage.py makemigrations --lint post
```
```shell
docker-compose exec app ./manage.py migrate
```





```shell
docker-compose exec app ./manage.py createsuperuser
```

### Create Category model 'Economy', 'Technology', 'Sport', 'Music'  
```shell
docker-compose exec app ./manage.py create_category

```

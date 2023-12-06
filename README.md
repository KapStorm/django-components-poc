# PoC django-components and django-tailwind

This is a proof of concept for using [django-components](https://github.com/EmilStenstrom/django-components) and [django-tailwind](https://github.com/timonweb/django-tailwind/).

## How to run
- Create a virtual environment and install the requirements
```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Views
- Open the browser at http://127.0.0.1:8000/users/ to see the PoC without tailwind
- Open the browser at http://127.0.0.1:8000/users/tailwind/ to see the PoC with tailwind
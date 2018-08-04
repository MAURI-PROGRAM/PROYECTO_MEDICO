python --version
django-admin --version

django-admin startproject Clinica_Website
python manage.py satrapp Registros

python manage.py makemigrations Registros

python manage.py migrate

python manage.py createsuperuser

python manage.py showmigrations

python manage.py migrate --fake Registros zero
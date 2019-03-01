# Trip-Buddy
Python, Django, SQLite

cd Trip-Buddy

pip install virtualenv

virtualenv virtual

## initiate a virtual environment

source virtual/bin/activate 

## install dependecies
pip install -r requirements.txt
pip list

## run migrations
python manage.py makemigrations
python manage.py migrate

## run the server
python manage.py runserver 0.0.0.0:5000

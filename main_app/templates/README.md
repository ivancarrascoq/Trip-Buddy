git clone https://github.com/ivancarrascoq/Trip-Buddy.git
cd Trip-Buddy
pip install virtualenv
virtualenv virtual
source virtual/bin/activate 
pip install -r requirements.txt
pip list
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:5000
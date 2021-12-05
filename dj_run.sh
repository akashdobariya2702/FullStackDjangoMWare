pip3 install --upgrade virtualenv
virtualenv -p python3.6 venv
source venv/bin/activate

pip3 install -r requirements.txt
python manage.py migrate
#python manage.py loaddata file.json
python manage.py collectstatic --noinput
python manage.py test
python manage.py runserver

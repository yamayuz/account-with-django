# User管理のデモ
## Setup
install Python libraries
```
pip install -r requirements.txt
```

DB migrations and create superuser
```
./manage.py makemigrations
./manage.py migrate
python3 manage.py createsuperuser
```

run local server
```
python3 manage.py runserver
```
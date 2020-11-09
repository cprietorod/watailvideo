# Wagtail proof of concept to use the document component to handle videos.

## Requirements
* python 3.7
* virtualenv
* gcloud

## Installation
* create virtualenv
```
virtualenv -p $(which python3) venv
source venv/bin/activate
```
* Install requirements
```
pip install -r requirements.txt
```

* Configure database 
```
python3 manage.py migrate
```

## how to run it
* create super user
```
python3 manage.py createsuperuser
```

* run server 
```
python3 manage.py runserver 0.0.0.0:8000
```


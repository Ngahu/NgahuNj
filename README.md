
## Project Overview
Personal website and blog built with  [Python](https://www.python.org/) and [Django](https://www.djangoproject.com).





## Required Features





# Installation and Setup
```
https://github.com/Ngahu/NgahuNj
```


## Create a virtual environment

```
python3 -m venv venv;
source venv/bin/activate
```
If you need to install virtualenv:
```
virtualenv venv
```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```
source venv/bin/activate
```
## Install requirements
```
pip install -r dev_requirements.txt
```


## Running the application
After the configuration, you will run the app 
```
cd ngahunj

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

